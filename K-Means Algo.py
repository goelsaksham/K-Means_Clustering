import matplotlib.pyplot as mp
import matplotlib.animation as animation
import numpy as np
import random as rand
import sys


class KMeans:
    def __init__(self, k, points, distance_calculator, iter_num):
        self.centroids = []
        self.k = k
        self.points = points
        self.distance_calc = distance_calculator
        self.groups = []
        self.no_of_iters = iter_num
        self.colors = ["b", "g", "r", "c", "m", "y", "k"]

    def get_centroids(self):
        return self.centroids

    def get_number_of_clusters(self):
        return self.k

    def get_points(self):
        return self.points

    def initialize_centroids(self):
        self.centroids.clear()
        for i in range(self.k):
            x_cor = 0.25*rand.random()
            y_cor = 0.25*rand.random()
            self.centroids.append((x_cor, y_cor))

    def initialize_centroid_groups(self):
        self.groups.clear()
        for i in range(self.k):
            self.groups.append([])

    def clear_centroid_groups(self):
        for group in self.groups:
            group.clear()

    def put_in_group(self, group_no, point):
        if group_no < 0 or group_no >= len(self.groups):
            raise Exception("Group Number out of bounds", group_no)
        else:
            self.groups[group_no].append(point)

    def get_group_number(self, point):
        min_dist_centroid = sys.maxsize
        index_min_dist_centroid = -1
        for i in range(len(self.centroids)):
            dist = self.distance_calc(point, self.centroids[i])
            if min_dist_centroid > dist:
                min_dist_centroid = dist
                index_min_dist_centroid = i
        return index_min_dist_centroid

    def assign_groups_to_points(self):
        self.clear_centroid_groups()
        for point in self.points:
            self.groups[self.get_group_number(point)].append(point)

    def get_x_cors(self, point_list):
        x_list = []
        for (x, y) in point_list:
            x_list.append(x)
        return x_list

    def get_y_cors(self, point_list):
        y_list = []
        for (x, y) in point_list:
            y_list.append(y)
        return y_list

    def get_new_centroid_for_group(self, group_no):
        try:
            group_x_cor = self.get_x_cors(self.groups[group_no])
            group_y_cor = self.get_y_cors(self.groups[group_no])
            x_mean = sum(group_x_cor)/len(group_x_cor)
            y_mean = sum(group_y_cor)/len(group_y_cor)
            return (x_mean, y_mean)
        except:
            return (0, 0)

    def recompute_centroids(self):
        self.centroids.clear()
        for group_no in range(self.k):
            self.centroids.append(self.get_new_centroid_for_group(group_no))

    def display_graph(self):
        for i in range(self.k):
            mp.scatter(self.get_x_cors(self.groups[i]), self.get_y_cors(self.groups[i]), c = self.colors[i])
            mp.scatter(self.centroids[i][0], self.centroids[i][1], c = self.colors[i], marker="x")
        mp.show()

    def run_k_means(self):
        self.initialize_centroid_groups()
        self.initialize_centroids()
        for iter_no in range(self.no_of_iters):
            self.clear_centroid_groups()
            self.assign_groups_to_points()
            self.display_graph()
            self.recompute_centroids()


def main():
    def euc_dist(point_a, point_b):
        x = point_a[0] - point_b[0]
        y = point_a[1] - point_b[1]
        return np.sqrt(x**2 + y**2)

    def manhattan_dist(point_a, point_b):
        x = point_a[0] - point_b[0]
        y = point_a[1] - point_b[1]
        return abs(x) + abs(y)

    def get_random_points(num_of_points):
        return [(rand.random(), rand.random()) for i in range(num_of_points)]

    '''points = get_random_points(100)
    k_means = KMeans(3, points, euc_dist, 10)
    k_means.run_k_means()'''
    c1 = [(0.5*rand.random(), 0.5 + 0.5*rand.random()) for i in range(100)]
    c2 = [(0.5 + 0.5 * rand.random(), 0.5 + 0.5 * rand.random()) for i in range(100)]
    c3 = [(0.5 + 0.5 * rand.random(), 0.5 * rand.random()) for i in range(100)]
    k_means = KMeans(3, c1+c2+c3, euc_dist, 5)
    k_means.run_k_means()

    '''c1 = [(i/100, np.cos(np.sin(np.pi * rand.random()))) for i in range(1, 101)]
    c2 = [(i / 100, np.sin(np.cos(np.pi * rand.random()))) for i in range(1, 101)]
    k_means = KMeans(6, c1 + c2, euc_dist, 5)
    k_means.run_k_means()'''


if __name__ == '__main__':
    main()