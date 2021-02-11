# younicam-AI

Machine Learning project developed in Pyspark. The model uses the dataset related to the anonymized presences registered via the Younicam app in the University of Camerino buildings to predict the number of people in a room during a precise time interval.

[TPOT](https://epistasislab.github.io/tpot/) is used in the model training phase to get the best combination between the ML model and hyperparameters.

## Install dependencies 

To install the project dependencies run the following command:

```bash
pip3 install -r requirements.txt
```


## Structure

The repository has the following structure:

* *data* : this folder contains the original dataset plus some other intermediary transformations
* *notebooks* : contains all the notebooks used during experimentation
* *predictions* : contains the final predictions results in csv format

## Authors

* **Yuri Paoloni** - [yuripaoloni](https://github.com/yuripaoloni)
* **Matteo Leonesi** - [MatteoLeonesi](https://github.com/MatteoLeonesi)
