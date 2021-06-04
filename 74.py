"""
Exercise for reference: 

Please concatenate this file with this one to a single text file. The content of the output file should look like in the expected output.

"""

import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])