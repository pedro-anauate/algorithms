# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:49:25 2021

@author: pedro
"""

# define adjacent nodes and distances

grid =   {'SL':[('CH',300),('IN',245),('LV',263),('NV',312)],
         'CH':[('SL',300),('IN',201),('CL',362)],
         'IN':[('SL',245),('CH',201),('LV',114),('CI',112),('CO',176)],
         'LV':[('SL',263),('IN',214),('NV',175),('LX',86)],
         'NV':[('SL',312),('LV',175),('KV',180)],
         'CI':[('IN',112),('LX',95),('CO',105),('CN',204)],
         'LX':[('KV',170),('LV',86),('CI',95),('CN',177)],
         'KV':[('NV',180),('LX',170),('GR',299)],
         'CO':[('CI',105),('IN',176),('CL',142)],
         'CL':[('CH',362),('CO',142),('CN',251),('MT',201),('HB',332)],
         'CN':[('CL',251),('CI',204),('LX',177),('GR',244),('RI',317),('MT',157)],
         'GR':[('KV',299),('RI',205),('CN',244)],
         'MT':[('CL',201),('CN',157),('WA',209),('HB',213)],
         'HB':[('CL',332),('MT',213),('WA',120)],
         'WA':[('HB',120),('MT',209),('RI',111)],
         'RI':[('GR',205),('CN',318),('WA',111)]}

nodes = list(grid.keys())

# initialize S, P and L for every node
S = {i:0 for i in nodes}
P = {i:'' for i in nodes}
L = {i:5000 for i in nodes}

# define the source and terminal nodes
source = 'WA'
terminal = 'SL'

# start the algorithm

i = source
S[i] = 1
L[i] = 0

while True:
    print(i)
    for j,k in grid[i]:
        if L[j] > L[i]+k:
            L[j] = L[i]+k
            P[j] = i
       
    unvisited_nodes =  [node for node in S if S[node] == 0]
    min_L = unvisited_nodes[0]
    for node in unvisited_nodes:
        if L[node] < L[min_L]:
            min_L = node
    i = min_L
    S[i] = 1
    if i == terminal:
        break

# calculate final path and total distance
path = [terminal]
dist = 0        
while True:
    t = path[-1]
    t_next = P[t]
    dist += [k for j,k in grid[t_next] if j==t][0]
    path.append(t_next)
    if t_next == source:
        path.reverse()
        break

# print results
print('----------------------------------------------')
print('The shortest path between {} and {} is:'.format(source,terminal))
print()
print('-'.join(path))
print()
print('The total distance on this path is:')
print()
print(str(dist))
print('----------------------------------------------')






















