import pandas as pand


def load(path: str) -> pand.DataFrame:
    """Function load csv"""
    try:
        nba = pand.read_csv(path)
    except FileNotFoundError:
        print("File not found")
        return None
    except pand.errors.ParserError:
        print("Bad format")
        return None
    print("Loading DataFrame of dimensions", nba.shape)
    return nba
