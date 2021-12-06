import numpy as np


list1 = (0,1,2,3)
array = np.asarray([list1])
list2 = np.asarray([list1])
print(list2)
np.append(array,list2, axis=0)
print(array)