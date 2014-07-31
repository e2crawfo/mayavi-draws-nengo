import caps
import numpy as np


def just_encoders(num_neurons):
    caps.draw_encoders(num_neurons)


def show_threshold(vector, color, threshold, num_neurons):
    angle = np.arccos(threshold)

    caps.draw_encoders(num_neurons)

    caps.draw_cap(vector, color, angle)
    caps.draw_vector(vector, color)


def claimed_neurons(vector, color, threshold, num_neurons):
    encoders, encoder_colors = caps.colored_encoders(
        vector, color, threshold, num_neurons)

    caps.draw_encoders(encoders, colors=encoder_colors)


def zero_output_weights(vectors, colors, noisy_vec, threshold, num_neurons):
    angle = np.arccos(threshold)

    # ----------------
    encoders, encoder_colors = caps.colored_encoders(
        vectors, colors, threshold, num_neurons)

    caps.draw_encoders(encoders, colors=encoder_colors)
    caps.draw_vector(vectors[0], colors[0])

    # ----------------
    caps.draw_cap(noisy_vec, colors[0], angle, alpha=.5)
    caps.draw_testing_vector(noisy_vec, colors[0])


def need_encoder_movement(vectors, colors, threshold, num_neurons):
    angle = np.arccos(threshold)

    # ----------------
    encoders, encoder_colors = caps.colored_encoders(
        vectors, colors, threshold, num_neurons)

    caps.draw_encoders(encoders, colors=encoder_colors)
    caps.draw_vector(vectors[0], colors[0])

    # ----------------
    caps.draw_cap(vectors[0], colors[0], angle, alpha=.5)
    caps.draw_vector(vectors[0], colors[0])


def stolen_neurons(vectors, colors, threshold, num_neurons):
    # ----------------
    caps.draw_vector(vectors[0], colors[0])
    caps.draw_vector(vectors[1], colors[1])

    # reverse to get the right ordering
    vectors = vectors[::-1]
    colors = colors[::-1]

    encoders, encoder_colors = caps.colored_encoders(
        vectors, colors, threshold, num_neurons)

    caps.draw_encoders(encoders, colors=encoder_colors)
