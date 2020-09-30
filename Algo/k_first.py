#!/usr/bin/python
# -*-coding:utf-8 -*

import numpy

""" k_last_elem possible """
# import sys
# sys.setrecursionlimit(100000)

liste = list(numpy.random.permutation(numpy.arange(10000)))

def k_first_elem(ensemble, k):
    ensemble = ensemble.copy()
    for i in range (0, min(k , len(ensemble))):
        for j in range (i + 1, len(ensemble)):
            if ensemble[i] > ensemble[j]:
                ensemble[i], ensemble[j] = ensemble[j], ensemble[i]
    return ensemble[:k]

print(k_last_elem(liste, 5))