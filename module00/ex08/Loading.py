def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        progress = (i + 1) / total * 100
        bar = 20
        num_bars = int(progress / (100 / bar))
        progress_bar = "[" + "=" * num_bars + " " * (bar - num_bars) + "]"
        print(f"\r{int(progress)}%|{progress_bar}| ", end=f"{i+1}/{total}",
              flush=True)
        yield item
