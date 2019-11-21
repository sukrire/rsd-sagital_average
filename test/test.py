import numpy as np
import subprocess


correct= np.genfromtxt('brain_average_correct.csv', delimiter=",")

#create input file
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')
 


#run command
subprocess.run(["python","sagital_brain.py"])

test= np.genfromtxt('brain_average.csv', delimiter=",")

np.testing.assert_array_equal(test,correct) 