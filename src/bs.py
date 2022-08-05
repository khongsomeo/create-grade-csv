"""BeautifulSoup processing module"""

from bs4 import BeautifulSoup
import pandas as pd
from .processing import Processing


class BeautifulSoupProcessing(Processing):
    """Processing using BeautifulSoup"""

    def __preprocess(self, soup: BeautifulSoup) -> []:
        """Preprocessing data"""

        result_list = []

        for row in soup.find(id="lich-thi-dkhp").tbody:
            subject_name, credit, grade = "", 0, 0

            status = ""

            for index, td in enumerate(row):
                if index == 3:
                    subject_name = BeautifulSoupProcessing.clean_course_code(
                        td.text.strip())

                if index == 5:
                    credit = td.text.strip()

                if index == 7:
                    status = td.text.strip()

                if index == 11:
                    grade = td.text.strip()

            if len(credit) == 0:
                continue

            if len(grade) == 0:
                continue

            # Append to the list, also adding a pseudo type
            result_list.append([subject_name, int(credit), float(grade), "BB"])

        return result_list

    def process_and_write(self):
        """Preprocessing data with BeautifulSoup"""

        with open(self._Processing__input_file) as input_handle:
            soup = BeautifulSoup(input_handle, "html.parser")

        result_list = self.__preprocess(soup)

        df = pd.DataFrame(result_list)

        df.to_csv(self._Processing__output_file, header=False, index=False)
