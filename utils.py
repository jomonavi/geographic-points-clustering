import math


def driving_time_and_distance(src_lat, src_lon, dest_lat, dest_lon):
    """
    Given a node `src` `lat` and `lon` and a node `dest` `lat` and `lon`,
    return a tuple representing the driving time and the spherical distance
    between the two.
    """
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - src_lat) * degrees_to_radians
    phi2 = (90.0 - dest_lat) * degrees_to_radians

    # theta = longitude
    theta1 = src_lon * degrees_to_radians
    theta2 = dest_lon * degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (
        math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2)
        +
        math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)

    num_miles = arc * 3960
    minutes_per_mile = 8

    return num_miles * minutes_per_mile, num_miles
