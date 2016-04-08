import json, sys, pprint
from kmeans import Cluster

clusters, iterations, input_file = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]

with open(input_file) as data_file:
    points = json.load(data_file)

geo_clusters = Cluster(clusters, points, iterations)
val = geo_clusters.k_means()

with open('results2.json', 'w') as outfile:
    json.dump(val, outfile, sort_keys=True, indent=4, separators=(',', ': '))