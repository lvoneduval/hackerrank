import numpy
#python3
import numpy as np
A = np.array(input().split(), float)
B = float(input())
print(numpy.polyval(A,B))
