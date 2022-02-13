import argparse
import urllib.request
import logging
import datetime

logging.basicConfig(filename="errors.log", level=logging.ERROR)
assignment2 = logging.getLogger()


def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        url_data = response.read().decode('utf-8')

    return url_data


def processData(file_content):
    person_dict = {}
    for data_line in file_content.split("\n"):
        if data_line.strip() == "":
            continue
        id, name, birthday = data_line.split(",")
        if id == "id":
            continue
        try:
            real_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
            person_dict[id] = (name, real_birthday)
        except ValueError:
            assignment2.error('Error at ID ' + id + ' with birthday ' + birthday)

    return person_dict


def displayPerson(id, personData):
    try:
        info = personData[id]
        return "The person with ID " + id + " has a birthday of " + info[1].strftime("%d/%m/%Y")
    except:
        return "No person with that ID found"


def main(url):
    print(f"Running main with URL = {url}...")
    try:
        file_content = downloadData(url)
        personData = processData(file_content)
        while True:
            ID = input("Enter ID number to look data or enter <1 to exit: ")
            if int(ID) > 0:
                print(displayPerson(ID, personData))
            else:
                break
    except:
        assignment2.error('Error while getting data from URL, Please try again with different URL')


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
