import sys
sys.path.append("..")

import pandas as pd
from scripts.transform import Transform

transform_object = Transform()

def test_remove_missing_values():
    df = pd.DataFrame({
        'transaction_id': ['T001', 'T002', 'C003'],
        'customer_id': [1001, None, 1003],
        'other_column': ['A', 'B', 'C']
    })   
    cleaned_df = transform_object.remove_missing_values(df)
    # Check if missing values in 'customer_id' are removed
    assert cleaned_df['customer_id'].isnull().sum() == 0
    # Check if rows containing 'C' in 'transaction_id' are filtered out
    assert 'C' not in cleaned_df['transaction_id'].values