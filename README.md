# Mindd get
A simple python script to interact with the moetiknaardedokter.nl API, and save the result in json or csv format.

Output of the --help flag:
```txt
$python3 mindd_get.py --help

usage: mindd_get.py [-h] --api_key API_KEY [--start_date START_DATE]
                    [--end_date END_DATE] [--output_file OUTPUT_FILE]
                    [--convert_to_csv CONVERT_TO_CSV]

Fetch data from an API endpoint and save it to a JSON file.

options:
  -h, --help            show this help message and exit
  --api_key API_KEY     The API key to use for authentication.
  --start_date START_DATE
                        The start date for the API query in DD/MM/YYYY format
                        (Optional).
  --end_date END_DATE   The end date for the API query in DD/MM/YYYY format
                        (Optional).
  --output_file OUTPUT_FILE
                        The name of the output file. Defaults to "data.json".
  --convert_to_csv CONVERT_TO_CSV
                        save the output as a csv iso a json file
```
