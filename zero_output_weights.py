import caps
import colorbrewer
import numpy as np
from mytools import nf

num_neurons = 10 #50
threshold = 0.3
angle = np.arccos(threshold)

colors = [caps.normalize_color(c) for c in colorbrewer.Paired[5]]

colors = [(1.0, 0.0, 0.0)]

vectors = [np.array([0, 0, 1])]

caps.make_base_sphere(seed=21)

# ----------------
encoders, encoder_colors = caps.colored_encoders(
    vectors, colors, threshold, num_neurons)

caps.draw_encoders(encoders, colors=encoder_colors)

caps.draw_cap(vectors[0], colors[0], angle, alpha=0.3)
caps.draw_star(vectors[0], colors[0], alpha=0.8)
caps.draw_vector(vectors[0], colors[0])

# ----------------
colors = [caps.normalize_color(c) for c in colorbrewer.Paired[5]]
noisy_vec = nf.sample_cone(vectors[0], angle=np.pi/3.0)
noisy_vec = noisy_vec[0]

caps.draw_cap(noisy_vec, colors[0], angle, alpha=.5)
caps.draw_vector(noisy_vec, colors[0])
