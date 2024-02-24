import sys
sys.path.append("..")

from scripts.transform import Transform
import pandas as pd
from pandas.testing import assert_frame_equal

object_transform = Transform()

def test_standardize_columns():
    data = [['123', '456']]
    input_df = pd.DataFrame(data, columns=['Transaction_No', 'Product_No'])
    output_df = pd.DataFrame(data, columns=['transaction_id', 'product_id'])
    assert_frame_equal(object_transform.standardize_columns(input_df), output_df)