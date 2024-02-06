def ft_filter(funct, it):
    ret = []
    for its in it:
        if funct(its):
            ret.append(its)
    return ret
