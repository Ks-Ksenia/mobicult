from datetime import date, timedelta

CURRENCIES = ('EUR', 'USD')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'
HEADERS = {'apikey': 'LtdKsBvYOqIFhSqnuIAVtlVRtictVdfj'}
CONVERT_TO = 'RUB'

days = {'сегодня': date.today(),
        'вчера': date.today() - timedelta(days=1),
        'позавчера': date.today() - timedelta(days=2)}
