import pandas as pd
import numpy as np

class FullyConnectedNeuralNet:
    def __init__(self):
        self.learnin_rate = 0.00001
    
    def RelU(self, number):
        if number > 0:
            return number
        else:
            return 0

input_layer_size = len(train_file.columns)


# first_hidden_layer = 2500 neurons
# second_hidden_layer = 1536 neurons
# results_layer = 10
# data extraction:
#   - extract results columns
#   - create new data (new csv file) without the results colunms
#   - clone the data from the file to a pandas table - optional (I will check this out)
# feed forward:
#   - initial weights accoding to some weights initialization method
#   - feed the layers with the row including the calculation of the 
#     non-linear function. 
#   - print the expected result and the current result.
#   - keep the result (the layer of the result will be
#     represented as 10 neourons)
# back propogation:
#   - execute the back propogation algorithm according to the result
#   - updtate the weights accordingly.
#   - after finishing iterating the whole data, calculate the accuracy of the
#     epoch and write it to a file.
#   - 




