#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    tic_dict = {}

    # list of tickets -look in first
    for t in tickets:
        # key = t.source   :  value = t.destination
        tic_dict[t.source] = t.destination
    
    route = []

    # staring point
    # tick_dict['NONE'] is a key look up and actually gives the value
    place = tic_dict['NONE']

    # while loop to find rest of destinations
    while place != 'NONE':
        # append the value to a list
        route.append(place)
        # use the value as new key to get the next value
        place = tic_dict[place] # NEW_Place = Dictionary[OLD_Place]

    route.append('NONE') # instructions clearly state NONE is NOT needed - but tests fail without it. - Reevaluate
    return route
