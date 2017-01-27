import pickle
import collections

n_c = int(raw_input()) # No. of clusters
n_AP = int(raw_input()) # No. of APs throughout the network.

def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print keys,'::',values
	    print'\n'

'''
Reading the files : 1. Clusters file  2. Cluster Heads file  3. Files containing the APs not a part of any cluster. 
					 4. Cluster Heads in the vicinity of other Cluster Heads.
'''

clusters_r = pickle.load(open('clust_f.txt','r')) 
cluster_heads_r = pickle.load(open('clust_h_f.txt','r'))
remaining_APs = pickle.load(open('remaining_APs.txt','r'))
cluster_heads_detected = pickle.load(open('clust_h_d.txt','r'))



# Function to find the hop counts for Inter-Cluster Routing.


count = 0
visited = []
def find_host(CH_x,CH_y):
	global count
	visited.append(CH_x)
	li = cluster_heads_detected[CH_x]

	if len(li) == 0:
		visited.remove(CH_x)
		return False

	if CH_y in li:
		count += 1
		visited.remove(CH_x)
		return True

	if all(x in visited for x in li):
		visited.remove(CH_x)
		return False
	else:
		count += 1
		for item in li:
			if item not in visited:
				hop_count = [] 
				count1 = count
				rec_call = find_host(item,CH_y)

				if rec_call == False:
					count = count1
					
				elif rec_call == True:
					hop_count.append(count)
					count = count1
					
				elif isinstance(rec_call,int):
					hop_count.append(rec_call)
					count = count1
					
				elif rec_call == '#':
					count = count1
					

		visited.remove(CH_x)
		if len(hop_count):
			return min(hop_count)			
		else:
			return '#'



# Displaying all the files read.


print 'Clusters::'
display(clusters_r)
print 'Cluster Heads::'
display(cluster_heads_r)
print 'Not reachable APs::'
display(remaining_APs)



# Merging all the cluster files into a single file respectively.


temp_dict_r = {}
temp_dict_h = {}
temp_dict_AP = {}


for u in clusters_r:
	for v in clusters_r[u]:
		temp_dict_r[v] = clusters_r[u][v]

for u in cluster_heads_r:
	for v in cluster_heads_r[u]:
		temp_dict_h[v] = cluster_heads_r[u][v]

for u in remaining_APs:
	temp_dict_AP[u] = remaining_APs[u]
'''
display(temp_dict_r)
print '-----------'
display(temp_dict_h)
print '-----------'
display(temp_dict_AP)
print '-------'
'''


# Creating the Distance Matrix.


routing_table = collections.OrderedDict()
for i in range(1,n_AP+1):
	routing_dict = collections.OrderedDict()
	node1 = 'AP'+str(i)

	if node1 in temp_dict_r:
		cl_no = temp_dict_r[node1][3]
	elif node1 in temp_dict_AP:
		cl_no = temp_dict_AP[node1][3]
	
	for j in range(1,n_AP+1):


		# For Intra-Cluster


		node2 = 'AP'+str(j)
		if node2 == node1:
			routing_dict[node2] = 0 
			
		elif node2 in temp_dict_AP or node1 in temp_dict_AP:
			routing_dict[node2] = -1 

		else:
			if cl_no == temp_dict_r[node2][3] and (node2 in temp_dict_h or node1 in temp_dict_h):
				routing_dict[node2] = 1
			elif cl_no == temp_dict_r[node2][3]:

				
				#if distance from node1 to its CH is greater than the distance from node1 to node2.
				

				x1 = temp_dict_r[node1][1]
				y1 = temp_dict_r[node1][2]
				x2 = temp_dict_r[node2][1]
				y2 = temp_dict_r[node2][2]

				for key in temp_dict_h:
					if temp_dict_h[key][3] == temp_dict_r[node1][3]:
						x_c = temp_dict_h[key][1]
						y_c = temp_dict_h[key][2]
				dist1 = round((((x1 - x_c) ** 2) + ((y1 - y_c) ** 2)) ** (1/2.0),3)
				dist2 = round((((x2 - x_c) ** 2) + ((y2 - y_c) ** 2)) ** (1/2.0),3)
				dist3 = round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2.0),3)

				if dist3 < (dist1 + dist2):
					routing_dict[node2] = 1
				else:
					routing_dict[node2] = 2


		#For Inter-Cluster


			else:
				for key in temp_dict_h:
					if temp_dict_h[key][3] == temp_dict_r[node2][3]:
						CH_y = key
					if temp_dict_h[key][3] == cl_no:
						CH_x = key

				hops = find_host(CH_x,CH_y)

				count = 0
				if hops == True:
					if node1 == CH_x and node2 == CH_y:
						hops = 1
						routing_dict[node2] = hops
					elif node2 == CH_y or node1 == CH_x:
						hops = 2
						routing_dict[node2] = hops
					else:
						hops = 3
						routing_dict[node2] = hops

				elif hops == False:
					routing_dict[node2] = -1

				elif isinstance(hops,int):
					if node1 == CH_x and node2 == CH_y:
						routing_dict[node2] = hops
					elif (node1 == CH_x and node2 != CH_y) or (node1 != CH_x and node2 == CH_y):
						routing_dict[node2] = hops + 1
					else:
						routing_dict[node2] = hops + 2

				else:
					routing_dict[node2] = -1	
		
	routing_table[node1] = routing_dict



# Displaying the Distance Matrix calculated.


print 'Routing Table'
display(routing_table)

print 'Detected CHS..'
display(cluster_heads_detected)


print '\nRouting Matrix dumped !\n'
route_matrix = open('route_matrix.txt','w+')


#Dumping the Distance Matrix


for key in routing_table:
	count = 0
	for val in routing_table[key]:
		if count < n_AP - 1:
			route_matrix.write(str(routing_table[key][val])+' ')
		else:
			route_matrix.write(str(routing_table[key][val]))
		count += 1			
	route_matrix.write('\n')

route_matrix.close()
