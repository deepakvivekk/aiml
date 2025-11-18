import math 
import matplotlib.pyplot as plt 
points = { 
    "P1": (1, 3), 
    "P2": (2, 2), 
    "P3": (5, 8), 
    "P4": (8, 5), 
    "P5": (3, 9), 
    "P6": (10, 7), 
    "P7": (3, 3), 
    "P8": (9, 4), 
    "P9": (3, 7) 
} 
centroids = { 
    "C1": (2, 2.7), 
    "C2": (3.7, 8), 
    "C3": (9, 5.3) 
} 
 
def euclidean_distance(p1, p2): 
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) 
for pname, pcoords in points.items(): 
    print(f"Distances from {pname} {pcoords}:") 
    for cname, ccoords in centroids.items(): 
        dist = euclidean_distance(pcoords, ccoords) 
        print(f"  to {cname} {ccoords}: {dist:.2f}") 
print() 
plt.figure(figsize=(8,6)) 
for pname, (x, y) in points.items(): 
plt.scatter(x, y, c='blue', marker='o') 
plt.text(x+0.1, y+0.1, pname, fontsize=9, color='blue') 
for cname, (x, y) in centroids.items(): 
plt.scatter(x, y, c='red', marker='X', s=150) 
plt.text(x+0.1, y+0.1, cname, fontsize=11, color='red', weight='bold') 
plt.title("Data Points and Initial Centroids") 
plt.xlabel("X coordinate") 
plt.ylabel("Y coordinate") 
plt.grid(True) 
plt.show()
