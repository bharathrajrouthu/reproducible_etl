import sys
sys.path.append("..")

import pandas as pd
from transform import Transform

transform_object = Transform()

def test_remove_duplicates_positive():
        # Positive test case with duplicate rows
        df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]})
        df_cleaned = transform_object.remove_duplicates(df)
        assert len(df_cleaned) == 3  # Assert that duplicate rows are removed

def test_remove_duplicates_negative():
        # Negative test case with no duplicate rows
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df_cleaned = transform_object.remove_duplicates(df)
        assert len(df_cleaned) == 3  # Assert that no rows are removed