

# Set theory functions
def intersect(a,b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def union(a,b):
    """ return the union of two lists """
    return list(set(a) | set(b))
