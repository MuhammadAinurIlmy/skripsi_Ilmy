import math
import numpy as np

# function metode des


def des(nilai_xt, s1t, s2t, dtype=int):
    alfa = 0.61
    s1t = ((alfa*nilai_xt) + ((1 - alfa)*s1t))
    s2t = ((alfa*s1t) + ((1 - alfa)*s2t))
    at = ((2*s1t)-s2t)
    bt = (alfa/(1 - alfa)*(s1t - s2t))
    atbt = at + bt
    # -----------------------------------------------------------
    # print('s1t: ', "%.3f" % s1t)
    # print('s2t:', "%.3f" % s2t)
    # print('at:', "%.3f" % at)
    # print('bt:', "%.3f" % bt)
    # print('at+bt:', "%.3f" % atbt)
    # print('Type data as interger in array:')
    hasil = np.array([s1t, s2t, at, bt, atbt])
    print(hasil.astype(int))


# format(nilai, s1t, s2t)
des(2, 116, 116)
