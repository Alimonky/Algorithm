import random


def MergeSort(A, p, r):
    q=(p+r)/2
    if p<r:
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
    return MergeSort(A ,p,q,r)


def MergeSort(A ,p,q,r):


