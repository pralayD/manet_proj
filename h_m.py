import pickle
import collections

with open('inputs.txt') as f:
	for x in f:
		n_c,n_AP = map(int,x.split(' '))
	

clusters_r = pickle.load(open('clust_f.txt','r')) 
cluster_heads_r = pickle.load(open('clust_h_f.txt','r'))
remaining_APs = pickle.load(open('remaining_APs.txt','r'))
cluster_heads_detected = pickle.load(open('clust_h_d.txt','r'))

def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print keys,'::',values
	    print'\n'

def display_matrix():
	global Matrix
	for i in Matrix:
		print i

w,h = n_AP,n_AP
Matrix = [[0 if x == y else -1 for x in range(w)] for y in range(h)]
#print Matrix

#display(clusters_r)
display(cluster_heads_detected)
#display(cluster_heads_r)

heads = []
head_AP = {}

for item in cluster_heads_r:
	heads.append(cluster_heads_r[item].keys()[0])

for item in cluster_heads_r:
	head_AP[cluster_heads_r[item].keys()[0]] = clusters_r[item].keys()

for item in heads:
	head_AP[item].remove(item)

display(head_AP)

visited = []

for c_h in heads:
	x = int(c_h.split("AP")[1])
	for node in cluster_heads_detected[c_h]:
		y = int(node.split("AP")[1])
		Matrix[x-1][y-1] = 1

	for node in head_AP[c_h]:
		y = int(node.split("AP")[1])
		Matrix[x-1][y-1] = 1
		Matrix[y-1][x-1] = 1

	

print '\nRouting Matrix dumped !\n'
distance_matrix = open('distance_matrix.txt','w+')

for row in Matrix:
	count = 0
	for entry in row:
		if count < n_AP - 1:
			distance_matrix.write(str(entry)+' ')
		else:
			distance_matrix.write(str(entry))
		count += 1			
	distance_matrix.write('\n')
distance_matrix.close()
#display_matrix()