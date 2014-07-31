import mytools.threed as threed
import mayavi.mlab as mlab
import numpy as np
import nengo.utils.distributions as dists

radius = 1.0
black = (0.0, 0.0, 0.0)
white = (1.0, 1.0, 1.0)


def normalize_color(c):
    return tuple(np.array(c) / 255.0)


def make_base_sphere(seed=None):
    mlab.figure(
        figure=None, fgcolor=None, engine=None, size=(400, 350))

    cap = threed.make_cap(
        r=radius, cap_angle=np.pi, direction=np.array([0, 0, 1]),
        usteps=50, vsteps=50)

    mlab.mesh(*cap, representation='surface', color=white)

    engine = mlab.get_engine()

    from mayavi.modules.outline import Outline
    o = Outline()
    engine.add_module(o)

    from mayavi.modules.axes import Axes
    ax = Axes()
    engine.add_module(ax)

    if seed is not None:
        np.random.seed(seed)


def colored_encoders(vectors, colors, threshold, num_neurons=30):
    """
    Randomly generates encoders and assigns them colors based
    on their similarity to the given input vectors.
    """

    encoders = dists.UniformHypersphere(3, surface=True).sample(num_neurons)
    encoder_colors = []

    for enc in encoders:
        c = black
        for vector, color in zip(vectors, colors):
            if np.dot(enc, vector) > threshold:
                c = color
                break

        encoder_colors.append(c)

    return encoders, encoder_colors


def draw_encoders(encoders, angle=None, colors=None):
    """Add encoders to the scene.

    Can either supply a collection of encoders, or an integer giving the
    number of encoders to randomly generate.

    encoders: int or collection
    angle: angle giving size of the cap drawn to represent an encoder
    colors: collection of normalized rgb colors to paint the encoders
    """

    if isinstance(encoders, int):
        encoders = dists.UniformHypersphere(3, surface=True).sample(encoders)

    if colors is None:
        colors = [black for e in encoders]

    if not angle:
        angle = 0.01 * np.pi

    for enc, color in zip(encoders, colors):
        front = color
        back = black

        cap = threed.make_cap(r=1.01*radius, cap_angle=angle, direction=enc)
        mlab.mesh(*cap, color=front, opacity=1.0)

        cap = threed.make_cap(r=1.007*radius, cap_angle=angle, direction=enc)
        mlab.mesh(*cap, color=back, opacity=1.0)


def draw_vector(vector, color):
    v = (0.0, 0.0, 0.0) + tuple(vector)
    v = np.array(v)

    v = mlab.pipeline.vectors(mlab.pipeline.vector_scatter(*v), color=color)

    return v


def draw_cap(vector, color, cap_angle, alpha=0.8, func=None):
    cap = threed.make_cap(
        r=1.02*radius, cap_angle=cap_angle, direction=vector, func=func)

    mesh = mlab.mesh(*cap, color=color, opacity=alpha)

    return mesh


def draw_star(vector, color, cap_angle=np.pi/32, freq=10, amplitude=0.3, alpha=0.8):

    func = lambda x: 1 + amplitude * np.sin(freq * x)

    mesh = draw_cap(
        vector, color, np.pi/32, alpha=alpha, func=func)

    return mesh
