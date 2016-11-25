'''Created APs, Assigned clusters, Elected the CHs, T1 : checking for the nodes within range, T2: Changing the co-ordinates and updating the
CHs
'''
	
'''----------------------------------------------
Creating clusters and distributing the APs.
-------------------------------------------------'''

import random
import time
from threading import Thread
clusters = {} #Stores the APs of the clusters.
cluster_heads = {} # Dictionary with final CHs.
n_AP_clusters = {} # No. of APs in each cluster.
not_assigned = {} # Mobile nodes not assigned to any cluster.
avg_scan_list = {} #Finding the average of the dBm levels from each AP to the other.

n_c = int(raw_input('Enter the number of clusters:\n')) 

def nodes_in_cluster(n_c): #Creating random amount of APs for each cluster.
	for i in range(n_c):
		n_AP_clusters['c'+str(i)] = random.randint(2,6)


def avg_calc(temp_list):
	total = 0
	n = len(temp_list.keys())
	for i in temp_list.keys():
		for j in temp_list.keys():
			temp = temp_list[i][0] - temp_list[j][0]
			total += temp
		avg_scan_list[i] = total / n
		total = 0
	#print 'Average dBm level list::'
	#print avg_scan_list
	print '\n'


def maxm_calc(temp_list):
	return max(temp_list,key = temp_list.get)


def find_CH(AP_list,k):
	print 'AP list','\n',AP_list
	avg_calc(AP_list)  #Average Calculation
	#CLuster head on the basis of maximum of average dBm levels.
	c_h = {}
	c_h[maxm_calc(avg_scan_list)] = AP_list[maxm_calc(avg_scan_list)]
	cluster_heads['Cluster '+str(k)] = dict(c_h)
	print 'Done'
	print 'CH\n',cluster_heads
	avg_scan_list.clear()
	c_h.clear()

	

def assign_coordinates():
	for key in clusters:
		temp1,temp2 = cluster_heads[key].keys()[0], cluster_heads[key].keys()[0]
		x,y = cluster_heads[key][temp1][1], cluster_heads[key][temp2][1]
		for item in clusters[key]:
			if item not in cluster_heads[key]:
				clusters[key][item].append(random.randint(x-8,x+8))
				clusters[key][item].append(random.randint(y-8,y+8))
				clusters[key][item].append(int(key[8]))


def display(temp_list):
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'


def change_coordinates(i):
	cluster_heads.clear()
	while(i):
		for key in clusters:
			for val in clusters[key]:
				x,y,z = clusters[key][val][1],clusters[key][val][2],clusters[key][val][0]
				
				clusters[key][val][0] = random.randint(z-15,z+15)  #dBm Value
				clusters[key][val][1] = random.randint(x-10,x+10)  # X-coordinate
				clusters[key][val][2] = random.randint(y-10,y+10)  # Y-coordinate
				
				if val in not_assigned:
					not_assigned[val][0] = clusters[key][val][0]
					not_assigned[val][1] = clusters[key][val][1]
					not_assigned[val][2] = clusters[key][val][2]

		for key in clusters:
			print 'keys::\n',clusters[key]
			find_CH(clusters[key],key[8])
		print 'New Cluster Heads assigned...\n'
		
		#i -= 2
		
		display(clusters)
		print '\n'
		display(cluster_heads)
		print '::Executed Thread 1::','\n'
		time.sleep(10)


def assign_cluster_not_assigned(mobile_nodes,distance_CH):
	radius = 10
	print "Reached successfully..."
	for key in distance_CH:
		if distance_CH[key][1] <= radius:
			clusters['Cluster '+ str(distance_CH[key][0][1])][key] = mobile_nodes[key]
			clusters['Cluster '+ str(distance_CH[key][0][1])][key][3] = int(distance_CH[key][0][1])
			print 'Found a new cluster for the AP'
			print 'Cluster list updated.\n'
			del not_assigned[key]
	print 'Updated not_assigned list\n'
	print not_assigned
	return None

def assign_cluster(mobile_nodes,distance_CH):
	print '\n',distance_CH
	radius = 10

	for key in distance_CH:
		if distance_CH[key][1] <= radius:

			del clusters['Cluster '+ str(distance_CH[key][2])][key]
			print key,' Deleted from the respective cluster.\n'	

			clusters['Cluster '+ str(distance_CH[key][0][1])][key] = mobile_nodes[key]
			print key,' Appended to the respective cluster.\n'
			clusters['Cluster '+ str(distance_CH[key][0][1])][key][3] = int(distance_CH[key][0][1])

			if key in not_assigned:
				del not_assigned[key]
		else:
			not_assigned[key] = clusters['Cluster '+ str(distance_CH[key][2])][key]

	print 'Executing for the remaining nodes.\n'
	for key in not_assigned:
		if key in clusters['Cluster '+ str(not_assigned[key][3])]:
			del clusters['Cluster '+ str(not_assigned[key][3])][key]
			print 'Deleted from the clusters.'

	print '\n\n',display(clusters)

	print '::Remaining APs::\n'
	print '\n',not_assigned,'\n'
	return
	

def find_cluster(mobile_nodes,radius,flag):

	distance_CH = {}
	temp_dict = {}
	for key1 in mobile_nodes:
		for key in cluster_heads:
			x_c,y_c = cluster_heads[key][cluster_heads[key].keys()[0]][1], cluster_heads[key][cluster_heads[key].keys()[0]][2]
			x,y = mobile_nodes[key1][1], mobile_nodes[key1][2]

			temp_dict[cluster_heads[key].keys()[0]] = round((((x - x_c) ** 2) + ((y - y_c) ** 2)) ** (1/2.0),3)
		
		nearest_CH = min(temp_dict,key = temp_dict.get)
		distance = temp_dict[nearest_CH]
		distance_CH[key1] = [nearest_CH,distance,mobile_nodes[key1][3]]
	if flag == 0:
		assign_cluster(mobile_nodes,distance_CH)
	else:
		assign_cluster_not_assigned(mobile_nodes,distance_CH)
	return 


def check_mobility(j):
	radius = 10
	mobile_nodes = {}

	while(j):
		if len(not_assigned.keys()):
			print 'Calling for Remaining APs::\n'
			find_cluster(not_assigned,radius, 1)
			print '-------------------------Done for not_assigned'
			print 'not_assigned::\n',not_assigned

		for key in clusters:
			for val in clusters[key]:
				if val not in cluster_heads[key]:
					x,y = clusters[key][val][1],clusters[key][val][2]

					'''				
					Checking whether an AP is within the radius or not.
					'''
					#temp_x_c , temp_y_c = ,
					x_c,y_c = cluster_heads[key][cluster_heads[key].keys()[0]][1],cluster_heads[key][cluster_heads[key].keys()[0]][2]
					distance = round((((x - x_c) ** 2) + ((y - y_c) ** 2)) ** (1/2.0),3)
					print val,distance
					if  distance > radius:
						'''
						Call the function to assign a new cluster.
						'''
						mobile_nodes[val] = [clusters[key][val][0],clusters[key][val][1],clusters[key][val][2],clusters[key][val][3]]
						print val,'of',key,'is not in range.\n'
		
		print 'Calling function ...\n'
		print 'Mobile Nodes\n',mobile_nodes
		find_cluster(mobile_nodes,radius,0)			
		
		#j -= 1
		print '::Executed Thread 2::','\n\n'
		mobile_nodes.clear()
		time.sleep(6)
		#display(clusters)



'''--------------------------------------------------------------------
Driver function 
--------------------------------------------------------------------'''

nodes_in_cluster(n_c)   #No. of nodes in clusters.

print 'Each clusters with their respective number of APs::'
print n_AP_clusters
print '\n'
print '----------------------------------------------------------'
for k in range(n_c):
	print 'Cluster::',k
	print '\n'
	AP_list = {} #Dictionary containing the Access Points list.

	# 'n' denotes the no. of access points in the vicinity.
	n = n_AP_clusters['c'+str(k)] #int(raw_input("No. of access points in the cluster::\n"))
	
	#Creating the access points with random dBm levels.
	AP = "AP"
	for i in range(n):
		AP_list['c'+str(k)+'_'+AP+str(i)] = [random.randint(-100,-50)]
	print 'The AP list::'
	print AP_list
	print '\n'
	clusters['Cluster '+str(k)] = dict(AP_list)

	find_CH(AP_list,k)
		
	AP_list.clear()
	
	print '-------------------------------------------------------'

#Displaying the cluster heads and the APs in the clusters.
print 'Cluster Heads are::'
#print cluster_heads
display(cluster_heads)

print 'Clusters::'
#print clusters
display(clusters)

for key in cluster_heads:
	for item in cluster_heads[key]:
		cluster_heads[key][item].append(int(raw_input('X-cordinate:: ')))
		cluster_heads[key][item].append(int(raw_input('Y-cordinate:: ')))
		cluster_heads[key][item].append(int(key[8]))
display(cluster_heads)

assign_coordinates()   #'''Assigning the co-ordinates to each AP w.r.t to the CH'''

print '\n'
display(clusters)

'''--------------------------------------------------------------------'''
'''--------------------------------------------------------------------'''
print 'Thread starts...\n'
Thread(target=check_mobility,args=(2,)).start()
time.sleep(5)
Thread(target=change_coordinates,args=(4,)).start()



#print 'not assigned\n',not_assigned








