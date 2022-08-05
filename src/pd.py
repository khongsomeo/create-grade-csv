"""Pandas processing module"""

import pandas as pd
from .processing import Processing


class PandasProcessing(Processing):
    """Processing using Pandas"""

    def process_and_write(self) -> None:
        """Preprocessing data with Pandas"""

        df = pd.read_csv(self._Processing__input_file, sep="\t", header=None)
        df = df.drop(df.columns[[0, 3, 4, 6]], axis=1)
        df.columns = ["course_id", "course_credits", "course_grade"]
        df = df.dropna()

        df["course_id"] = df["course_id"].apply(
            PandasProcessing.clean_course_code)
        df["course_credits"] = df["course_credits"].astype(int)

        # Adding a pseudo type
        df["type"] = "BB"

        # Saving file as csv
        df.to_csv(self._Processing__output_file, header=False, index=False)
