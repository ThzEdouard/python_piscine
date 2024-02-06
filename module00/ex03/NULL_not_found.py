from types import NoneType


def NULL_not_found(object: any) -> int:
    if type(object) is NoneType and object == None:
        print("Nothing:", object, type(object))
    elif type(object) is float and object != object:
        print("Cheese:", object, type(object))
    elif type(object) is int and object == 0:
        print("Zero:", object, type(object))
    elif type(object) is str and object == '':
        print("Empty:", type(object))
    elif type(object) is bool and object == False:
        print("Fake:", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0
