import tensorflow as tf
import pandas as pd


COLUMN_NAMES = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness","True_Emotion"]

# Import training dataset
training_dataset = pd.read_csv('/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/Optimizer_training.csv', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0:7]
train_y = training_dataset.iloc[:, 7]

# Import testing dataset
test_dataset = pd.read_csv('/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/Optimizer_Testing.csv', names=COLUMN_NAMES, header=0)
test_x = test_dataset.iloc[:, 0:7]
test_y = test_dataset.iloc[:, 7]

columns_feat = [
    tf.feature_column.numeric_column(key='Anger'),
    tf.feature_column.numeric_column(key='Boredom'),
    tf.feature_column.numeric_column(key='Disgust'),
    tf.feature_column.numeric_column(key='Fear'),
    tf.feature_column.numeric_column(key='Happiness'),
    tf.feature_column.numeric_column(key='Neutral'),
    tf.feature_column.numeric_column(key='Sadness')
    
]

classifier = tf.estimator.DNNClassifier(
    feature_columns=columns_feat,
    # Two hidden layers of 10 nodes each.
    hidden_units=[10, 10],
    # The model is classifying 7 classes
    n_classes=7)

# Define train function
def train_function(inputs, outputs, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((dict(inputs), outputs))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset.tf.compat.v1.data.make_one_shot_iterator().get_next()

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