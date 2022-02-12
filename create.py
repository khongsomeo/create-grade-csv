import datetime, sys, getopt
import pandas as pd

def clean_course_code(course_string):
    return course_string.split('-')[0].strip()

def main(argv):
    input_file, output_file = '', ''
    
    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        elif opt == '--output':
            output_file = arg

    if (input_file == '' or output_file == ''):
        print('Missing arguments, please try again')
        sys.exit(2)

    # Preprocessing data with Pandas
    df = pd.read_csv(input_file, sep = '\t', header = None)
    df = df.drop(df.columns[[0, 3, 4, 6]], axis = 1)
    df.columns = ['course_id', 'course_credits', 'course_grade']   
    df = df.dropna()

    df['course_id']= df['course_id'].apply(clean_course_code)
    df['course_credits'] = df['course_credits'].astype(int)

    # Saving file as csv
    df.to_csv(output_file, header = False, index = False)

if __name__ == '__main__':
    main(sys.argv[1:])
