import numpy as np

N = np.array(list(map(int, input())))
mid = int(len(N)/2)
left = N[:mid]
right = N[mid:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
