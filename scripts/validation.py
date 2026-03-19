import pandas as pd

def validate_data():
    df = pd.read_csv("data/cleaned/clean_orders.csv")

    assert df.isnull().sum().sum() == 0, "Null values found!"
    assert (df['quantity'] > 0).all(), "Invalid quantity!"
    assert (df['unit_price'] > 0).all(), "Invalid price!"

    print("Data validation passed!")
