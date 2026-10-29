def plane_ride_cost(city):
    """
    Calculates the plane ride cost based on the destination city.
    """
    costs = {
        "Charlotte": 183,
        "Tampa": 220,
        "Pittsburgh": 222,
        "Los Angeles": 475
    }
    return costs.get(city)
