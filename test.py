"""
This is a coding test for the role of Platform Engineer at MakeSpace. Please
complete this Python module, following the instructions below. Please feel free
to complete it in either Python 2 or 3.

 === Part 1 ===

 `nodes` is a list of sample geographical datapoints. Each node is a
 dictionary with a `lat`, `lon` and `id` value. The `lat` and `lon` values
 represent latitude and longitude, ie, cartesian coordinates on a sphere. For
 now, however, we'd like to treat these coordinates as though they lie on a
 flat plane, for simplicity's sake.

 Here's a sample:

 {"lat": -25.075021498182814, "lon": 49.05443017459794, "id":
  "1f2198df-3e29-48f7-92a7-985d10f799dd"}

 Please write a function that will take a list of node dictionaries with these
 keys, as well as an integer *n*, and groups the nodes into *n* different
 clusters. Please group the nodes so that each cluster contains nodes that are
 closest to each other. Your function will then return a list of lists, where
 each sublist is a group of node ids. For instance:

 >>> group_nodes(sample_data, 3)
 [['7d3aae7d-6b5b-4643-9c45-3c3ae822041d',
   '1b3d9e11-5b2d-4a6c-83b0-58f598144feb'],
  ['50b618ea-832f-4651-91cb-20841d9e6895'],
  ['63508d65-5d6b-4805-99ae-aa74fe64bdca',
   'bb0efb00-d7e2-4b3c-87f8-ee15936b43a6',
   'defb9877-bec0-4dcb-aba4-16c98daf78e2']]

 In this case our function returned three node groups over a list of six
 nodes: the first containing two nodes, the second containing one, the third
 containing three. It's important to note that the order of the groups, and
 the order within the groups doesn't matter.
 """


def group_nodes(node_list, number_of_groups):
    """
    Given a list of nodes and a number of groups to make *n*, returns a list of
    *n* lists of node ids.
    """

# === Part 2 ===


"""
`driving_time_and_distance()` is a function adapted from our routing logic that
takes two nodes, and returns a tuple representing the driving time between them
as well as the spherical distance. For instance:

>>> driving_time_and_distance(sample_data[0], sample_data[1])
(11171.132900883827, 1396.3916126104784)

Please note that `driving_time_and_distance()` will return the same values in either direction, for instance:

>>> driving_time_and_distance(sample_data[1], sample_data[2])
(11171.132900883827, 1396.3916126104784)

Please write a new function that will once again group nodes, this time using
the driving time - the first element in the tuple returned by
`driving_time_and_distance()` - as the value to be minimized when grouping
nodes.

Please feel free to reuse any of the code that you wrote in Part 1, if it's useful.
"""

from utils import driving_time_and_distance


def group_nodes2(node_list, number_of_groups):
    """
    Given a list of nodes and a number of groups to make *n*, returns a list of
    *n* lists of node ids, where the value to group by is the result of
    `driving_time_and_distance(n1, n2)`.
    """

"""
=== Part 3 ===

When grouping addresses to produce our daily routes, it's important that each
van has roughly the same number of stops to make in a day. Please write a new
function that will group nodes according to the driving time between nodes, but
this time additionally trying to optimize for equal size among each group.

Please feel free to reuse any of the code that you wrote in Parts 1 and 2, if
it's useful.
"""


def group_nodes3(node_list, number_of_groups):
    """
    Given a list of nodes and a number of groups to make *n*, returns a list of
    *n* lists of node ids, where the value to group by is the result of
    `driving_time_and_distance(n1, n2)`, and all sublists are roughly the same size.
    """

if __name__ == "__main__":
    from pprint import pprint
    from utils import nodes
    pprint(group_nodes(nodes, 6))
    pprint(group_nodes2(nodes, 6))
    pprint(group_nodes3(nodes, 6))
