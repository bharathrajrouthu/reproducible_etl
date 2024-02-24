import sys
sys.path.append("..")

from scripts.transform import *
import pandas as pd
from pandas.testing import assert_frame_equal

object_transform = Transform()

def test_clean_column_names():
    data = [['123', '456']]
    input_df = pd.DataFrame(data, columns=['Transaction No', 'Product No'])
    output_df = pd.DataFrame(data, columns=['Transaction_No', 'Product_No'])
    assert_frame_equal(object_transform.clean_columns(input_df), output_df)