import math
import matplotlib.pyplot as plt

dataset = [
    [1.2, 8.5],
    [2.1, 7.9],
    [1.8, 9.1],
    [2.5, 8.3],
    [1.5, 7.4],
    [3.1, 9.0],
    [2.0, 8.8],
    [1.9, 7.6],
    [7.5, 2.3],
    [8.2, 1.8],
    [7.8, 3.1],
    [9.0, 2.5],
    [8.5, 1.5],
    [7.2, 2.8],
    [8.8, 3.3],
    [9.1, 1.9],
]

k = 2

centroid1 = [dataset[0][0], dataset[0][1]]
centroid2 = [dataset[8][0], dataset[8][1]]  # pick one from each natural group

print(f"Initial centroids:")
print(f"  Centroid 1: {centroid1}")
print(f"  Centroid 2: {centroid2}")

for iteration in range(10):
    print(f"\n── Iteration {iteration + 1} ──")

    assignments = []

    for row in dataset:
        x = row[0]
        y = row[1]

        dist_to_c1 = math.sqrt((x - centroid1[0])**2 + (y - centroid1[1])**2)
        dist_to_c2 = math.sqrt((x - centroid2[0])**2 + (y - centroid2[1])**2)

        if dist_to_c1 < dist_to_c2:
            assignments.append(1)
            print(f"  ({x}, {y})  →  Cluster 1  (d1={dist_to_c1:.2f}, d2={dist_to_c2:.2f})")
        else:
            assignments.append(2)
            print(f"  ({x}, {y})  →  Cluster 2  (d1={dist_to_c1:.2f}, d2={dist_to_c2:.2f})")

    cluster1_points = []
    cluster2_points = []

    for i in range(len(dataset)):
        if assignments[i] == 1:
            cluster1_points.append(dataset[i])
        else:
            cluster2_points.append(dataset[i])

    new_c1_x = sum(p[0] for p in cluster1_points) / len(cluster1_points)
    new_c1_y = sum(p[1] for p in cluster1_points) / len(cluster1_points)

    new_c2_x = sum(p[0] for p in cluster2_points) / len(cluster2_points)
    new_c2_y = sum(p[1] for p in cluster2_points) / len(cluster2_points)

    new_centroid1 = [new_c1_x, new_c1_y]
    new_centroid2 = [new_c2_x, new_c2_y]

    print(f"\n  New Centroid 1: {new_centroid1}")
    print(f"  New Centroid 2: {new_centroid2}")

    if new_centroid1 == centroid1 and new_centroid2 == centroid2:
        print("\nCentroids did not move — converged!")
        break

    centroid1 = new_centroid1
    centroid2 = new_centroid2

print("\n── Final Clusters ──")
for i in range(len(dataset)):
    print(f"  {dataset[i]}  →  Cluster {assignments[i]}")

print(f"\nFinal Centroid 1: {centroid1}")
print(f"Final Centroid 2: {centroid2}")

# ─────────────────────────────────────────
# PLOT
# ─────────────────────────────────────────

for i in range(len(dataset)):
    x = dataset[i][0]
    y = dataset[i][1]

    if assignments[i] == 1:
        plt.scatter(x, y, color="steelblue", s=100, zorder=3)
    else:
        plt.scatter(x, y, color="orange", s=100, zorder=3)

plt.scatter(centroid1[0], centroid1[1], color="steelblue", marker="*",
            s=400, edgecolors="black", linewidths=1, zorder=4,
            label=f"Centroid 1 ({centroid1[0]:.2f}, {centroid1[1]:.2f})")
plt.scatter(centroid2[0], centroid2[1], color="orange", marker="*",
            s=400, edgecolors="black", linewidths=1, zorder=4,
            label=f"Centroid 2 ({centroid2[0]:.2f}, {centroid2[1]:.2f})")

plt.title("K-Means Clustering (k=2)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()