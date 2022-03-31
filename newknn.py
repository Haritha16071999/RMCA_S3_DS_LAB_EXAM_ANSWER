from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


iris= load_iris()
x= iris.data
y= iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
print("prediction:",y_pred)
print("accuracy:" ,accuracy_score(y_test,y_pred))

