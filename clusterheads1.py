import random
clusters = {} #Stores the APs of the clusters.
cluster_heads = {} # Dictionary with final CHs.

n_c = int(raw_input('Enter the number of clusters:\n'))
for k in range(n_c):
	AP_list = {} #Dictionary containing the Access Points list.

	# 'n' denotes the no. of access points in the vicinity.
	n = int(raw_input("No. of access points in the cluster::\n"))
	
	#Creating the access points with random dBm levels.
	AP = "AP"
	for i in range(n):
		AP_list[AP+str(i)] = random.randint(-200,0)
	print 'The AP list::'
	print AP_list
	print '\n'
	clusters['Cluster '+str(k)] = dict(AP_list)

	#Finding the average of the dBm levels from each AP to the other.
	avg_scan_list = {}
	total = 0
	for i in AP_list.keys():
		for j in AP_list.keys():
			temp = AP_list[i] - AP_list[j]
			total += temp
		avg_scan_list[i] = total / n
		total = 0
	print 'Average dBm level list::'
	print avg_scan_list
	print '\n'

	#CLuster head on the basis of minimum of average dBm levels.
	c_h = min(avg_scan_list,key = avg_scan_list.get)
	print "Cluster head is:",c_h
	print '\n'
	cluster_heads['Cluster '+str(k)] = c_h

	AP_list.clear()
	avg_scan_list.clear()
	print '-------------------------------------------------------'

#Displaying the cluster heads and the APs in the clusters.
print 'Cluster Heads are::'
print cluster_heads
print 'Clusters::'
print clusters



