import random
AP_list = {} #Dictionary containing the Access Points list.
n = int(raw_input("No. of access points in the network::\n"))
# 'n' denotes the no. of access points in the vicinity.

#Creating the access points with random dBm levels.
AP = "AP"
for i in range(n):
	AP_list[AP+str(i)] = random.randint(-100,0)

print AP_list

#Finding the average of the dBm levels from each AP to the other.
record = []
avg_scan_list = {}
total = 0
for i in AP_list.keys():
	for j in AP_list.keys():
		temp = AP_list[i] - AP_list[j]
		total += temp
	avg_scan_list[i] = total / n
	total = 0

print avg_scan_list

#CLuster head on the basis of minimum of average dBm levels.
cluster_head = min(avg_scan_list,key = avg_scan_list.get)
print "cluster head is:",cluster_head






