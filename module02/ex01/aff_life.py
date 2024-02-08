from load_csv import load
import matplotlib.pyplot as plt


def ft_graph(load_file, country: str) -> bool:
    """View graph, Life expectancy to Year for the country"""
    data = load_file[load_file['country'] == country]
    if data.empty:
        print("Error: Country not found in the dataset.")
        return False
    x_column = data.columns[1:]
    y_column = data.iloc[0, 1:]
    plt.plot(x_column, y_column)
    plt.title("France Life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.xticks(x_column[::40])
    plt.show()
    return True


def main():
    load_file = load("life_expectancy_years.csv")
    if load_file is not None:
        ft_graph(load_file, "France")
    return


if __name__ == "__main__":
    main()
