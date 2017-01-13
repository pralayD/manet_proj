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
cluster_heads_detected = pickle.load(open('clust_h_d.txt','r'))

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
				#print 'count1 and count',count1, count
				rec_call = find_host(item,CH_y)

				if rec_call == False:
					count = count1
					#continue
				elif rec_call == True:
					hop_count.append(count)
					count = count1
					#continue
				elif isinstance(rec_call,int):
					hop_count.append(rec_call)
					count = count1
					#continue
				elif rec_call == '#':
					count = count1
					#continue

		visited.remove(CH_x)
		if len(hop_count):
			return min(hop_count)			
		else:
			return '#'


display(clusters_r)
display(cluster_heads_r)
display(remaining_APs)

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
	#print 'node1',node1
	if node1 in temp_dict_r:
		cl_no = temp_dict_r[node1][3]
	elif node1 in temp_dict_AP:
		cl_no = temp_dict_AP[node1][3]
	#print node1,cl_no
	for j in range(n_AP):
		node2 = 'AP'+str(j)
		#print 'node2',node2
		if node2 == node1:
			routing_dict[node2] = 0 
			#continue

		elif node2 in temp_dict_AP or node1 in temp_dict_AP:
			routing_dict[node2] = -1 

		else:
		#elif node2 in temp_dict_r:
			if cl_no == temp_dict_r[node2][3]:
				routing_dict[node2] = 1
			else:
				for key in temp_dict_h:
					if temp_dict_h[key][3] == temp_dict_r[node2][3]:
						CH_y = key
					if temp_dict_h[key][3] == cl_no:
						CH_x = key

				#print 'CH_x',CH_x,'CH_y',CH_y				
				hops = find_host(CH_x,CH_y)
				count = 0
				if hops == True:
					hops = 0
				#print 'Hops',hops,node1,node2
				if isinstance(hops,int):
					#hops += 2
					routing_dict[node2] = hops
				else:
					#print 'Not found::',node2
					routing_dict[node2] = -1
				print '\n'
		
		#print 'value',routing_dict[node2]
		#dummy = raw_input()			
		
	routing_table[node1] = routing_dict
print 'Routing Table'
display(routing_table)

print '::\nBuilding the Routing Matrix::\n'
route_matrix = open('route_matrix.txt','w+')
#hops = []

for key in routing_table:
	for val in routing_table[key]:
		route_matrix.write(str(routing_table[key][val])+' ')
	route_matrix.write('\n')

route_matrix.close()
print 'Detected CHS..'
display(cluster_heads_detected)