import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np


num_vertices = 9


adj = [[0 for i in range(num_vertices)] for j in range(num_vertices)]

#the shared vertex will be labeled as 8, connected to 6 and 7

for i in range(3):
    adj[2*i][2*i + 1] = 1
    adj[2*i + 1][2*i] = 1

adj[6][8] = 1
adj[7][8] = 1
adj[8][6] = 1
adj[8][7] = 1
#need E1-E2, E2-E3, E3-E4, E4-E1, and all of them to E5

def edgeT(ind1, ind2, eaeb):
    adj[ind1 + eaeb%2][ind2 + eaeb//2] ^=1
    adj[ind2 + eaeb//2][ind1 + eaeb%2] ^= 1


def DFS(marked, n, vert, start, count):
 
    # mark the vertex vert as visited
    marked[vert] = True
  
    # if the path of length (n-1) is found
    if n == 0: 
 
        # mark vert as un-visited to make
        # it usable again.
        marked[vert] = False
  
        # Check if vertex vert can end with
        # vertex start
        if adj[vert][start] == 1:
            count = count + 1
            return count
        else:
            return count
  
    # For searching every possible path of
    # length (n-1)
    for i in range(num_vertices):
        if marked[i] == False and adj[vert][i] == 1:
 
            # DFS for searching path by decreasing
            # length by 1
            count = DFS(marked, n-1, i, start, count)
  
    # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return count

def checkcyc(n):
    marked = [False for i in range(num_vertices)]

    count = 0
    for i in range(num_vertices-(n-1)):
        count = DFS(marked, n-1, i, i, count)

        marked[i] = True
        if count>0: return True
    return False

def edgeTFor3(e1, loopvar): #e1 is 0 indexed
    v1=0
    if loopvar<3:
        v1=e1*2
    else:
        v1=e1*2 + 1

    if loopvar%2 == 0:
        #connect to noly 8
        adj[v1][8]^=1
        adj[8][v1]^=1
    else:
        #connect to both 6 and 7
        adj[v1][6]^=1
        adj[v1][7]^=1
        adj[6][v1]^=1
        adj[7][v1]^=1



occurances = 0

for e1e2 in range(4):
    edgeT(0,2,e1e2)
    for (e1e3) in range(4):
        edgeT(0,4,e1e3)

        for e1e45 in range(4):
            edgeTFor3(0, e1e45)

            
            for e2e45 in range(4):
                edgeTFor3(1, e1e45)
                for e3e45 in range(4):
                    edgeTFor3(2, e1e45)
                    if not checkcyc(3) and not checkcyc(4) and not checkcyc(6):
                        print(adj)
                        # Create a graph from the adjacency matrix 
                        G = nx.from_numpy_array(np.array(adj))
                        
                        # Draw the graph 
                        pos = nx.spring_layout(G) 
                        nx.draw(G, pos, with_labels=True) 
                        plt.show() 
                        exit()
                    occurances+=1
                    edgeTFor3(2, e1e45)
                edgeTFor3(1, e1e45)
            edgeTFor3(0, e1e45)
        edgeT(0,4,e1e3)
    edgeT(0,2,e1e2)



print(occurances)

