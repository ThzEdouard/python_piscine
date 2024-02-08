from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def ft_graph(load_ippgpia, load_ley) -> bool:
    life_expectancy = load_ley.loc[:, '1900']
    gross_domestic = load_ippgpia.loc[:, '1900']
    plt.scatter(gross_domestic, life_expectancy)
    plt.title("1900")
    plt.ylabel("Life expectancy")
    plt.xlabel("Gross domestic product")
    plt.show()
    return True


def main():
    load_ippgpia = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    load_ley = load("life_expectancy_years.csv")
    if load_ippgpia is not None and load_ley is not None:
        ft_graph(load_ippgpia, load_ley)
    return


if __name__ == "__main__":
    main()
