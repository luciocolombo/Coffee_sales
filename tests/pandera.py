import pandera.pandas as pa


def validate_schema(df):
    schema = pa.DataFrameSchema({})
    return df
