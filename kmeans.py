'''
k-means clustering
'''

from sklearn.cluster import KMeans
import numpy as np
import random

m = 0		# Declared for denoting the new APs.

clusters_AP = []	# List holding the co-ordinates of the APs.
clusters = {}		# Dictionary holding the APs with co-ordinates and the cluster no.
cluster_list = {}

def create_AP(n_AP):
	global m
	AP_list = {}	# Temporary dictionary holding the APs.
	for j in range(n_AP):
		AP_list['AP'+str(m)] = []
		m += 1
	return AP_list

def assign_coordinates(c,AP_list):
	c_h = random.choice(AP_list.keys())		
	''' Selecting any random AP for assignment of co-ordinates on the basis of which other
		co-ordinates are assigned.
	'''
	
	(AP_list[c_h]).append(int(raw_input('X-coordinate::')))
	(AP_list[c_h]).append(int(raw_input('Y-coordinate::')))
	
	x = AP_list[c_h][0]		# Taking out the X-value
	y = AP_list[c_h][1]		# Taking out the Y-value
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
	return kmeans


def create_AP_local(n_nodes):		# Function for the new APs.
	global m
	clust = {}
	for i in range(n_nodes):
		clust['AP'+str(m)] = map(int,raw_input().split())
		m += 1
	return clust

		
def predict_loc(clust,kmeans):		# Prediction of the co-ordinates for the new APs.
	temp = []
	for i in clust:
		temp.append(clust[i])

	pred = kmeans.predict(temp)
	print pred
	for i,j in zip(clust,pred):
		clust[i].append(j)
		clusters[i] = clust[i]

def assign_clusters(k):		# For preparing default cluster list.
	for i in range(k):
		cluster_list['Cluster '+str(i)] = None

	for i in cluster_list:
		temp = {}
		for j in clusters:
			if clusters[j][2] == int(i[8]):
				temp[j] = clusters[j]
		cluster_list[i] = dict(temp) 
	print '\n'
	display(cluster_list)



def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'

'''
Driver function
'''
k = int(raw_input('Enter the number of clusters::\n'))
#Initial Stage.

for i in range(k):
	n_AP = random.randint(2,5)
	AP_list = create_AP(n_AP)

	assign_coordinates(i,AP_list)


for i in clusters:
	clusters_AP.append([clusters[i][0],clusters[i][1]])

print '::AP List::'
print clusters,'\n'
print 'Co-ordinate List\n',clusters_AP

kmeans = k_means_algo(k)

# Final Stage.

n_nodes = int(raw_input('Enter the number of APs to be predicted::\n'))

clust = create_AP_local(n_nodes)

predict_loc(clust,kmeans)

print clusters

assign_clusters(k)


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