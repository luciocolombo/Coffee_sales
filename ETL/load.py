import pandas as pd


def load():
    df = pd.read_csv("./Dataset/dirty_cafe_sales.csv")
    return df
