# Future Work

A list of possible future implementation:

- test again the model with a larger amount of data

- using the progressive numerical values on the columns room, building and city imply that there is an order among the values in this category and that this specific order is
  important for the decision making. But, if the order of a feature’s values is not important, using ordered numbers as values is likely to confuse the learning algorithm, because the algorithm will try to find a regularity where there’s no one, which may potentially lead to overfitting. A solution could be applying one-hot encoding increasing the dimensionality of the feature vectors, e.g. [1, 0, 0] for a room and [0, 1, 0] for another one. Of course, we will need a more long array to cover all the combinations.
