'''----------------------------------------------
Creating clusters and distributing the APs.
-------------------------------------------------'''

import random
import time
from threading import Thread
clusters = {} #Stores the APs of the clusters.
cluster_heads = {} # Dictionary with final CHs.
n_AP_clusters = {} # No. of APs in each cluster


n_c = int(raw_input('Enter the number of clusters:\n')) 

def nodes_in_cluster(n_c): #Creating random amount of APs for each cluster.
	for i in range(n_c):
		n_AP_clusters['c'+str(i)] = random.randint(5,15)


def avg_calc(temp_list):
	total = 0
	for i in temp_list.keys():
		for j in temp_list.keys():
			temp = temp_list[i][0] - temp_list[j][0]
			total += temp
		avg_scan_list[i] = total / n
		total = 0
	print 'Average dBm level list::'
	print avg_scan_list
	print '\n'


def maxm_calc(temp_list):
	return max(temp_list,key = temp_list.get)


def assign_coordinates():
	for key in clusters:
		x,y = cluster_heads[key][2], cluster_heads[key][3]
		for item in clusters[key]:
			clusters[key][item].append(random.randint(x-10,x+10))
			clusters[key][item].append(random.randint(y-10,y+10))


def display(temp_list):
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'


def change_coordinates(i):
	while(i):
		for key in clusters:
			for val in clusters[key]:
				x,y,z = clusters[key][val][1],clusters[key][val][2],clusters[key][val][0]
				
				clusters[key][val][0] = random.randint(z-5,z+5)  #dBm Value
				clusters[key][val][1] = random.randint(x-10,x+10)  # X-coordinate
				clusters[key][val][2] = random.randint(y-10,y+10)  # Y-coordinate

				if val in cluster_heads[key][0]:
					cluster_heads[key][1] = clusters[key][val][0]
					cluster_heads[key][2] = clusters[key][val][1]
					cluster_heads[key][3] = clusters[key][val][2]
		
		#i -= 1
		print '::Executed Thread 1::','\n'
		display(clusters)
		display(cluster_heads)
		time.sleep(3)


def assign_cluster(x,y,radius,key,val):
	distance_CH = {}

	for key in cluster_heads:
		x_c,y_c = cluster_heads[key][2], cluster_heads[key][3]

		distance_CH[cluster_heads[key][0]] = round((((x - x_c) ** 2) + ((y - y_c) ** 2)) ** (1/2.0),3)

	elected_CH = min(distance_CH,key = distance_CH.get)
	print 'Min. distance CH',elected_CH
	cluster_no = elected_CH[1]
	print 'cluster no.',cluster_no,'\n'
	print'-------'
	print distance_CH

	if distance_CH[elected_CH] <= radius:
		clusters['Cluster '+ str(cluster_no)][val] = clusters[key][val]
		del clusters[key][val]
		print 'temporary dict.--------------'
		print clusters
		#clusters = temp_dict
		print 'Deleted from the respective cluster.\n'	


def check_mobility(j):
	radius = 12
	#time.sleep(2)
	while(j):
		for key in clusters:
			for val in clusters[key]:
				if val is not cluster_heads[key][0]:
					x,y = clusters[key][val][1],clusters[key][val][2]

					'''				
					Checking whether an AP is within the radius or not.
					'''

					x_c,y_c = cluster_heads[key][2],cluster_heads[key][3]
					distance = round((((x - x_c) ** 2) + ((y - y_c) ** 2)) ** (1/2.0),3)
					print val,distance
					if  distance > radius:
						'''
						Call the function to assign a new cluster.
						'''
						print val,'of',key,'is not in range.\n'
						print 'Calling function ...\n'
						assign_cluster(x,y,radius,key,val)
		#time.sleep(3)
		j -= 2
		print '::Executed Thread 2::','\n\n'
		display(clusters)



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
		AP_list['c'+str(k)+'_'+AP+str(i)] = [random.randint(-100,0)]
	print 'The AP list::'
	print AP_list
	print '\n'
	clusters['Cluster '+str(k)] = dict(AP_list)

	#Finding the average of the dBm levels from each AP to the other.
	avg_scan_list = {}
	avg_calc(AP_list)  #Average Calculation'''

	#CLuster head on the basis of maximum of average dBm levels.
	
	c_h = maxm_calc(avg_scan_list)  #Maximum Calculation'''

	cluster_heads['Cluster '+str(k)] = [c_h]
	cluster_heads['Cluster '+str(k)].append(AP_list[c_h])

	AP_list.clear()
	avg_scan_list.clear()
	print '-------------------------------------------------------'

#Displaying the cluster heads and the APs in the clusters.
print 'Cluster Heads are::'
#print cluster_heads
display(cluster_heads)

print 'Clusters::'
#print clusters
display(clusters)

for key in cluster_heads:
		cluster_heads[key].append(int(raw_input('X-cordinate:: ')))
		cluster_heads[key].append(int(raw_input('Y-cordinate:: ')))

display(cluster_heads)

assign_coordinates()   #'''Assigning the co-ordinates to each AP w.r.t to the CH'''

print '\n\n'
display(clusters)

'''--------------------------------------------------------------------'''
'''--------------------------------------------------------------------'''

#Thread(target=change_coordinates,args=(2,)).start()
Thread(target=check_mobility,args=(2,)).start()
#change_coordinates(1)








