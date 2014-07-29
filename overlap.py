import caps
import colorbrewer
import numpy as np

threshold = 0.3
angle = np.cos(threshold)

colors = [caps.normalize_color(c) for c in colorbrewer.Dark2[3]]

vectors = [
    (1.0 / np.sqrt(2)) * np.array([1, 1, 0]),
    (1.0 / np.sqrt(2)) * np.array([-1, -1, 0]),
    np.array([0, 0, 1]),
    ]
