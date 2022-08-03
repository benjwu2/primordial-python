import matplotlib.pyplot as plt
import numpy as np
import math

# array1 = np.linspace(10,20,11)
# array2 = np.array(1:1:100)

def Example():
    x = range(1,11)
    Numbers = []
    for n in x:
        Numbers.append(n)
    return Numbers

Numbers = Example()

print('Numbers type is: ' + str(type(Numbers)))
Numbers2 = list(Numbers)
Numbers2.append('a')
print(Numbers2)
print('Numbers 2 type is: ' + str(type(Numbers2)))