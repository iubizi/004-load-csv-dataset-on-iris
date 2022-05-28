f = open('iris.csv', 'r')
lines = f.readlines()
f.close()

data, label = [], []

for line in lines[1:]: # ignore first line which are feature names
    
    line = line.replace('\n', '').split(',')
    data.append(list(map(float, line[:-1])))
    label.append(int(line[-1]))

import numpy as np
data, label = np.array(data), np.array(label)

print(data)
print(label)
