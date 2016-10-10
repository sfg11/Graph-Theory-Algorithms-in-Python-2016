

import numpy as np
import collections
import sys
import os
import random
import itertools
import setTheory
import graphDefinitions as graph


# Read the txt file in as an adjacency matrix
T = np.loadtxt("P_3.txt", int)

print "Original tree is:"
print T

n = len(T)
# print "Original tree stored as matrix:\n", T
# print "\n\n\n"
#order = graph.order(T)
# print "Order of original : ", order
#vertexSet = graph.vertexSet(T)
# print "Vertex Set of original: ", vertexSet

#degreeOfV = graph.degree(T, i)
# print "Degree of vertex original", degreeOfV

#neighbors = graph.neighbors(T, i)
# print "Neighbors: ", neighbors

#op = graph.openNeighbors(T, neighbors)
# print "Open Neighbors: ", op

#numEdges = graph.size(T)
# print "Number of edges: ", numEdges
'''
degSeq = graph.degreeSeq(T)
print "Degree Sequence: ", degSeq

maxDegree = graph.maxDegree(T)
# print "Maximum Degree of Tree: ", maxDegree

minDegree = graph.minDegree(T)
# print "Minimum Degree of Tree: ", minDegree

maxine = graph.maxine(T)
print "Maxine: ", maxine

r = graph.residue(T)
print "Residue of original: ", r

annihilationNumber = graph.annihilation(T)
print "Annihilation Number of original Graph: ", annihilationNumber

indepNum = graph.independenceNumber(T)
print "independence number of T", indepNum
'''
for i in range(0,n):

    Tree = T
    Tree = np.insert(Tree,n, values = 0, axis = 1)
    Tree = np.insert(Tree,n, values = 0, axis = 0)
    Tree[i][n] = 1
    Tree[n][i] = 1
    nTree=len(Tree)

    m = np.matrix(Tree)
    print "Tree stored as matrix:\n", m

    print "\t"
    order = graph.order(Tree)
    print "Order: ", order

    vertexSet = graph.vertexSet(Tree)
    #print "Vertex Set: ", vertexSet

    degreeOfV = graph.degree(Tree, i)
    #print "Degree of vertex", degreeOfV

    neighbors = graph.neighbors(Tree, i)
    #print "Neighbors: ", neighbors

    op = graph.openNeighbors(Tree, neighbors)
    #print "Open Neighbors: ", op
    numEdges = graph.size(Tree)
    #print "Number of edges: ", numEdges
    maxDegree = graph.maxDegree(Tree)
    #print "Maximum Degree of Tree: ", maxDegree

    minDegree = graph.minDegree(Tree)
    #print "Minimum Degree of Tree: ", minDegree

    degSeq = graph.degreeSeq(Tree)
    print "Degree Sequence: ", degSeq
    print "\t"

    maxine = graph.maxine(Tree)
    print "Maxine: ", maxine
    r = graph.residue(Tree)
    print "Residue: ", r

    annihilationNumber = graph.annihilation(Tree)
    print "Annihilation Number of Graph: ", annihilationNumber
    indepNum = graph.independenceNumber(Tree)
    print "Independence number:", indepNum
    print "\t"
    #isDom = graph.isDominating(Tree,i)
    #print "Is dominating", isDom


