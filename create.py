'''Simple module to generate grade.csv file'''

import argparse
from src.pd import PandasProcessing
from src.bs import BeautifulSoupProcessing

def main():
    '''Main driver'''

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        required = True,
        help = 'Input text file'
    )
    parser.add_argument(
        '--output',
        required = True,
        help = 'Output csv file'
    )
    parser.add_argument(
        '--pd',
        action = argparse.BooleanOptionalAction,
        help = 'Using pandas - input must be a text file'
    )
    parser.add_argument(
        '--bs',
        action = argparse.BooleanOptionalAction,
        help = 'Using BeautifulSoup - input must be a saved html file'
    )

    args = parser.parse_args()

    if args.pd is not None:
        print('Preprocessing with Pandas')

        creator = PandasProcessing(
            input_file = args.input,
            output_file = args.output
        )

        creator.process_and_write()

    elif args.bs is not None:
        print('Preprocessing with BeautifulSoup')

        creator = BeautifulSoupProcessing(
            input_file = args.input,
            output_file = args.output
        )

        creator.process_and_write()


if __name__ == '__main__':
    main()
