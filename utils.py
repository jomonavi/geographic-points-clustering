import math


nodes = [
    {'lat': 4.230509857737786, 'lon': -58.83513917625535, 'id': 'c24e8984-abd3-4e2a-ac5e-0dead05725f8'},
    {'lat': -15.056322793924458, 'lon': -52.76070496476228, 'id': '5403d956-b94b-4e9a-ad19-01b7f1eb9e56'},
    {'lat': -56.31197261613533, 'lon': 24.017742442610725, 'id': '4c399c25-f123-4779-851d-d0596159b898'},
    {'lat': 1.3195046909071664, 'lon': -0.3700245309310475, 'id': '9c347f4c-f71a-4cfb-8b36-61f5ffdb05e9'},
    {'lat': 43.36428271140588, 'lon': -35.98114501238928, 'id': '30eba78a-a6eb-45a7-8b72-5a36d808d2e9'},
    {'lat': -8.589863321845755, 'lon': 44.186367040126996, 'id': '03118df5-a580-4e9f-826f-dc5b41f7feba'},
    {'lat': 6.747279202142806, 'lon': 59.34492549054525, 'id': '1c56a83c-9cc7-4291-8bc4-23566d3dc4c5'},
    {'lat': -62.14779376810412, 'lon': -0.20321139110764364, 'id': 'aefa67ec-2cf3-474f-b3bb-5e1873110879'},
    {'lat': -5.359002337549484, 'lon': -13.578873147096928, 'id': 'ebf70658-cd25-45c4-a15b-f98b917c2b0f'},
    {'lat': -0.7742185610200778, 'lon': -26.424250144988612, 'id': 'f68b023c-ba05-422e-8471-d7eca3353b9a'},
    {'lat': 42.821924694104695, 'lon': -10.92858366557968, 'id': '98709670-6afa-4c12-b078-b60ea03c2f14'},
    {'lat': -36.92762379157924, 'lon': 34.08031576528795, 'id': '3ecbd240-a703-4d5f-9ab6-a80811e311e9'},
    {'lat': -1.430879580692391, 'lon': 3.496492083060346, 'id': 'd1271e6e-79ad-4379-b7c3-3b4d901b56ae'},
    {'lat': -19.586843563772703, 'lon': 68.52471543327056, 'id': '4b606635-81c2-4c48-9c9f-c10ac037dea6'},
    {'lat': 45.55412982307638, 'lon': 19.75217558786288, 'id': '8c872e69-77d5-40a4-ac3e-f243b62b2603'},
    {'lat': -16.522415781825543, 'lon': 34.08972847505888, 'id': '0d7697f8-ca52-469e-ab37-6a1c3d9bced6'},
    {'lat': 33.15407356416611, 'lon': -68.96823135754707, 'id': 'cbc0a802-bac6-4874-a3ed-1a53d2fd3fbf'},
    {'lat': -6.264035616417708, 'lon': 59.29064650821658, 'id': 'a80b4093-e3a7-4170-a540-cfa3492dd613'},
    {'lat': 29.041771139888283, 'lon': -35.544161819780484, 'id': '48eaebd4-0378-4975-bba9-9ace64ac1146'},
    {'lat': 53.937768081735285, 'lon': -23.703774651396465, 'id': 'efb18ffe-5bb3-41cd-9091-69b5b8c7dc12'},
    {'lat': 36.50598279170022, 'lon': -14.331469248442254, 'id': '345a6413-1b3f-458a-9025-7c429efd5c83'},
    {'lat': 37.752470156339356, 'lon': -2.3919603900013158, 'id': '267e4e4e-3e04-49e8-abdd-5acfad81bfde'},
    {'lat': 41.642281063649236, 'lon': -47.5846275470942, 'id': '987d2aa3-8d50-487a-b518-b8ec14c1fb78'},
    {'lat': 51.781771813421074, 'lon': -23.628909377154635, 'id': '8fe9bc96-4df9-42e2-a8b6-c6e44e393e94'},
    {'lat': -21.311593388405313, 'lon': 13.745771447285989, 'id': '22b35e59-427c-4cac-a691-cbb45c1ab196'},
    {'lat': 13.92548008143801, 'lon': -55.950201194974746, 'id': '1ee672e8-8cfd-4929-8535-0fe7223b8e8a'},
    {'lat': -20.65992452346304, 'lon': 11.176212408909407, 'id': 'df891ebe-4f6e-4b71-8421-2be9dc9c45cd'},
    {'lat': -69.72949792483399, 'lon': -60.91756174826216, 'id': '6a5e0d52-4019-4b35-b970-ef00eb72538a'},
    {'lat': -18.815953437670835, 'lon': -60.95243597301045, 'id': '8ef1d3a0-d92d-42ae-bca4-de8ab1aa9922'},
    {'lat': 2.0954847442446294, 'lon': 21.32214036416667, 'id': 'f3617976-2b6b-4cb7-8db7-5b6aafa58e3c'}
]


def driving_time_and_distance(src, dest):
    """
    Given a node `src` and a node `dest`, return a tuple representing the
    driving time and the spherical distance between the two.
    """
    origin_lat = src['lat']
    origin_lon = src['lon']
    dest_lat = dest['lat']
    dest_lon = dest['lon']
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - origin_lat) * degrees_to_radians
    phi2 = (90.0 - dest_lat) * degrees_to_radians

    # theta = longitude
    theta1 = origin_lon * degrees_to_radians
    theta2 = dest_lon * degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2)
    arc = math.acos(cos)

    num_miles = arc * 3960
    minutes_per_mile = 8

    return num_miles * minutes_per_mile, num_miles