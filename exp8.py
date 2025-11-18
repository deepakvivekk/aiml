import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X = np.array([[1,2],[2,3],[3,3],[6,1],[7,2],[6,5],[7,7],[8,6],[7,5],[6,6]])
y = np.array([0,0,0,0,0,1,1,1,1,1])

clf = SVC(kernel='linear').fit(X, y)

xx, yy = np.meshgrid(
    np.linspace(X[:,0].min()-1, X[:,0].max()+1, 500),
    np.linspace(X[:,1].min()-1, X[:,1].max()+1, 500)
)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(*X[y==0].T, c='blue', label='Group 0')
plt.scatter(*X[y==1].T, c='red', label='Group 1')
plt.scatter(*clf.support_vectors_.T, s=100, facecolors='none', edgecolors='k', label='Support Vectors')
plt.xlabel('Feature 1'); plt.ylabel('Feature 2')
plt.title('SVM: Separating Two Groups with a Decision Boundary')
plt.legend(); plt.show()
