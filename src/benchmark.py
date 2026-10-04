import pandas as pd


def prepare_benchmark(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    result = result.sort_values("latency_ms")

    return result


if __name__ == "__main__":
    data = pd.read_csv("data/benchmark.csv")
    print(prepare_benchmark(data))