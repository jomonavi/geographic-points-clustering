import numpy
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles, 6371 for kilometers
    return c * r

class Cluster(object):

    def __init__(self, points):
        self.points = points
        self.clusters = []
        self.MinPts = int(math.floor(math.sqrt(len(self.points)))) - 1
        self.set_eps()

    def set_eps(self):
        all_kth_distances = []
        k = int(math.floor(math.sqrt(len(self.points)))) - 1
        print(k)

        for i, point in enumerate(self.points):
            distances = []
            for j, other_point in enumerate(self.points):
                if i != j:
                    # d = math.sqrt((other_point['lat'] - point['lat'])**2 + (other_point['lon'] - point['lon'])**2)
                    d = haversine(point['lon'], point['lat'], other_point['lon'], other_point['lat'])
                    # distances.append((d, point['id']))
                    distances.append(d);
            distances.sort()
            kth_nearest_distances = distances[:k]
            all_kth_distances = all_kth_distances + kth_nearest_distances

        eps = numpy.mean(all_kth_distances)
        print(math.sqrt(eps))
        self.eps = math.sqrt(eps)


    def DBSCAN(self):
        for i, point in enumerate(self.points):
            if not 'is_visited' in point:
                point['is_visited'] = True

                NeighborPts = self.region_query(point, self.eps)
                if len(NeighborPts) < self.MinPts:
                    point['is_noise'] = True
                else:
                    cluster = []
                    self.expand_cluster(point, NeighborPts, cluster, self.eps, self.MinPts)

        # print("wonder what it looks like", len(self.clusters), self.clusters[0])
        return self.clusters

    def expand_cluster(self, point, NeighborPts, cluster, eps, MinPts):
        cluster.append(point)

        for i, np in enumerate(NeighborPts):
            is_in_cluster = False
            if not 'is_visited' in np:
                np['is_visited'] = True
                other_NeighborPts = self.region_query(np, self.eps)
                if len(other_NeighborPts) >= self.MinPts:
                    NeighborPts = NeighborPts + other_NeighborPts

                for c in self.clusters:
                    if any(loc['id'] == np['id'] for loc in c):
                        is_in_cluster = True

            if not is_in_cluster:
                cluster.append(np)

        self.clusters.append(cluster)

    def region_query(self, point, eps):
        neighbors = []

        for i, o_p in enumerate(self.points):
            if point is not o_p:
                d = math.sqrt(haversine(point['lon'], point['lat'], o_p['lon'], o_p['lat']))
                if d <= eps:
                    neighbors.append(o_p)

        return neighbors


