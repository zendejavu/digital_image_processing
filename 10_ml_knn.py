#machine learning knn

from sklearn import datasets  # import dataset bunga iris 
from sklearn.neighbors import KNeighborsClassifier

labels = ['Setosa', 'VersiColor', 'Virginica']

iris = datasets.load_iris() #150 data set bunga iris
X = iris.data # p dan L kelopak, P dan L putik
Y = iris.target # sepesies / jenis bungan iris

#tarining KNN
knn = KNeighborsClassifier()
knn.fit(X,Y)  # membangun model

#test
predict = knn.predict([[5.1, 3.5, 1.5, 0.2]])
print(labels[predict[0]])
