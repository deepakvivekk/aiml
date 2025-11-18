import numpy as np
np.random.seed(42)

# Data
cats    = np.random.randn(100,4) + [1,0,1,0]
dogs    = np.random.randn(100,4) + [4,2,3,1]
rabbits = np.random.randn(100,4) + [0,3,0,2]
X = np.vstack((cats, dogs, rabbits))
y = np.array([0]*100 + [1]*100 + [2]*100)

Y = np.zeros((300,3))
Y[np.arange(300), y] = 1

# Activations
relu = lambda x: np.maximum(0,x)
drelu = lambda x: (x > 0).astype(float)
softmax = lambda x: np.exp(x - x.max(1,keepdims=True)) / np.exp(x - x.max(1,keepdims=True)).sum(1,keepdims=True)
loss_fn = lambda y, p: -np.sum(y * np.log(p+1e-9)) / y.shape[0]

# Sizes
W1 = np.random.randn(4,8) * 0.01
b1 = np.zeros((1,8))
W2 = np.random.randn(8,6) * 0.01
b2 = np.zeros((1,6))
W3 = np.random.randn(6,3) * 0.01
b3 = np.zeros((1,3))

lr = 0.05
epochs = 600

# Training
for e in range(epochs):
    A1 = relu(X @ W1 + b1)
    A2 = relu(A1 @ W2 + b2)
    A3 = softmax(A2 @ W3 + b3)

    loss = loss_fn(Y, A3)
    m = X.shape[0]

    d3 = (A3 - Y) / m
    d2 = (d3 @ W3.T) * drelu(A2)
    d1 = (d2 @ W2.T) * drelu(A1)

    W3 -= lr * (A2.T @ d3)
    b3 -= lr * d3.sum(0,keepdims=True)
    W2 -= lr * (A1.T @ d2)
    b2 -= lr * d2.sum(0,keepdims=True)
    W1 -= lr * (X.T @ d1)
    b1 -= lr * d1.sum(0,keepdims=True)

    if (e+1) % 50 == 0:
        acc = (A3.argmax(1) == y).mean()*100
        print(f"Epoch {e+1}/{epochs} | Loss: {loss:.4f} | Acc: {acc:.2f}%")

# Prediction on new samples
X_test = np.array([
    [1.2, 0.2, 0.8, 0.1],
    [4.0, 2.5, 3.1, 1.0],
    [0.1, 3.2, 0.2, 2.1]
])

A1 = relu(X_test @ W1 + b1)
A2 = relu(A1 @ W2 + b2)
A3 = softmax(A2 @ W3 + b3)

labels = ["Cat","Dog","Rabbit"]
print("\nPredicted Class Labels:")
for i,p in enumerate(A3.argmax(1)):
    print(f"Sample {i+1}: {labels[p]}")
