import csv
import json

def convert(csv_file_path,starting_id):
    csv_file_path = "input/" + csv_file_path
    contents = []
    # Open a csv reader called DictReader
    with open(csv_file_path, encoding='utf-8') as csvfile:
        # get report ID number by removing last 4 characters from filename and spliting using "-" delimiter
        report_id = csv_file_path[:-4].split("-")[2]
        reader = csv.DictReader(csvfile)
        for row in reader:         
            item = {}
            item = row
            item["employee id"] = int(item["employee id"])
            item["_id"] = starting_id
            item["report_id"] = report_id
            contents.append(item)
            starting_id = starting_id + 1

    return contents
 
# csv_file_path = 'time-report-42.csv'
if __name__ == '__main__':
    print(convert(csv_file_path))