import requests
from datetime import datetime

def find_url():
    current_year = datetime.now().year
    year_lookback = 0
    status_code = 0

    while status_code != 200:
        year = current_year - year_lookback
        ebird_url = (f'http://www.birds.cornell.edu/clementschecklist/wp-content/uploads/{year}/'
            f'08/Clements-Checklist-v{year}-August-{year}.csv')

        status_code = requests.head(ebird_url).status_code
        year_lookback += 1
    return ebird_url