import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print(f"✅ Loaded {len(data)} rows from {filepath}")
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
