# 004-load-csv-dataset-on-iris

load csv dataset on iris

The data stored in csv is a string, and the string data needs to be converted into float data for data processing. Using the map function can easily solve the problem of batch data conversion.

The csv file can easily process the data, and opening it with excel makes it easier to visualize the data. However, the csv file does not contain data compression, cannot store a large amount of data and takes up a lot of computer space, so it is necessary to introduce a compression encoding format such as npz or h5 to store a large amount of data.
