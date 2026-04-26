import math
import matplotlib.pyplot as plt

dataset = [
    [1.2, 8.5, "Edible"],
    [2.1, 7.9, "Edible"],
    [1.8, 9.1, "Edible"],
    [2.5, 8.3, "Edible"],
    [1.5, 7.4, "Edible"],
    [3.1, 9.0, "Edible"],
    [2.0, 8.8, "Edible"],
    [1.9, 7.6, "Edible"],
    [7.5, 2.3, "Poisonous"],
    [8.2, 1.8, "Poisonous"],
    [7.8, 3.1, "Poisonous"],
    [9.0, 2.5, "Poisonous"],
    [8.5, 1.5, "Poisonous"],
    [7.2, 2.8, "Poisonous"],
    [8.8, 3.3, "Poisonous"],
    [9.1, 1.9, "Poisonous"],
]
 

mystery_cap_color = 8
.343
mystery_odor      = 8.1232
k = 9

distances = []

for row in dataset:
    cap_color = row[0]
    odor      = row[1]
    label     = row[2]

    distance = math.sqrt((mystery_cap_color - cap_color)**2 + (mystery_odor - odor)**2)
    distances.append([distance, label, cap_color, odor])  # store coords too for plotting
    print(f"Distance to ({cap_color}, {odor}) [{label}] = {distance:.2f}")

for i in range(len(distances)):
    for j in range(i + 1, len(distances)):
        if distances[j][0] < distances[i][0]:
            distances[i], distances[j] = distances[j], distances[i]

print("\nSorted distances:")
for d in distances:
    print(f"  {d[0]:.2f}  →  {d[1]}")

neighbors = distances[:k]

print(f"\nTop {k} neighbors:")
for n in neighbors:
    print(f"  {n[0]:.2f}  →  {n[1]}")

edible_count    = 0
poisonous_count = 0

for n in neighbors:
    if n[1] == "Edible":
        edible_count += 1
    else:
        poisonous_count += 1

print(f"\nVotes — Edible: {edible_count}  Poisonous: {poisonous_count}")

if edible_count > poisonous_count:
    predicted = "Edible"
else:
    predicted = "Poisonous"

print(f"Predicted class: {predicted}")

# ─────────────────────────────────────────
# PLOT
# ─────────────────────────────────────────

# collect neighbor coordinates for easy checking
neighbor_coords = [[n[2], n[3]] for n in neighbors]

# draw all dataset points
for row in dataset:
    x     = row[0]
    y     = row[1]
    label = row[2]

    if label == "Edible":
        plt.scatter(x, y, color="steelblue", s=100, zorder=3)
    else:
        plt.scatter(x, y, color="orange", s=100, zorder=3)

# draw lines from mystery point to each neighbor
for n in neighbors:
    nx = n[2]
    ny = n[3]
    plt.plot([mystery_cap_color, nx], [mystery_odor, ny],
             color="gray", linewidth=1.2, linestyle="-", zorder=2)

# plot mystery point on top
if predicted == "Edible":
    mystery_color = "steelblue"
else:
    mystery_color = "orange"

plt.scatter(mystery_cap_color, mystery_odor, color=mystery_color,
            s=180, edgecolors="black", linewidths=1.5, zorder=5)

plt.annotate(f"k={k} → {predicted}!",
             xy=(mystery_cap_color, mystery_odor),
             xytext=(mystery_cap_color + 0.2, mystery_odor + 0.2),
             fontsize=9, fontweight="bold")

plt.title("K-Nearest Neighbours")
plt.xlabel("X1 (Cap Color)")
plt.ylabel("X2 (Odor)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()