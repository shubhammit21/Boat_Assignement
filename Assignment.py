# A Dynamic Programming based 
# solution to find min cost 
# to reach temple N-1 
# from station 0. 

INF = 2147483647   #(max value of infinity as integer)
N = 4

# This function returns the 
# smallest possible cost to 
# reach temple N-1 from A 0. 
def minCost(cost): 

	# dist[i] stores minimum 
	# cost to reach temple i 
	# from temple 0. 
	dist=[0 for i in range(N)] 
	for i in range(N): 
		dist[i] = INF 
	dist[0] = 0

	for i in range(N): 
		for j in range(i+1,N): 
			if (dist[j] > dist[i] + cost[i][j]): 
				dist[j] = dist[i] + cost[i][j] 

	return dist[N-1] 


# Driver program to 
# test above function 

cost= [ [0, 15, 80, 90], 
			[INF, 0, 40, 50], 
			[INF, INF, 0, 70], 
			[INF, INF, INF, 0]] 
			
print("The Minimum cost to reach temple ", 
		N," is ",minCost(cost)) 
