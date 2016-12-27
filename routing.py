import pickle
import collections

n_c = int(raw_input())
n_AP = int(raw_input())

def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'

clusters_r = pickle.load(open('clust_f.txt','rb'))
cluster_heads_r = pickle.load(open('clust_h_f.txt','rb'))
remaining_APs = pickle.load(open('remaining_APs.txt','rb'))

print 'Clusters::'
display(clusters_r)
print 'CHs'
display(cluster_heads_r)
print 'R.APs'
display(remaining_APs)
print '\n#####################\n'
routing_table = {}

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

temp_dict_r = collections.OrderedDict(sorted(temp_dict_r.items()))
temp_dict_h = collections.OrderedDict(sorted(temp_dict_h.items()))
temp_dict_AP = collections.OrderedDict(sorted(temp_dict_AP.items()))

display(temp_dict_r)
print '-----------'
display(temp_dict_h)
print '-----------'
display(temp_dict_AP)
print '-----------'

for u in range(n_AP):
	routing_dict = {}
	AP = 'AP'+str(u)
	if AP in temp_dict_AP:
		cl_no = temp_dict_AP[AP][3]
	else:	
		cl_no = temp_dict_r[AP][3]

	for j in temp_dict_r:
		if cl_no == None:
			routing_dict[j] = -1
		elif j == AP:
			routing_dict[j] = 0
		elif cl_no == temp_dict_r[j][3]:
			routing_dict[j]	= 1
		else:
			routing_dict[j] = -1

	for j in temp_dict_AP:
		routing_dict[j] = -1
	routing_dict[AP] = 0
	routing_table[AP] = collections.OrderedDict(sorted(routing_dict.items())) 

print 'Routing table'
display(collections.OrderedDict(sorted(routing_table.items())))

