import csv
import requests
from flask_sqlalchemy import SQLAlchemy
from birdverse import app


db = SQLAlchemy(app)


from models import Bird

ebird_url = ('http://help.ebird.org/customer/portal/'
             'kb_article_attachments/91238/original.csv?1471193184')
local_bird_storage = 'birdverse/temp/raw_bird_data.csv'

def get_csv(url):
    r = requests.get(url, stream=True)
    print r.status_code
    with open(local_bird_storage, 'wb') as handle:
        for block in r.iter_content(1024):
            handle.write(block)
    return local_bird_storage

def process_csv(bird_storage):
    first_line = True
    with open(bird_storage, 'rU') as bird_csv:
        bird_reader = csv.reader(bird_csv, dialect=csv.excel_tab)
        for row in bird_reader:
            if first_line:
                headers = row
                first_line = False
                continue
            bird_data = row[0].split(',')
            print bird_data
            new_bird = Bird(
                common_name = bird_data[4],
                species_name = bird_data[5].split()[1],
                genus_name = bird_data[5].split()[0],
                family_name = bird_data[6],
                order_name = bird_data[7],
                spuh = bird_data[8]
                )
            db.session.add(new_bird)
            db.session.commit()
    return all_birds


print process_csv(get_csv(ebird_url))[0][0].split(',')
print process_csv(get_csv(ebird_url))[1][0].split(',')