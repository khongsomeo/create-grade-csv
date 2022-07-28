'''Pandas processing module'''

import pandas as pd

class PandasProcessing:
    '''Processing using Pandas'''

    def __init__(self, **kwargs) -> None:
        '''Initialise'''

        self.__input_file = kwargs.get('input_file', None)
        self.__output_file = kwargs.get('output_file', None)

    @staticmethod
    def clean_course_code(course_string):
        '''Clean the course code from original name-coursecode'''

        return course_string.split('-')[0].strip()

    def process_and_write(self) -> None:
        '''Preprocessing data with Pandas'''

        df = pd.read_csv(self.__input_file, sep = '\t', header = None)
        df = df.drop(df.columns[[0, 3, 4, 6]], axis = 1)
        df.columns = ['course_id', 'course_credits', 'course_grade']
        df = df.dropna()

        df['course_id']= df['course_id'].apply(PandasProcessing.clean_course_code)
        df['course_credits'] = df['course_credits'].astype(int)

        # Adding a pseudo type
        df['type'] = 'BB'

        # Saving file as csv
        df.to_csv(self.__output_file, header = False, index = False)
