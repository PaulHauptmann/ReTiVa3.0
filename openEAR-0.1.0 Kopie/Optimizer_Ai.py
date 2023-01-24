import tensorflow as tf
import pandas as pd


COLUMN_NAMES = [
        'SepalLength', 
        'SepalWidth',
        'PetalLength', 
        'PetalWidth', 
        'Species'
        ]

# Import training dataset
training_dataset = pd.read_csv('/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/iris_training.csv', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0:4]
train_y = training_dataset.iloc[:, 4]

# Import testing dataset
test_dataset = pd.read_csv('/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/Iris_test.csv', names=COLUMN_NAMES, header=0)
test_x = test_dataset.iloc[:, 0:4]
test_y = test_dataset.iloc[:, 4]

columns_feat = [
    tf.feature_column.numeric_column(key='SepalLength'),
    tf.feature_column.numeric_column(key='SepalWidth'),
    tf.feature_column.numeric_column(key='PetalLength'),
    tf.feature_column.numeric_column(key='PetalWidth')
]

classifier = tf.estimator.DNNClassifier(
    feature_columns=columns_feat,
    # Two hidden layers of 10 nodes each.
    hidden_units=[10, 10],
    # The model is classifying 3 classes
    n_classes=3)

# Define train function
def train_function(inputs, outputs, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(inputs), outputs))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()

# Train the Model.
classifier.train(
    input_fn=lambda:train_function(train_x, train_y, 100),
    steps=1000)
# Define evaluation function
def evaluation_function(attributes, classes, batch_size):
    attributes=dict(attributes)
    if classes is None:
        inputs = attributes
    else:
        inputs = (attributes, classes)
    dataset = tf.data.Dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()

# Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:evaluation_function(test_x, test_y, 100))