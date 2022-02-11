import datetime, sys, getopt
import pandas as pd

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

    df = pd.read_csv(input_file, sep = '\t', header = None)
    df = df.drop(df.columns[[0, 3, 4, 6]], axis = 1)
    df = df.dropna()
    df[1, :] = df[1, :].split('-')[0].strip()
    print(df)

if __name__ == '__main__':
    main(sys.argv[1:])
