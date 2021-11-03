import pickle
from utils.preprocess import load_data, create_training_data, bag_of_words
from utils.model import create_model, train_model
import tensorflow as tf
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")

# stemmer = LancasterStemmer()

# Load dataset
words, labels, docs = load_data("intents.json")
docs_x, docs_y = docs

# create trainning data
training, output = create_training_data(words, labels, docs_x, docs_y)

with open("data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)

print(output)

# model creation
model = create_model(len(training[0]), len(output[0]))

train_model(model, training, output, epoch=100, save=True, filename="model/model.h5", callbacks=[tensorboard_callback])
