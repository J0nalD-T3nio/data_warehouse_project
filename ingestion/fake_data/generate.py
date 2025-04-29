""" Python script for generating dummy data"""

import json
from datetime import datetime
from sys import argv
from pathlib import Path
from shutil import rmtree
from concurrent.futures import ThreadPoolExecutor
from faker import Faker

def generate_fake_person(faker: Faker, num: int, folder: Path) -> dict:
    """
        Parameters:

        Returns:
    """
    print(f"Generating fake person data id={num}")

    # Dictionary of fake person details
    fake_person = {
        # Identity
        "id": num,
        "full_name": faker.name(),
        "is_male": faker.boolean(chance_of_getting_true=55),
        "dob": faker.date_of_birth().strftime("%Y-%m-%d"),
        "ssn": faker.ssn(),

        # Contact details
        "email": faker.email(),
        "phone": faker.phone_number(),

        # Location
        "address": faker.address(),
        "city": faker.city(),
        "state": faker.state(),
        "zipcode": faker.zipcode(),
        "country": faker.country(),
    }

    with open(folder / f"{num}.json", "w") as fp:
        json.dump(fake_person, fp)

if __name__=="__main__":

    # Some logs
    start_time = datetime.now()
    print(f"{start_time}: App has started")

    # Control the number of records
    if len(argv)>=2:
        RECORDS = int(argv[1])
    else:
        # Oh no! 'Di ba masisira PC ko?
        RECORDS = 1_000_000

    # Delete existing folder with dummy files
    folder = Path("files")
    if folder.is_dir():
        rmtree(folder)

    # Recreate the folder
    folder.mkdir(exist_ok=True)

    # Initialize Faker class and set seed for reproducibility
    fake = Faker()
    Faker.seed(20240901)

    # Parallel generation of fake data; use tqdm for visual progress bar
    with ThreadPoolExecutor() as executor:
        for i in range(1,RECORDS + 1):
            executor.submit(generate_fake_person, fake, i, folder)

    # Some logs
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"{end_time}: App has ended. Runtime: {duration}")
