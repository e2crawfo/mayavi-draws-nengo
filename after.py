import caps
import colorbrewer
import numpy as np

threshold = 0.3
num_neurons = 35
angle = np.cos(threshold)

colors = [caps.normalize_color(c) for c in colorbrewer.Paired[5]]

vectors = [np.array([0, 0, 1])]

caps.make_base_sphere(seed=1)

encoders, encoder_colors = caps.colored_encoders(
    vectors, colors, threshold, num_neurons)

caps.draw_encoders(encoders, colors=encoder_colors)
