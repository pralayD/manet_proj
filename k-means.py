'''k-means clustering
'''
from sklearn.cluster import KMeans
import numpy as np
import random

clusters = {}

def create_AP(n_AP,i):
	AP_list = {}
	for j in range(n_AP):
		AP_list['c'+str(i)+'_AP'+str(j)] = []
	return AP_list

def assign_coordinates(AP_list):
	c_h = random.choice(AP_list.keys())
	
	AP_list[c_h].append(int(raw_input('X-coordinate::')))
	AP_list[c_h].append(int(raw_input('Y-coordinate::')))
	print AP_list
	x = AP_list[c_h][0]
	y = AP_list[c_h][1]
	r = 5
	for i in AP_list:
		if i not in c_h:
			pos_AP = random.randint(1,8)
				#print pos_AP,'\n'
				if pos_AP == 1:
					AP_list.append(x-r)
					AP_list.append(y+r)
				elif pos_AP == 2:
					AP_list.append(x)
					AP_list.append(y+r)
				elif pos_AP == 3:
					AP_list.append(x+r)
					AP_list.append(y+r)
				elif pos_AP == 4:
					AP_list.append(x+r)
					AP_list.append(y)
				elif pos_AP == 5:
					AP_list.append(x+r)
					AP_list.append(y-r)
				elif pos_AP == 6:
					AP_list.append(x)
					AP_list.append(y-r)
				elif pos_AP == 7:
					AP_list.append(x-r)
					AP_list.append(y-r)
				elif pos_AP == 8:
					AP_list.append(x-r)
					AP_list.append(y)



def display(temp_list):		# Display the items in the passed Dictionaries.
	for keys,values in temp_list.items():
	    print(keys)
	    print(values)
	    print'\n'


n_clusters = int(raw_input('Enter the number of clusters::\n'))
for i in range(n_clusters):
	n_AP = random.randint(1,5)
	AP_list = create_AP(n_AP,i)

	assign_coordinates(AP_list)

#display(clusters)
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