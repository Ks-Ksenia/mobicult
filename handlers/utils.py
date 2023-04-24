from datetime import date

import requests
from sqlalchemy.orm import Session

from database.models import Rate
from handlers.constants import CURRENCIES, CONVERT_TO, HEADERS, BASE_URL


def create_rate(rate_day: date, db: Session) -> Rate:
    params = {'to': CONVERT_TO, 'from': None, 'amount': 1, 'date': rate_day}

    response_rate = {}
    for currency in CURRENCIES:
        params['from'] = currency
        response = requests.get(url=BASE_URL, headers=HEADERS, params=params)
        response_rate.update({currency: response.json()['result']})

    rate = Rate(date_rate=rate_day, EUR=response_rate['EUR'], USD=response_rate['USD'])
    db.add(rate)
    db.commit()
    return rate
