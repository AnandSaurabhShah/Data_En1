import pandas as pd

def transform_data():
    df = pd.read_csv("data/raw/orders.csv")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Convert date
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Feature engineering
    df['total_amount'] = df['quantity'] * df['unit_price']

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]

    df.to_csv("data/cleaned/clean_orders.csv", index=False)

    print("Transformation completed successfully")
