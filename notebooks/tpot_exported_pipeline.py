import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import MinMaxScaler, RobustScaler
from tpot.builtins import StackingEstimator

tpot_data = pd.read_json("../data/engineered/presences.json")
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

exported_pipeline = make_pipeline(
    MinMaxScaler(),
    RobustScaler(),
    StackingEstimator(estimator=SGDRegressor(alpha=0.01, eta0=0.1, fit_intercept=False, l1_ratio=0.5, learning_rate="invscaling", loss="squared_loss", penalty="elasticnet", power_t=0.1)),
    SelectFromModel(estimator=ExtraTreesRegressor(max_features=0.9500000000000001, n_estimators=100), threshold=0.05),
    RandomForestRegressor(bootstrap=True, max_features=0.45, min_samples_leaf=1, min_samples_split=5, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
preds = exported_pipeline.predict(testing_features)

np.savetxt("../predictions/preds.csv", preds, delimiter=",")

accuracy = exported_pipeline.score(testing_features, testing_target)

print("Accuracy:", accuracy)


