def ft_statistics(*args: any, **kwargs: any) -> None:
    numbers = [x for x in args if isinstance(x, (int, float))]
    for kwarg in kwargs.values():
        if "mean" in kwarg:
            if not numbers:
                print("ERROR")
            else:
                mean = sum(numbers) / len(numbers)
                print(f"mean : {mean}")
        elif "median" in kwarg:
            if not numbers:
                print("ERROR")
            else:
                sorted_numbers = sorted(numbers)
                n = len(sorted_numbers)
                median = (sorted_numbers[n // 2] if n % 2 != 0 else
                          (sorted_numbers[n // 2 - 1] +
                           sorted_numbers[n // 2]) / 2)
                print(f"median : {median}")
        elif "quartile" in kwarg:
            if not numbers:
                print("ERROR")
            else:
                sorted_numbers = sorted(numbers)
                quartile_25_index = int(len(sorted_numbers) * 0.25)
                quartile_75_index = int(len(sorted_numbers) * 0.75)
                quartile_25 = float(sorted_numbers[quartile_25_index])
                quartile_75 = float(sorted_numbers[quartile_75_index])
                print(f"quartile : [{quartile_25}, {quartile_75}]")
        elif "std" in kwarg:
            if not numbers:
                print("ERROR")
            else:
                mean = sum(numbers) / len(numbers)
                variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
                std_dev = variance ** 0.5
                print(f"std : {std_dev}")
        elif "var" in kwarg:
            if not numbers:
                print("ERROR")
            else:
                mean = sum(numbers) / len(numbers)
                variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
                print(f"var : {variance}")
