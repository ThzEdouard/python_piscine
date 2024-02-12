def ft_filter(funct, it):
    """filter"""
    ret = []
    for its in it:
        if funct(its):
            ret.append(its)
    return ret
