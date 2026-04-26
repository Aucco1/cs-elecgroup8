# Mushroom Classifier — kNN & K-Means from Scratch

Bare-bones implementations of **K-Nearest Neighbours (kNN)** and **K-Means Clustering** in pure Python, built for a computational science lab assignment. No external libraries except `matplotlib` for plotting and `math` from the standard library.

---

## Files

| File | Algorithm |
|---|---|
| `testknnplot.py` | K-Nearest Neighbours classifier |
| `testkmeanplot.py` | K-Means clustering |

---

## Dataset

Both scripts use the same synthetic mushroom dataset with **16 points** and **2 features**:

- **X1** — Cap color (encoded as a float)
- **X2** — Odor (encoded as a float)

The dataset has two natural groups:
- **Edible** — low cap color (~1–3), high odor (~7–9)
- **Poisonous** — high cap color (~7–9), low odor (~1–3)

---

## K-Nearest Neighbours (`testknnplot.py`)

Classifies a single mystery point by majority vote among its `k` nearest neighbours.

**How it works:**
1. Compute Euclidean distance from the mystery point to every training point
2. Sort distances (bubble sort — no `sorted()`)
3. Take the top `k` neighbours
4. Count votes by class; predict the majority

**Key parameters (edit at the top of the file):**
```python
mystery_cap_color = 8.343
mystery_odor      = 8.1232
k = 9
```

**Output:**
- Console: distances, sorted list, neighbour votes, predicted class
- Plot: dataset points colored by class, lines from mystery point to each neighbour, mystery point annotated with prediction

---

## K-Means Clustering (`testkmeanplot.py`)

Partitions the 16 points into `k` clusters by iteratively updating centroids.

**How it works:**
1. Initialize centroids manually (one from each natural group)
2. Assign every point to its nearest centroid (Euclidean distance)
3. Recompute each centroid as the mean of its assigned points
4. Repeat until centroids stop moving (convergence) or 10 iterations elapse

**Key parameters:**
```python
k = 2
centroid1 = dataset[0]   # starts in the Edible group
centroid2 = dataset[8]   # starts in the Poisonous group
```

**Output:**
- Console: per-iteration assignments and centroid updates, convergence notice
- Plot: points colored by cluster, final centroids marked with stars (★)

---

## Running

```bash
python testknnplot.py
python testkmeanplot.py
```

Requires Python 3 with `matplotlib` installed. No other dependencies.

---

## Constraints

- No NumPy, pandas, or scikit-learn
- CSV loading (where applicable) uses `open()` / `split()`
- Sorting done manually (bubble sort)
- Randomness via the `random` module with a fixed seed
- All math via the `math` standard library module
