import time
startTime = time.time()
from multiprocessing import Pool

def square(x):
    return x**2


if __name__ == "__main__":
    pool = Pool(processes=2)
    for i in range(100):
        print(square(i),)
    print(pool.map(square, range(100)))
    print("total time taken ", time.time() - startTime)