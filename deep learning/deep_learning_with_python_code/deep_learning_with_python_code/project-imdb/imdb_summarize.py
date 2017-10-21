# Summarize the IMDB problem
import numpy
from keras.datasets import imdb
from matplotlib import pyplot
# load the dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data(test_split=0)
# summarize size
print("Training data: ")
print(X_train.shape)
print(y_train.shape)
# Summarize number of classes
print("Classes: ")
print(numpy.unique(y_train))
# Summarize number of words
print("Number of words: ")
print(len(numpy.unique(X_train)))
# Summarize review length
print("Review length: ")
result = map(len, X_train)
print("Mean %.2f words (%f)" % (numpy.mean(result), numpy.std(result)))
# plot review length as a boxplot and histogram
pyplot.subplot(121)
pyplot.boxplot(result)
pyplot.subplot(122)
pyplot.hist(result)
pyplot.show()





# Training data:
# (25000,)
# (25000,)
# Classes:
# [0 1]
# Number of words:
# 24902
# Review length:
# Mean 285.84 words (212.622320)
