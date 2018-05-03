from sklearn import tree
#https://www.youtube.com/watch?v=cKxRvEZd3Mw
#"smooth" = 1
#"bumpy" = 0
#and 0 for apple and 1 for orrange
# collect training data
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
labels = [0, 0, 1, 1]
# train classifire
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[160,0]])
#make predictions
