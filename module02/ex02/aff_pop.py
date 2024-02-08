from load_csv import load
import matplotlib.pyplot as plt


def ft_graph_compare(load_file, country, versus) -> bool:
    data_country = load_file[load_file['country'] == country]
    data_versus = load_file[load_file['country'] == versus]
    if data_country.empty or data_versus.empty:
        print("Error: Country not found in the dataset.")
        return False
    years = [str(year) for year in range(1800, 2051)]
    x_column_filtered = [year for year in years if year in load_file.columns]
    plt.plot(x_column_filtered, data_versus[x_column_filtered].iloc[0], label=versus)
    plt.plot(x_column_filtered, data_country[x_column_filtered].iloc[0], label=country)
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.xticks(x_column_filtered[::40])
    data_country_numeric = data_country[x_column_filtered].iloc[0].str.replace('M', '').astype(float)
    data_versus_numeric = data_versus[x_column_filtered].iloc[0].str.replace('M', '').astype(float)
    max_population = max(data_country_numeric.max(), data_versus_numeric.max())
    y_ticks = [20, 40, 60]
    y_tick_labels = [f"M" for tick in y_ticks if tick <= max_population]
    plt.yticks(y_ticks, y_tick_labels)
    plt.legend()
    plt.show()
    return True


def main():
    load_file = load("population_total.csv")
    print(load_file)
    if load_file is not None:
        ft_graph_compare(load_file, "France", "Belgium")
    return


if __name__ == "__main__":
    main()
