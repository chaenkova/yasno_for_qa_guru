import pytest
from pages.rzhd_page import rzhd


@pytest.mark.parametrize("city_from, city_to", ('Москва', 'Казань'))
def test_search_today(city_from, city_to):
    rzhd.open_from_station()
    rzhd.click_city(city_from)
    rzhd.open_to_station(city_to)
    rzhd.chose_today_date()
    rzhd.click_search()
    rzhd.check_from_to_today(city_from, city_to)


@pytest.mark.parametrize("city", ['Брянск', 'Казань', pytest.param('Неверленд', marks=pytest.mark.xfail(strict=True))])
def test_rzhd_search_terminal(city):
    rzhd.open_from_station()
    rzhd.type_city(city)
    rzhd.check_all_station_of_city()


@pytest.mark.parametrize("city", ['Брянск'])
def test_rzhd_search_city_duplicates(city):
    rzhd.open_from_station()
    rzhd.type_city(city)
    rzhd.check_same_cities_exist()


@pytest.mark.parametrize("city", ['Брянск'])
def test_rzhd_clear_search_field(city):
    rzhd.open_from_station()
    rzhd.type_city(city)
    rzhd.clean_field_from()
    rzhd.check_clean_field()


def test_flies_waiting_text_is_present():
    rzhd.chose_fly()
    rzhd.check_fly_popup()
