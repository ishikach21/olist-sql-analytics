import pandas as pd
from pathlib import Path
data_path = Path("data/raw")

for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)

    print("\n" + "="*60)
    print("File:", file.name)
    print("Shape:", df.shape)

    print("\nCOLUMNS:")
    print(df.columns.tolist())
    
    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("\nSAMPLE RECORDS:")
    print(df.head(3))