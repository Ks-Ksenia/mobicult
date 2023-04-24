from datetime import date, timedelta

from fastapi import status

from main import app


class TestRate:
    def test_get_rate_today(self, client):
        response = client.get(app.url_path_for('rate_today'))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today())
        assert response.json()['EUR'] == 70

    def test_get_rate_day_without_query(self, client):
        response = client.get(app.url_path_for('rate_day'))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today())
        assert response.json()['EUR'] == 70

    def test_get_rate_day_today(self, client):
        response = client.get(app.url_path_for('rate_day'), params={'day': 'сегодня'})

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today())
        assert response.json()['EUR'] == 70

    def test_get_rate_day_yesterday(self, client):
        response = client.get(app.url_path_for('rate_day'), params={'day': 'вчера'})

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today() - timedelta(days=1))
        assert response.json()['EUR'] == 80

    def test_get_rate_day_before_yesterday(self, client):
        response = client.get(app.url_path_for('rate_day'), params={'day': 'позавчера'})

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today() - timedelta(days=2))
        assert response.json()['EUR'] == 90

    def test_get_rate_day_bad_name_day(self, client):
        response = client.get(app.url_path_for('rate_day'), params={'day': 'notday'})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['detail'] == 'The day is set incorrectly.'

    def test_get_rate_day_bad_query_param(self, client):
        response = client.get(app.url_path_for('rate_day'), params={'params': 'notday'})

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['date_rate'] == str(date.today())
        assert response.json()['EUR'] == 70
