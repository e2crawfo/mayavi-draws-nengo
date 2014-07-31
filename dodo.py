import datetime
import string

import caps
import scripts
import numpy as np
import mayavi.mlab as mlab

seed = 1
num_neurons = 100
threshold = 0.3
color1 = np.array([1.0, 0.0, 0.0])
color2 = np.array([0.0, 0.0, 1.0])

vector1 = np.array([0.0, 0.0, 1.0])
vector2 = np.array([1.0, 1.0, 0.0] / np.sqrt(2))

training_vector = np.array([1.0, 1.0, 1.0] / np.sqrt(3))

DOIT_CONFIG = {'verbosity': 2}

num_subtasks = 4

date_time_string = DOIT_CONFIG.get('datetime', '')

if not date_time_string:
    date_time_string = str(datetime.datetime.now()).split('.')[0]
    date_time_string = reduce(
        lambda y, z: string.replace(y, z, "_"),
        [date_time_string, ":", " ", "-"])

view = (22.500000000000011, 45.0, 6.9999999999999982,
        np.array([0.11703234, -0.14143265, -0.05305123]))

def task_plot1():
    filename = 'plot1/just_encoders.png'

    def f():
        caps.make_base_sphere(seed=seed)
        scripts.just_encoders(num_neurons)
        mlab.view(*view)
        mlab.savefig(filename)

    yield {'name': 'plot1',
           'actions': [(f, [])],
           'targets': [filename]}


def task_plot2():
    pass


def task_plot3():
    pass


def task_plot4():
    pass


def task_plot5():
    pass


def task_plot6():
    pass
