def ft_filter(funct, it):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if funct is None:
        return [x for x in it if x]
    return [x for x in it if funct(x)]
