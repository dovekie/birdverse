import csv
import re
import requests
import predict_bird_url
from flask_sqlalchemy import SQLAlchemy
from birdverse import app

db = SQLAlchemy(app)

match_spuh = re.compile('\(.+\)')

from models import Bird

ebird_url = predict_bird_url.find_url()
local_bird_storage = 'birdverse/temp/raw_bird_data.csv'

def get_csv(url):
    r = requests.get(url, stream=True)
    print(r.status_code)
    with open(local_bird_storage, 'wb') as handle:
        for block in r.iter_content(1024):
            handle.write(block)
    return local_bird_storage

def process_csv(bird_storage):
    # Consider using yield here instead of return; it creates an iterable
    first_line = True
    with open(bird_storage, 'rU', encoding='mac_latin2') as bird_csv:
        bird_reader = csv.reader(bird_csv)
        while True:
            try:
                if first_line:
                    # skip the first row, which is headers
                    first_line = False
                    continue
                else:
                    bird_data = bird_reader.__next__()
                    if bird_data[1] == 'species':
                        print(bird_data)
                        # only load species data
                        create_bird(bird_data)
                    else:
                        continue
            except UnicodeDecodeError as error:
                print('ERROR {}'.format(error))
            except StopIteration:
                print("Finished loading birds")
                break

def create_bird(bird):
    common_name = bird[3]
    species_name = bird[4].split()[1]
    genus_name = bird[4].split()[0]
    family_name = bird[5]
    spuh = extract_spuh(bird[6])
    order_name = bird[6].split()[0]

    new_bird = Bird(
        common_name = common_name,
        species_name = species_name,
        genus_name = genus_name,
        family_name = family_name,
        order_name = order_name,
        spuh = spuh
        )
    db.session.add(new_bird)
    db.session.commit()

def extract_spuh(spuh_raw):
    spuh = ''
    matched = match_spuh.findall(spuh_raw)
    if matched:
        spuh = matched[0].strip('()')

    return spuh

def populate_the_database():
    process_csv(get_csv(ebird_url))