from scripts.ingest_data import load_data
from scripts.clean_data import clean_data
from scripts.transform_data import transform_data
from scripts.visualize_data import plot_data

if __name__ == "__main__":
    df = load_data("data/raw_data.csv")
    if df is not None:
        df = clean_data(df)
        df = transform_data(df)
        df.to_csv("data/cleaned_data.csv", index=False)
        plot_data(df, column='department')
