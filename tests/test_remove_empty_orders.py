import sys
sys.path.append("..")

import pandas as pd
from transform import Transform

transform_object = Transform()

def test_remove_empty_orders():
    df = pd.DataFrame({
        'order_id': [1, 2, 3, 4],
        'quantity': [5, 0, 10, -1],  # Include some rows with empty orders
        'product_name': ['A', 'B', 'C', 'D']
    })
    cleaned_df = transform_object.remove_empty_orders(df)
    # Check if rows with empty orders (quantity <= 0) are removed
    assert (cleaned_df['quantity'] <= 0).sum() == 0