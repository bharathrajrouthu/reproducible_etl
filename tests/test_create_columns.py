import sys
sys.path.append("..")

import pandas as pd
from scripts.transform import Transform

transform_object = Transform()

def test_cast_data_types():
    df = pd.DataFrame({
        'date': pd.to_datetime(['01/01/2024', '01/02/2024', '01/03/2024']),
        'country': ['USA', 'Canada', 'UK']
    })
    converted_df = transform_object.create_columns(df)
    # Check if new columns are added and data types are correct
    assert 'year' in converted_df.columns
    assert 'quarter' in converted_df.columns
    assert 'month' in converted_df.columns
    assert 'week' in converted_df.columns
    assert 'day' in converted_df.columns
    assert 'day_name' in converted_df.columns
    assert 'country_id' in converted_df.columns