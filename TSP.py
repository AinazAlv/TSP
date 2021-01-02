# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:14:28 2020

@author: iNaz
"""
#0.voooroodi az karbar
#1.tolid noqate random
#2.mohasebye faseleye har 2 noqte
#3.por kardane matris fasele
#4.tolid javabe random aval
#5.mohasebeye andazeye dor
#6.hamsayeha
#7.hillclimbing
#8.rasme noqat


import matplotlib.pyplot as plt
import numpy as np
import random

#Random solution
def random_sol(dis):
  
    nodes = list(range(len(dis)))
    
    solution = []

    for i in range(len(dis)):       
        rand_node = nodes[random.randint(0, len(nodes) - 1)]
        solution.append(rand_node)
        nodes.remove(rand_node)        
    print ( "Random first solution",solution)
    
    return solution

#Evaluation function
def get_h(dis, solution):
    routeLength = 0

    for i in range(len(solution)):
        
        if(i!=(len(solution)-1)):
            
            routeLength += dis[solution[i]][solution[i+1]]
            #print("t",solution[i],solution[i+1])
        elif(i == (len(solution)-1) ):
            routeLength += dis[solution[i]][solution[0]]
            #print("t",solution[i],solution[0])
            
    return routeLength

#Find neighbours
def swap(sol, pos1, pos2):
       
    sol[pos1], sol[pos2] = sol[pos2], sol[pos1] 
    return sol

def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
              
            neighbours.append(swap(neighbour, i, j))
            #print("neighbours=",neighbour)
   
    return neighbours

#Hillclimbing
    
def hillClimbing(dis):
    current_sol = random_sol(dis)
    current_h = get_h(dis, current_sol)
    neighbours = get_neighbours(current_sol)
    best_h_n = get_h(dis, neighbours[0])
    best_n = neighbours[0]
            
    while best_h_n < current_h:
        current_sol = best_n
        current_h = best_h_n
        neighbours = get_neighbours(current_sol)
        for neighbour in neighbours:
          current_h_n = get_h(dis, neighbour)
          if current_h_n < best_h_n:
              best_h_n = current_h
              best_n = neighbour
        
    return current_sol, current_h

#Input
dots=int(input("Input N:"))

#Creat n random coordinates
cords_set = set()
while len(cords_set) < dots:
    n=10
    x, y = random.randint(0, n - 1), random.randint(0, n - 1)    
    cords_set.add((x, y))
    
print("Random coordinates ",cords_set)
s = list(cords_set) 


#Euclidean distance
def distance(p1, p2):

    return round(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5)

dis=[] 
for i in range(len(s)): 
    col = [] 
    for j in range(len(s)): 
        col.append(distance(s[i],s[j])) 
    dis.append(col) 
    
print("Distance matrix\n",np.matrix(dis))

sol,length=hillClimbing(dis)

print("Best solution",sol,"\nTotal length",length)


#Plot
positions = np.array(s)
N=len(positions)

fig, ax = plt.subplots(2, sharex=True, sharey=True)         
ax[0].set_title('Nodes')
ax[1].set_title('Solution')
ax[0].scatter(positions[:, 0], positions[:, 1])             
ax[1].scatter(positions[:, 0], positions[:, 1])             


for i in range(len(sol)):
   
    if(i!=(len(sol)-1)):
        
        start_pos = positions[sol[i]]
        end_pos = positions[sol[i+1]]
        
    elif(i == (len(sol)-1) ):
        start_pos = positions[sol[i]]
        end_pos = positions[sol[0]]
        
    ax[1].annotate("", xy=start_pos, xycoords='data', xytext=end_pos, textcoords='data', arrowprops=dict(arrowstyle="<-",connectionstyle="arc3"))
    
    start_node = end_pos



##textbox
textstr = "Number of nodes: %d\nTotal length: %i" % (N, length)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax[1].text(0.05, 0.95, textstr, transform=ax[1].transAxes, fontsize=14, verticalalignment='top', bbox=props)

##padding
plt.tight_layout()

plt.show()

