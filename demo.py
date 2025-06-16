from sklearn import tree

X = [[282,80,40],[123,13,213,],[1231,321,3213],[12312,3,123],[1234,354,345],[56763,345,354],[435,345,345],[65,123,74]]
Y = ['male','male','male','male','female','female','male','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[1,2,3]])
print(prediction)