import argparse
import requests
import json
import csv
import time

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Fetch data from an API endpoint and save it to a JSON file.')
parser.add_argument('--api_key', type=str, required=True, help='The API key to use for authentication.')
parser.add_argument('--start_date', type=str, required=False, help='The start date for the API query in DD/MM/YYYY format (Optional).')
parser.add_argument('--end_date', type=str, required=False, help='The end date for the API query in DD/MM/YYYY format (Optional).')
parser.add_argument('--output_file', type=str, default= f"mindd_{int(time.time())}.csv", help='The name of the output file. Defaults to "data.json".')
parser.add_argument('--convert_to_csv', type=bool, default=True, help = "save the output as a csv iso a json file")
args = parser.parse_args()

# Define the API endpoint and request parameters
url = "https://minddstatisticsfunctions.azurewebsites.net/api/GetStatistics"

params = {}
if args.start_date:
    params['fromDate'] = args.start_date
if args.end_date:
    params['ftoDate'] = args.end_date
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = {
    "apiKey": args.api_key
}

# Make the API request and save the response to a JSON file
response = requests.post(url, params=params, headers=headers, json=data)
if response.status_code == 200:
    with open(args.output_file, 'w') as f:
        if not args.convert_to_csv:
            json.dump(response.json(), f)
            print('Data as json saved to', args.output_file)
        else:
            # response .json is already a dict
            data = response.json()
            csv_headers = data['triageLogs'][0].keys()

            dict_writer = csv.DictWriter(f, csv_headers)
            dict_writer.writeheader()
            dict_writer.writerows(data['triageLogs'])
            print('Data as csv saved to', args.output_file)
            print(f"wrote {len(data['triageLogs'])} rows")

else:
    print('Error: API request failed with status code', response.status_code)
