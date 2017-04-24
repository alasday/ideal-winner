# Asher Lasday
# SoftDev2 pd8
# HW11 -- Ready, Set, Math!
# 2017-04-23

def intersection(A,B):
    return [a for a in A if a in B]

def diff(A,B):
    return [a for a in A if a not in B]

def union(A,B):
    return diff(A,B) + B

def symDiff(A,B):
    return diff(A,B) + diff(B,A)

def cartesian(A,B):
    return [[a, b] for a in A for b in B]


