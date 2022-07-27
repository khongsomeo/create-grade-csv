'''Simple module to generate grade.csv file'''

import datetime
import argparse
import pandas as pd

def clean_course_code(course_string):
    '''Clean the course code from original name-coursecode'''

    return course_string.split('-')[0].strip()

def main():
    '''Main driver'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'Input text file')
    parser.add_argument('--output', help = 'Output csv file')

    args = parser.parse_args()

    # Preprocessing data with Pandas
    df = pd.read_csv(args.input, sep = '\t', header = None)
    df = df.drop(df.columns[[0, 3, 4, 6]], axis = 1)
    df.columns = ['course_id', 'course_credits', 'course_grade']   
    df = df.dropna()

    df['course_id']= df['course_id'].apply(clean_course_code)
    df['course_credits'] = df['course_credits'].astype(int)

    # Saving file as csv
    df.to_csv(args.output, header = False, index = False)

if __name__ == '__main__':
    main()
