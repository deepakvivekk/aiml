from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score 
# Load dataset 
iris = load_iris() 
X = iris.data 
y = iris.target 
# Split into train and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
# Create Naive Bayes model 
model = GaussianNB() 
# Train the model 
model.fit(X_train, y_train) 
# Predict on test data 
y_pred = model.predict(X_test) 
# Accuracy 
print("Accuracy:", accuracy_score(y_test, y_pred))