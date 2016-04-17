import random
from pprint import pprint
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
    def __init__(self, k, points, iterations):
        self.k = k
        self.points = points
        self.iterations = iterations


    def k_means(self):
        """
        Runs the k means algorithm
        """
        centroids = random.sample(self.points, self.k)
        list_of_ids = []

        clusters = self.fill_clusters(centroids)

        for i in range(self.iterations):
            new_centroids = self.reset_centroids(clusters)
            if new_centroids == centroids:
                print("this happened!")
                return clusters
            else:
                clusters = self.fill_clusters(new_centroids)

        for key in clusters:
            c = []
            for p in clusters[key]:
                c.append(p['id'])
            list_of_ids.append(c)

        return list_of_ids

    def find_nearest_centroid(self, p, centroids):
        """
        Finds the nearest center for a given point
        """
        distances = []

        for i, o_p in enumerate(centroids):
            d = haversine(p['lon'], p['lat'], o_p['lon'], o_p['lat'])
            distances.append((i, d))

        distances.sort(key=lambda tup: tup[1])
        return distances[0]

    def fill_clusters(self, centroids):
        """
        Assigns points to clusters based on its closest center point
        """
        clusters = {}
        for i, p in enumerate(self.points):
            center = self.find_nearest_centroid(p, centroids)
            center_i = center[0]
            key = centroids[center_i]['id']
            if key not in clusters:
                clusters[key] = []

            clusters[key].append(p)

        return clusters

    def reset_centroids(self, clusters):
        """
        Calculates new center points for each iteration of k-means
        """
        new_centroids = []

        for key in clusters:
            lat_sum, lon_sum = 0, 0
            for p in clusters[key]:
                lat_sum += p['lat']
                lon_sum += p['lon']
            lat_mean = lat_sum / len(clusters[key])
            lon_mean = lon_sum / len(clusters[key])

            distances = []
            for p in clusters[key]:
                d  = haversine(p['lon'], p['lat'], lon_mean, lat_mean)
                distances.append((d, p))

            distances.sort(key=lambda tup: tup[0])
            new_centroids.append(distances[0][1])

        return new_centroids

            

