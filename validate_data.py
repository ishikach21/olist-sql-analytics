
import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

files_to_check = {
    "customers": {
        "file": "olist_customers_dataset.csv",
        "key": ["customer_id"]
    },
    "orders": {
        "file": "olist_orders_dataset.csv",
        "key": ["order_id"]
    },
    "order_items": {
        "file": "olist_order_items_dataset.csv",
        "key": ["order_id", "order_item_id"]
    },
    "order_payments": {
        "file": "olist_order_payments_dataset.csv",
        "key": ["order_id", "payment_sequential"]
    },
    "order_reviews": {
        "file": "olist_order_reviews_dataset.csv",
        "key": ["review_id"]
    },
    "products": {
        "file": "olist_products_dataset.csv",
        "key": ["product_id"]
    },
    "sellers": {
        "file": "olist_sellers_dataset.csv",
        "key": ["seller_id"]
    },
    "category_translation": {
        "file": "product_category_name_translation.csv",
        "key": ["product_category_name"]
    }
}

for table, info in files_to_check.items():
    df = pd.read_csv(data_path / info["file"])

    duplicate_count = df.duplicated(subset=info["key"]).sum()

    print(f"\nTABLE: {table}")
    print("Rows:", len(df))
    print("Candidate key:", info["key"])
    print("Duplicate key combinations:", duplicate_count)
