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
                    first_line = False
                    continue
                else:
                    bird_data = bird_reader.__next__()

                    if bird_data[1] == 'species':
                        new_bird = Bird(
                            common_name = bird_data[3],
                            species_name = bird_data[5].split()[1],
                            genus_name = bird_data[5].split()[0],
                            family_name = bird_data[6],
                            order_name = bird_data[7],
                            spuh = bird_data[8]
                            )
                        db.session.add(new_bird)
                        db.session.commit()
                    else:
                        continue
            except UnicodeDecodeError as error:
                print('ERROR {}'.format(error))
            except StopIteration:
                print("Finished loading birds")
                break


    


process_csv(get_csv(ebird_url))