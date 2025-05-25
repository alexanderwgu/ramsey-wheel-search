import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np





adj = [[0 for i in range(10)] for j in range(10)]

for i in range(5):
    adj[2*i][2*i + 1] = 1
    adj[2*i + 1][2*i] = 1
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
    for i in range(10):
        if marked[i] == False and adj[vert][i] == 1:
 
            # DFS for searching path by decreasing
            # length by 1
            count = DFS(marked, n-1, i, start, count)
  
    # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return count

def checkcyc(n):
    marked = [False for i in range(10)]

    count = 0
    for i in range(10-(n-1)):
        count = DFS(marked, n-1, i, i, count)

        marked[i] = True
        if count>0: return True
    return False


occurances = 0
for e1e2 in range(4):
    edgeT(0,2,e1e2)
    for e2e3 in range(4):
        edgeT(2, 4, e2e3)
        for e3e4 in range(4):
            edgeT(4,6,e3e4)
            for e4e1 in range(4):
                edgeT(6,0, e4e1)

                for e5e1 in range(4):
                    edgeT(8,0,e5e1)
                    for e5e2 in range(4):
                        edgeT(8,2,e5e2)
                        for e5e3 in range(4):
                            edgeT(8,4,e5e3)
                            for e5e4 in range(4):
                                edgeT(8,6,e5e4)
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
                                



                                #now check for cycles
                                edgeT(8,6,e5e4)
                            edgeT(8,4,e5e3)
                        edgeT(8,2,e5e2)
                    edgeT(8,0,e5e1)
                edgeT(6,0, e4e1)
            edgeT(4,6,e3e4)
        edgeT(2, 4, e2e3)
    edgeT(0,2,e1e2)



print(occurances)
