def has_negatives(a):
    """
    YOUR CODE HERE
    """
    bird = {}

    # convert to dictionary
    for i in a:
        # fill the dictionary 
        # each 'i' will be the key and all values will be None
        bird[i] = None
    
    # list for the keys that are positive
    pos_a = [i for i in a if i > 0]
    
    result = []

    for i in pos_a:
        if (i*-1) in bird:
            result.append(i)
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
