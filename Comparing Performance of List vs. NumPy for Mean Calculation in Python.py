import numpy as np
import time

a = np.random.rand(100000000)

# # list
# start = time.time()
# mean_list = sum(a) / len(a)
# print(time.time() - start)

# # numpy
# start = time.time()
# mean_numpy = np.mean(a)
# print(time.time() - start)

print(np.__version__)