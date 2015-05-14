"""
testing out the code
"""

import argparse

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

from min_bounding_rect import minBoundingRect as get_mbr


def plot_stuff(points, hull, mbr):
    f = plt.figure()
    axes = f.add_subplot(111)
    axes.plot(points[:, 0], points[:, 1], 'og')
    axes.plot(hull[:, 0], hull[:, 1], 'r--')
    axes.plot(mbr[:, 0], mbr[:, 1], 'o-b')
    f.show()


def main(samples):
    for i in xrange(samples):
        points = np.random.rand(30, 2)
        hull = ConvexHull(points)
        vertices = points[hull.vertices]
        params = get_mbr(vertices)
        rot_angle, area, width, height, center_point, corners = params
        plot_stuff(points, vertices, corners)
    while True:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--samples", type=int, default=1)
    args = parser.parse_args()
    main(args.samples)
