'''
k-means clustering
'''

from sklearn.cluster import KMeans
import numpy as np
import random

m = 0

clusters_AP = []
clusters = {}

def create_AP(n_AP):
	global m
	AP_list = {}
	for j in range(n_AP):
		AP_list['AP'+str(m)] = []
		m += 1
	return AP_list

def assign_coordinates(c,AP_list):
	c_h = random.choice(AP_list.keys())
	
	(AP_list[c_h]).append(int(raw_input('X-coordinate::')))
	(AP_list[c_h]).append(int(raw_input('Y-coordinate::')))
	
	x = AP_list[c_h][0]
	y = AP_list[c_h][1]
	r = 3
	for i in AP_list:
		if i not in c_h:
			pos_AP = random.randint(1,8)
				#print pos_AP,'\n'
			if pos_AP == 1:
				(AP_list[i]).append(x-r)
				(AP_list[i]).append(y+r)
			elif pos_AP == 2:
				(AP_list[i]).append(x)
				(AP_list[i]).append(y+r)
			elif pos_AP == 3:
				(AP_list[i]).append(x+r)
				(AP_list[i]).append(y+r)
			elif pos_AP == 4:
				(AP_list[i]).append(x+r)
				(AP_list[i]).append(y)
			elif pos_AP == 5:
				(AP_list[i]).append(x+r)
				(AP_list[i]).append(y-r)
			elif pos_AP == 6:
				(AP_list[i]).append(x)
				(AP_list[i]).append(y-r)
			elif pos_AP == 7:
				(AP_list[i]).append(x-r)
				(AP_list[i]).append(y-r)
			elif pos_AP == 8:
				(AP_list[i]).append(x-r)
				(AP_list[i]).append(y)	

	for i in AP_list:
		clusters[i] = AP_list[i]

	print '::Set -- '+str(c)+'::\n'
	print AP_list,'\n'


def k_means_algo(k):
	X_Y = np.array(clusters_AP)
	kmeans = KMeans(n_clusters = k, random_state = 0).fit(X_Y)
	clust_no = kmeans.labels_
	print '\n','Cluster Numbers::',clust_no

	for i,j in zip(clusters,clust_no):
		clusters[i].append(j)

	print clusters
	#print kmeans.cluster_centers_


def find_clust(n_nodes):
	global m
	clust = {}
	for i in range(n_nodes):
		clust['AP'+str(m)] = map(int,raw_input().split())
		m += 1
	
	print clust 	
		

def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'

'''
Driver function
'''
k = int(raw_input('Enter the number of clusters::\n'))

for i in range(k):
	n_AP = random.randint(2,5)
	AP_list = create_AP(n_AP)

	assign_coordinates(i,AP_list)


for i in clusters:
	clusters_AP.append([clusters[i][0],clusters[i][1]])

print '::AP List::'
print clusters,'\n'
print 'Co-ordinate List\n',clusters_AP

k_means_algo(k)

display(clusters)

n_nodes = int(raw_input('Enter the number of APs to be predicted::\n'))

find_clust(n_nodes)


'''
X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
kmeans.labels_
#array([0, 0, 0, 1, 1, 1], dtype=int32)
kmeans.predict([[0, 0], [4, 4]])
#array([0, 1], dtype=int32)
kmeans.cluster_centers_
#array([[ 1.,  2.],[ 4.,  2.]])
'''