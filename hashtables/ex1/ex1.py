from typing import Dict, List, Tuple

# Conversion list --> dictionary
def list_to_dict(a: List[object]) -> Dict[object, List[int]]:
    ''' takes in a list, converts to dictionary, 
    while retaining values that are duplicates
    '''

    my_dict = dict()
    
    # index = 0

    # for element in a:
    #     if element in my_dict:
    #         my_dict[element].append(index)
    #     else:
    #         my_dict[element] = [index]
    #     index += 1

    for index, element in enumerate(a):
        if element in my_dict:
            my_dict[element].append(index)
        else:
            my_dict[element] = [index]

    return my_dict

def get_indices_of_item_weights(weights: List[int], length: int, limit: int) -> Tuple[int, int]:
    """
    YOUR CODE HERE
    """
    cat = list_to_dict(weights)

    # for loop that looks at each weight(key)
    for key in list(cat.keys()): # this makes a copy
        # Pop the key index in case key == compliment
        i1 = cat[key].pop(0)

        # If popping the index leaves the list at that key empty, the key is no
        #    longer valid for the dictionary, so delete the key from the dictionary
        if cat[key] == []:
            del cat[key]

        # take the current key and get the compliment (limit - key)
        compliment = limit - key

        # search via the compliment
        if compliment in cat:
            # Save the index of the complement (first occurrence)
            i2 = cat[compliment][0]

            # Organize the two indices and return them
            if i1 > i2:
                return (i1, i2)
            else:
                return (i2, i1)

    # The for loop ended and no valid pair was found, so return None
    return None
