import multiprocessing as mp
import os
import time

def func(n):
    
    print("ID of process running successfully: {}".format(os.getpid()))
    print()
    time.sleep(2)   #simulate processing or server return time
    print("Task {} has done now.".format(n))


if __name__ == '__main__':

    nums_core = mp.cpu_count()
    print("There are {} cores being used now.".format(nums_core))
    pool = mp.Pool(nums_core) #use all available cores
    for i in range(0, 20):
        pool.apply_async(func, args=(i,))
    pool.close()
    pool.join()