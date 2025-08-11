"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x,y,*last = each_wagons_id
    wagons = last + [x, y]
        # Remove locomotive to reinsert it at the front
    wagons.remove(1)
    # Place 1 at the front, then missing wagons, then the rest
    return [1, *missing_wagons, *wagons]

def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param stops: arbitrary keyword arguments of stops.
    :return: dict - updated route dictionary.
    """
    route.setdefault("stops", [])
    route["stops"].extend(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    #Lets unpack the first list
    a,b,c = wagons_rows[0]
    d,e,f = wagons_rows[1]
    g,h,i = wagons_rows[2] 
    return [[a,d,g],[b,e,h],[c,f,i]]
