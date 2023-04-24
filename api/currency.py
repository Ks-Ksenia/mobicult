# Написать веб-приложение заходя на главную страницу которого пользователь видит текущий курс рубля для доллара и евро.
# Источник получения курса валюты можно выбрать на свое усмотрение. Курс необходимо обновлять раз в сутки.
# Пользователь может выбрать день (сегодня, вчера, позавчера) и увидеть курс на этот день.
# В приложении должны присутствовать unit-тесты на вывод курса и его получение/обновление.


from datetime import date
from typing import Optional, Union

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database.crud import get_db
from database.models import Rate
from handlers.constants import days

route = APIRouter()


@route.get('/', response_model=None, name='rate_today')
def get_today_rate(db: Session = Depends(get_db)) -> Union[Rate, JSONResponse]:
    """
        Get the current ruble exchange rate for euro and dollar.
    :return: JSONResponse or model Rate
    """
    rate = db.query(Rate).filter_by(date_rate=date.today()).first()
    if not rate:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={'detail': 'The value for the day was not found.'})
    return rate


@route.get('/rateDay', response_model=None, name='rate_day')
def get_rate_day(day: Optional[str] = None, db: Session = Depends(get_db)) -> Union[Rate, JSONResponse]:
    """
        Get the ruble exchange rate per day for euro and dollar.
    :param day: the day for which you need to get a course
    :param db: object Session
    :return: JSONResponse or model Rate
    """
    if day not in days.keys() and day is not None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={'detail': 'The day is set incorrectly.'})

    if not day:
        rate_day = days['сегодня']
    else:
        rate_day = days.get(day)

    rate = db.query(Rate).filter_by(date_rate=rate_day).first()

    if not rate:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={'detail': 'The value for the day was not found.'})
    return rate
