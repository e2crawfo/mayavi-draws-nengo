import caps
import colorbrewer
import numpy as np

threshold = 0.7
num_neurons = 35
angle = np.arccos(threshold)

colors = [caps.normalize_color(c) for c in colorbrewer.Paired[5]]

vectors = [np.array([0, 0, 1])]

caps.make_base_sphere(seed=1)

caps.draw_encoders(num_neurons)

for vector, color in zip(vectors, colors):
    caps.draw_cap(vector, color, angle)
    caps.draw_vector(vector, color)
