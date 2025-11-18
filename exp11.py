import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))
sigmoid_deriv = lambda x: x * (1 - x)

# Data
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Init
np.random.seed(42)
W1, b1 = np.random.rand(2,2), np.zeros((1,2))
W2, b2 = np.random.rand(2,1), np.zeros((1,1))

# Training
lr = 0.1
for e in range(10000):
    a1 = sigmoid(X @ W1 + b1)
    a2 = sigmoid(a1 @ W2 + b2)
    d2 = (y - a2) * sigmoid_deriv(a2)
    d1 = d2 @ W2.T * sigmoid_deriv(a1)

    W2 += a1.T @ d2 * lr
    b2 += d2.sum(0, keepdims=True) * lr
    W1 += X.T @ d1 * lr
    b1 += d1.sum(0, keepdims=True) * lr

    if e % 1000 == 0:
        print(f"Epoch {e}, Loss: {np.mean((y-a2)**2):.4f}")

print("\nFinal Predictions:\n", a2.round(3))
