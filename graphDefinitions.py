import numpy as np
import collections
import sys
import setTheory
import itertools

# The order function calculates the order of the graph.
def order(G):
    n = len(G)
    return n


#The vertexSet function creates an array of vertices of the graph.
def vertexSet(G):
    V = range(order(G))
    return V


# The neighbors function finds the neighbors of a given vertex.
def neighbors(G, v):
    neighborhood = []
    for i in range(0, len(G)):
        if G[v][i] == 1:
            neighborhood.append(i)
    return neighborhood


# The degree function calculates the degree of a given vertex.
def degree(G, v):
    dv = len(neighbors(G, v))
    return dv


# The degree sequence function finds the degree sequence of G.
def degreeSeq(G):
    degSeq = [0] * order(G)
    for i in range(0, order(G)):
        degSeq[i] = degree(G, i)
    degSeq.sort(reverse=True)
    return degSeq


# The size function calculates the number of edges in G.
def size(G):
    m = np.sum(degreeSeq(G)) / 2
    return m


# The maxDegree function calculates the maximum degree of G.
def maxDegree(G):
    seq = degreeSeq(G)
    maxD = seq[0]
    return maxD


# The minDegree function calculates the minimum degree of G.
def minDegree(G):
    seq = degreeSeq(G)
    minD = seq[len(seq) - 1]
    return minD


# The maxine function iteratively deletes maximum degree vertices until
# isolates are reached. To see the adjacency matrix after each iteration
# un-comment the #'s in the function. The maxineCardinality represents
# a lower bound on the independence number of G.
def maxine(G):
    newG = G
    while maxDegree(newG) > 0:
        for i in range(0, order(newG)):
            if degree(newG, i) == maxDegree(newG):
                newG = np.delete(newG, (i), axis=0)
                newG = np.delete(newG, (i), axis=1)
                #print "The resulting adjacency matrix is"
                #print newG
                break
    maxineCardinality = len(newG)
    return maxineCardinality


# The residue function iteratively applies the Havel-Hakimi derivatives
# to the degree sequence of G until no further derivatives may be preformed
# the resulting number of zeros is returned. The function is a lower bound
# on the independence number of G.
def residue(G):
    D = degreeSeq(G)
    while D[0] > 0:
        maxD = D[0]
        D.remove(D[0])
        for i in range(0, maxD):
            D[i] = D[i] - 1
        D.sort(reverse=True)
        #print(D[0:len(D)+1])
    residue = len(D)
    return residue


# The annihilation function computes the annihilation number of G. This
# number is an upper bound on the independence number of G.
def annihilation(G):
    D = degreeSeq(G)
    index = len(D) - 1
    m = size(G)
    aSum = D[index]
    l = 1
    while aSum <= m:
        a = l
        aSum = aSum + D[index - l]
        l = l + 1
    return a


# The OpenNeighbors function computes the open neighborhood of a set of
# vertices S.
def openNeighbors(G, S):
    OpenNeighbors = neighbors(G, S[0])
    for i in range(1, len(S)):
        OpenNeighbors = setTheory.union(OpenNeighbors, neighbors(G, S[i]))
    return OpenNeighbors


# The ClosedNeighbors function computes the closed neighborhood of a set
# of vertices S.
def closedNeighbors(G, S):
    ClosedNeighbors = setTheory.union(openNeighbors(G, S), S)
    return ClosedNeighbors


# The following boolean functions determine various properties of subsets
# of vertices in G.

def isDominating(G, S):
    isDom = False
    V = range(order(G))
    if ClosedNeighbors(G, S) == V:
        isDom = True
        print "Dominating =True"
    return isDom


def isTotalDominating(G, S):
    isTotalDom = False
    V = range(order(G))
    if OpenNeighbors(G, S) == V:
        isTotalDom = True
        print "Total Dominating = True"
    return isTotalDom


def isIndependent(G, S):
    isInd = False
    if setTheory.intersect(openNeighbors(G, S), S) == []:
        isInd = True
        print "isIndependent = True"
    return isInd


# The following functions compute various NP-hard invariants

def minDomSet(G):
    for i in range(1, order(G)):
        Combinations = itertools.combinations(vertexSet(G), i)
        Combi = np.array(list(Combinations))
        for i in range(0, len(Combi)):
            S = Combi[i]
            if isDominating(G, S) == True:
                print "The following set is a minimum dominating set:", S
                return S


def domNumber(G):
    gamma = len(minDomSet(G))
    return gamma


def minTotalDomSet(G):
    for i in range(1, order(G)):
        Combinations = itertools.combinations(vertexSet(G), i)
        Combi = np.array(list(Combinations))
        for i in range(0, len(Combi)):
            S = Combi[i]
            if isTotalDominating(G, S) == True:
                # print "The following set is a minimum total dominating set:", S
                return S


def totalDomNumber(G):
    gammat = len(minTotalDomSet(G))
    return gammat


def minIndSet(G):
    V = range(order(G))
    for i in range(order(G), 0, -1):
        Combinations = itertools.combinations(vertexSet(G), i)
        Combi = np.array(list(Combinations))
        for i in range(0, len(Combi)):
            S = Combi[i]
            if isIndependent(G, S) == True:
                print "The following set is a maximum independent set:", S
                return S


def independenceNumber(G):
    alpha = len(minIndSet(G))
    return alpha


def minIndDomSet(G):
    for i in range(1, order(G)):
        Combinations = itertools.combinations(vertexSet(G), i)
        Combi = np.array(list(Combinations))
        for i in range(0, len(Combi)):
            S = Combi[i]
            if isDominating(G, S) and isIndependent(G, S) == True:
                print "The following set is a minimum independent dominating set:", S
                return S


def indDomNumber(G):
    i = len(minIndDomSet(G))
    return i
