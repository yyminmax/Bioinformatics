#!/usr/bin/env python

from __future__ import division
import os
import sys
import numpy as np

fp = open(sys.argv[1], 'r')
fp1 = open('distance.txt', 'w')
#modify the distance and bulid the sample index

sample = fp.readline().strip('\n').split('\t')

for line in fp:
	row = line.split('\t')
	del row[0]
	new_line = '\t'.join(row)
	fp1.write(new_line)

fp.close()
fp1.close()

# build the tree by upgma

def Find_Min_Dis_Group(matrix):
	m,n = np.shape(matrix)
	spot_row = 1
	spot_col = 0
	Min = dis_matrix[1,0]
	print Min
	for i in range(1,m):
		for j in range(i):
			if(dis_matrix[i,j] < Min):
				Min = dis_matrix[i,j]		
				spot_row = i
				spot_col = j
	return spot_row,spot_col
	
def Make_a_New_Matrix(matrix, spot_row, spot_col):
	Min = matrix[spot_row, spot_col]
	dis = Min/2
	m,n = np.shape(matrix)
	#new_matrix = np.zero((m-1)*(n-1)).reshape(m-1,n-1)
	spot = min(spot_row, spot_col)
	spot_max = max(spot_row, spot_col)
	L = []
	for i in range(1,m):
		if(i != spot_row & i != spot_col):
			value = (matrix[i,spot_row] + matrix[i,spot_col])/2
			print value
			matrix[spot,i] = value
			matrix[i,spot] = value
	np.delete(matrix, spot_max, axis=0)
	np.delete(matrix, spot_max, axis=1)
	return matrix

def Make_new_Sample(sample, spot_row, spot_col):
	spot = min(spot_row, spot_col)
	L = [sample[spot_row], sample[spot_col]]
	sample.(spot, L)
	del sample[spot_row]
	del sample[spot_col]
	return sample

dis_matrix = np.loadtxt('distance.txt')
spot_row,spot_col = Find_Min_Dis_Group(dis_matrix)
print spot_row 
print spot_col
sample = Make_new_Sample(sample, spot_row, spot_col)
matrix = Make_a_New_Matrix(dis_matrix, spot_row, spot_col)

print sample
print matrix
