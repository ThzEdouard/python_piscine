from load_csv import load
import matplotlib.pyplot as plt


def ft_graph_compare(load_file, country, versus) -> bool:
    """View graph country versus """
    if country == versus:
        print("Error: Country or Versus is ==")
        return False
    data_country = load_file[load_file['country'] == country]
    data_versus = load_file[load_file['country'] == versus]
    if data_country.empty or data_versus.empty:
        print("Error: Country or Versus not found in the dataset.")
        return False
    years = [str(year) for year in range(1800, 2051)]
    x_column_filtered = [year for year in years if year in load_file.columns]
    data_country_numeric = data_country[x_column_filtered].iloc[0].str
    data_country_numeric = data_country_numeric.replace('M', '').astype(float)
    data_versus_numeric = data_versus[x_column_filtered].iloc[0].str
    data_versus_numeric = data_versus_numeric.replace('M', '').astype(float)
    plt.plot(x_column_filtered, data_versus_numeric, label=versus)
    plt.plot(x_column_filtered, data_country_numeric, label=country)
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.xticks(x_column_filtered[::40])
    plt.legend()
    plt.show()
    return True


def main():
    load_file = load("population_total.csv")
    if load_file is not None:
        ft_graph_compare(load_file, "France", "Belgium")
    return


if __name__ == "__main__":
    main()
