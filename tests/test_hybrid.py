"""Testing BeautifulSoup and Pandas"""

import os
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from src.bs import BeautifulSoupProcessing
from src.pd import PandasProcessing


class TestHybrid:
    """Hybrid testing class"""

    def setup(self):
        """Setup testing class"""
        self.__bs_output_file = 'bs_output.csv'
        self.__bs_input_file = 'tests/data/sample.html'

        self.__pd_output_file = 'pd_output.csv'
        self.__pd_input_file = 'tests/data/sample.txt'

        # Create a BS output
        bs_creator = BeautifulSoupProcessing(
            input_file=self.__bs_input_file,
            output_file=self.__bs_output_file
        )

        bs_creator.process_and_write()

        self.__bs_result_df = pd.read_csv(
            self.__bs_output_file
        )

        # Create a PD output
        pd_creator = PandasProcessing(
            input_file=self.__pd_input_file,
            output_file=self.__pd_output_file
        )

        pd_creator.process_and_write()

        self.__pd_result_df = pd.read_csv(
            self.__pd_output_file
        )

    def teardown(self):
        """Clear leftovers"""

        os.remove(self.__bs_output_file)
        os.remove(self.__pd_output_file)

    def test_can_create(self):
        """Testing if the module is doing well"""

        # Testing if bs is doing well
        assert os.path.isfile(self.__bs_output_file)
        assert self.__bs_result_df is not None

        # Testing if pd is doing well
        assert os.path.isfile(self.__pd_output_file)
        assert self.__pd_result_df is not None

    def test_struct(self):
        """Testing the structure of results"""

        # Testing if bs is ok
        assert self.__bs_result_df.shape == (43, 4)

        assert self.__bs_result_df.dtypes.to_list() == [
            np.dtype('O'),
            np.dtype('int64'),
            np.dtype('float64'),
            np.dtype('O')
        ]

        # Testing if pd is ok
        assert self.__pd_result_df.shape == (43, 4)

        assert self.__pd_result_df.dtypes.to_list() == [
            np.dtype('O'),
            np.dtype('int64'),
            np.dtype('float64'),
            np.dtype('O')
        ]

    def test_the_same(self):
        """Test if the contents are the same"""

        assert_frame_equal(self.__pd_result_df, self.__bs_result_df)
