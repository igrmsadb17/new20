import numpy as np

a = np.identity(4)
print(a)

a1 = np.arange(1,5)
print(a1)

a2 = a*a1

np.max(a2, axis = 0)

a2[2:, 2: ]

# extract 1, 2, 3, 4
a2[[0, 1, 2, 3], [0, 1, 2, 3]]
