# Create grade.csv file

Preprocess grades from VNUHCM - US portal.

## How-to?
Install required packages:
```
pip install -r requirements.txt
```

### Using Pandas
Login to Portal, choose "All grades", then copy the grade table and paste to 
`sample.txt`. Run `create.py` from the command line:
```
python create.py --input <newly-created file> --output <result.csv> --pd
```

Notice the `--pd` option.

Example with previous `sample.txt`:
```
python create.py --input sample.txt --output sample.csv --pd
```

Your formatted grades will be inside `sample.csv`. 

### Using BeautifulSoup
Save the Portal webpage to html page (Save As -> html). Run `create.py` from
the command line:
```
python create.py --input <newly-created html file> --output <result.csv> --bs
```

Notice the `--bs` option.

Example with previous `sample.html`:
```
python create.py --input sample.html --output sample.csv --bs
```

Your formatted grades will be inside `sample.csv`. 

For detail command-line arguments, using
```
python create.py --help
```
