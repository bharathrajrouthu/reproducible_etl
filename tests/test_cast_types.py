import sys
sys.path.append("..")

import pandas as pd
from transform import Transform

transform_object = Transform()

def test_cast_types():
    df = pd.DataFrame({
        'transaction_id': ['001', '002', '003'],
        'customer_id': ['1001', '1002', '1003'],
        'date': ['01/01/2024', '01/02/2024', '01/03/2024']
    })
    converted_df = transform_object.cast_types(df)
    # Check if 'transaction_id' and 'customer_id' are converted to int
    assert converted_df['transaction_id'].dtype == 'int64'
    assert converted_df['customer_id'].dtype == 'int64'
    # Check if 'date' is converted to datetime
    assert pd.api.types.is_datetime64_any_dtype(converted_df['date'])