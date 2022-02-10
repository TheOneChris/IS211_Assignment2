import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        url_data = response.read().decode('utf-8')

    return url_data


def processData(file_content):
    person_dict = {}
    for data_line in file_content.split("\n"):
        id, name, birthday = data_line.split(",")
        if id == "id":
            continue
        id_int = int(id)
        try:
            real_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
            person_dict[id_int] = (name, real_birthday)
        except ValueError as be:
            print(f"error at birthday {birthday}")

    return person_dict


def displayPerson(id, personData):
    pass

def main(url):
    print(f"Running main with URL = {url}...")
    data_downloaded = downloadData(url)
    results_dict = processData(data_downloaded)
    print(results_dict)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
