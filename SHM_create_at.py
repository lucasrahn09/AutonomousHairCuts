import numpy as np
import matplotlib.pyplot as plt
import math


def shm_accel(A, w, total_time, val_per_second):
    # accel = -Aw^2cos(wt)
    ti = total_time*val_per_second
    at = np.zeros((2, ti))
    for i in range(ti):
        t = total_time*i/(ti-1)
        at[0, i] = t
        at[1, i] = -A*w**2*math.cos(w*t)
    np.savetxt('SHM_acceleration.csv', at.transpose(), delimiter=',')
    return at


if __name__ == '__main__':
    A = 1
    w = 4*math.pi
    total_time = 3 # seconds
    val_per_second = 101 # Hz
    at = shm_accel(A, w, total_time, val_per_second)
    plt.plot(at[0], at[1])
    plt.show()
