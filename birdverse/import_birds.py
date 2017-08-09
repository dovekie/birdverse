import csv
import requests

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
    all_birds = []
    with open(bird_storage, 'rU') as bird_csv:
        bird_reader = csv.reader(bird_csv, dialect=csv.excel_tab)
        for row in bird_reader:
            all_birds.append(row)
    return all_birds


print process_csv(get_csv(ebird_url))[1][0].split(',')