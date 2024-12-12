import pytest
from pages.rzhd_page import rzhd


def test_android_search_today():
    rzhd.open_from_station()
    rzhd.click_city("Москва")
    rzhd.open_to_station("Казань")
    rzhd.chose_today_date()
    rzhd.click_search()
    rzhd.check_from_to_today("Москва","Казань")


@pytest.mark.parametrize("city", ['Брянск', 'Казань', pytest.param('Неверленд', marks=pytest.mark.xfail)])
def test_android_rzhd_search_terminal(city):
    rzhd.open_from_station()
    rzhd.type_city(city)
    rzhd.check_all_station_of_city()


@pytest.mark.parametrize("city", ['Брянск'])
def test_android_rzhd_search_city_duplicates(city):
    rzhd.open_from_station()
    rzhd.type_city(city)
    rzhd.check_duplicates()


def test_android_rzhd_clear_search_field():
    rzhd.open_from_station()
    rzhd.type_city('Брянск')
    rzhd.clean_field_from()
    rzhd.check_clean_field()


def test_android_flies_waiting_text_is_present():
    rzhd.chose_fly()
    rzhd.check_fly_popup()
