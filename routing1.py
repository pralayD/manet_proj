import pickle
import collections

n_c = int(raw_input())
n_AP = int(raw_input())

def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print keys,'::',values
	    print'\n'

clusters_r = pickle.load(open('clust_f.txt','r'))
cluster_heads_r = pickle.load(open('clust_h_f.txt','r'))
remaining_APs = pickle.load(open('remaining_APs.txt','r'))
'''
display(clusters_r)
display(cluster_heads_r)
display(remaining_APs)
'''
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
routing_table = collections.OrderedDict()
for i in range(n_AP):
	routing_dict = collections.OrderedDict()
	node1 = 'AP'+str(i)
	if node1 in temp_dict_r:
		cl_no = temp_dict_r[node1][3]
	elif node1 in temp_dict_AP:
		cl_no = temp_dict_AP[node1][3]

	for j in range(n_AP):
		node2 = 'AP'+str(j)
		if node2 == node1:
			routing_dict[node2] = 0
		elif node2 in temp_dict_r:
			if cl_no == temp_dict_r[node2][3]:
				routing_dict[node2] = 1
			else:
				routing_dict[node2] = -1
		elif node2 in temp_dict_AP:
			routing_dict[node2] = -1 
	routing_table[node1] = routing_dict
print 'Routing Table'
display(routing_table)

print '::\nBuilding the Routing Matrix::\n'
route_matrix = open('route_matrix.txt','w+')
hops = []

for key in routing_table:
	for val in routing_table[key]:
		route_matrix.write(str(routing_table[key][val])+' ')
	route_matrix.write('\n')

route_matrix.close()
