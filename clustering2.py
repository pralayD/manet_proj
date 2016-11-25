'''----------------------------------------------
Creating clusters and distributing the APs.
-------------------------------------------------'''

import random
clusters = {} #Stores the APs of the clusters.
cluster_heads = {} # Dictionary with final CHs.
n_AP_clusters = {} # No. of APs in each cluster

n_c = int(raw_input('Enter the number of clusters:\n')) 

def nodes_in_cluster(n_c): #Creating random amount of APs for each cluster.
	for i in range(n_c):
		n_AP_clusters['c'+str(i)] = random.randint(5,15)


def pos_clust():
	for key in clusters:
		for val in clusters[key]:
			k_v = clusters[key][val]
			clusters[key][val] = random.randint(k_v-10,k_v+10)


def pos_AP():
	for key in m_AP_list:
		k = m_AP_list[key][0] 
		m_AP_list[key][0] = random.randint(k-10,k+10) 


def avg_calc(temp_list):
	total = 0
	for i in temp_list.keys():
		for j in temp_list.keys():
			temp = temp_list[i] - temp_list[j]
			total += temp
		avg_scan_list[i] = total / n
		total = 0
	print 'Average dBm level list::'
	print avg_scan_list
	print '\n'


def maxm_calc(temp_list):
	return max(temp_list,key = temp_list.get)
	

def mobility_node():
	n_m = 2#random.randint(1,5) #NUmber of nodes moving out of the network at a time.

	#m_AP_list = {} #List of APs moving out of a cluster.
	print 'A random cluster is chosen on which the mobility of a node will be shown.'
	print '\n'
	print 'A random node is chosen which will move out of the cluster.'

	#i = 0;
	for i in range(n_m):
		cl_no = random.randint(0,n_c-1) #Choosing a random cluster from which a node will move.
		m_AP = random.randint(0,1)#n_AP_clusters['c'+str(cl_no)]-1) # Choosing a random AP from the given cluster.

		

		#print 'A random cluster is chosen on which the mobility of a node will be shown.'
		print 'Selected Cluster number ::',cl_no
		print '\n'
		#print 'A random node is chosen which will move out of the cluster.'
		print 'Selected AP::',m_AP,'of cluster number',cl_no
		print '\n'

		#if not(clusters['Cluster '+str(cl_no)]['c'+str(cl_no)+'_'+AP+str(m_AP)]):
		if (clusters.get('Cluster '+str(cl_no),{}).has_key('c'+str(cl_no)+'_'+AP+str(m_AP))):
			'''print i,'i'
			i = i-1
			continue'''

			m_AP_list['c'+str(cl_no)+'_'+AP+str(m_AP)] = [clusters['Cluster '+str(cl_no)]['c'+str(cl_no)+'_'+AP+str(m_AP)]]

			del[clusters['Cluster '+str(cl_no)]['c'+str(cl_no)+'_'+AP+str(m_AP)]] #deleting the AP from the cluster.
			print 'AP deleted from the cluster list.\n'
			#print clusters
			n_AP_clusters['c'+str(cl_no)] = n_AP_clusters['c'+str(cl_no)] - 1; #Reducing the count of APs in the cluster.
			
		else:
			#i = i-1
			print 'Same AP. Already deleted.'
		

	for keys,values in clusters.items():
		    print(keys)
		    print(values)
	print '\n'
	print 'Number of APs in each cluster::\n',n_AP_clusters,'\n'
	print 'Mobile APs::',m_AP_list


def co_ordinates():
	for key in cluster_heads:
		cluster_heads[key].append(int(raw_input('X-cordinate:: ')))
		cluster_heads[key].append(int(raw_input('Y-cordinate:: ')))

	print 'Updated Cluster Heads\n', cluster_heads,'\n'


	for key in m_AP_list:
		m_AP_list[key].append(int(raw_input('Mobile AP--X-cordinate:: ')))
		m_AP_list[key].append(int(raw_input('Mobile AP--Y-cordinate:: ')))

	print '\nUpdated Mobile AP list::\n',m_AP_list,'\n'

	#Calculating the Euclidean Distance from the AP to all the CHs.

	min_d = 100 #Maximum distance calculated
	clust_h = '' #Inermediate variable for storing the resultant CH


	for i in m_AP_list:
		d_cluster_h[i] = []
		for j in cluster_heads:

			#d_cluster_h[str(i)+'-to-'+str(cluster_heads[j][0])]= 
			d_cluster_h[i].append(cluster_heads[j][0])
			distance = round((((m_AP_list[i][2] - cluster_heads[j][3])**2) + ((m_AP_list[i][1] - cluster_heads[j][2])**2)) ** (1/2.0),3)
			d_cluster_h[i].append(distance)
			
			if distance < min_d:
				min_d = distance
				clust_h = cluster_heads[j][0]
		min_dist_ch[i] = clust_h 
		min_d = 100

	print 'Minimum Distance calculated for each cluster ::'
	print d_cluster_h,'\n'

	print 'Cluster Heads in vicinity::\n', min_dist_ch,'\n'


def display(temp_list):
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'


nodes_in_cluster(n_c) #Driver function

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
		AP_list['c'+str(k)+'_'+AP+str(i)] = random.randint(-100,0)
	print 'The AP list::'
	print AP_list
	print '\n'
	clusters['Cluster '+str(k)] = dict(AP_list)

	#Finding the average of the dBm levels from each AP to the other.
	avg_scan_list = {}
	avg_calc(AP_list)

	#CLuster head on the basis of maximum of average dBm levels.
	
	c_h = maxm_calc(avg_scan_list)

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


'''----------------------------------------------
Mobility of the nodes.
-------------------------------------------------'''
m_AP_list = {} #List of APs moving out of a cluster.
mobility_node()


'''----------------------------------------------
Co-ordinates
-------------------------------------------------'''

#Assuming 4 Clusters
d_cluster_h = {} #Storing the Euclidean distances.
min_dist_ch = {} #stores the Minimum Distance calculated for each cluster 
co_ordinates()



'''----------------------------------------------
Appending to suitable clusters
-------------------------------------------------'''

for key in min_dist_ch:
	clusters['Cluster '+str(min_dist_ch[key][1])][key] = random.randint(-100,0)

print 'Mobile nodes appended to new cluster.'
display(clusters)
print '\n'























