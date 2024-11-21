from selene import browser, be, have, by, query
import allure


class CatalogPage:
    filters_for_catalog_popup = {
        "": "Стресс",
        'Цена': '3 950 ₽',
        'Возраст': '45-55 лет',
        'Психотерапевтический подход': 'Гештальт-терапия',
        'Опыт': 'Более 5 лет',
        'Пол': 'Мужской',
        'Время сессии': 'Ближайшее',
        'Дополнительные настройки': 'Без доступного времени'
    }

    def __init__(self):
        self.count = 0

    @allure.step('Выбираем значение в фильтре')
    def choose_item_in_filter(self, filters, item, locator='body'):
        browser.element(locator).element(by.text(filters)).click()
        browser.element(locator).element(by.text(item)).click()
        return self

    def click_apply_filters_button(self, locator='body'):
        browser.element(locator).element(by.text('Показать')).click()
        return self

    def click_close_filters_button(self, locator='body'):
        browser.element(locator).element(by.text('Отменить')).click()
        return self

    @allure.step('сравниваем количество терапевтов с ответом сервера')
    def check_count(self, count):
        return count < browser.all('.ysn-grid-without-outer-padding > div').count()

    @allure.step('Открыть каталог терапевтов')
    def open(self):
        browser.open('/therapists')
        return self

    @staticmethod
    @allure.step('Проверяем результат в выбранных фильтрах')
    def check_filters(filters: dict) -> bool:
        for value in filters.values():
            if not browser.element(by.text(value)).should(be.visible):
                return false
        return True

    @allure.step('Проверяем результат в выбранных фильтрах')
    def text_should_be_in_filters(self, text):
        (browser.element(
            '[data-id="therapist-catalog-short-filters"] div._overflow-auto span._whitespace-nowrap')
         .should(have.exact_text(text)))

    @allure.step('Проверяем, фильтры по-умолчанию пустые')
    def should_have_no_filters(self):
        browser.element(by.text('Отменить')).click()
        browser.element(
            '[data-id="therapist-catalog-short-filters"] div._overflow-auto span._whitespace-nowrap').should(
            be.absent)

    @allure.step('Заполняем все фильтры в попапе')
    def fill_filters(self, filters: dict):
        for key, value in filters.items():
            self.choose_item_in_filter(key, value, locator='._s-popup_layer')
        return self

    @allure.step('Заполняем пресет')
    def fill_filters_for_preset(self):
        popup = browser.element('._s-popup_layer')
        popup.element(by.text('Стресс')).click()
        popup.element(by.text('Приступы страха и тревоги')).click()
        return self

    @allure.step('Проверяем название страницы')
    def check_preset_title(self):
        browser.element(by.text('Помощь и консультация психолога при стрессе')).should(be.existing)

    @allure.step('Посчитать количество терапевтов')
    def count_therapists(self):
        browser.element(by.text('Отменить')).click()
        self.count = len(browser.all('.ysn-grid-without-outer-padding > div'))
        return self

    @allure.step('Нажать кнопку показать еще')
    def see_more(self):
        browser.element(by.text('Показать еще')).click()
        return self

    @allure.step('проверить, что психологов стало больше')
    def check_count(self):
        assert self.count < len(browser.all('.ysn-grid-without-outer-padding > div'))

    @allure.step('Сортировка по убыванию цены')
    def choose_sort_max_price(self):
        browser.element(by.text('Отменить')).click()
        browser.element(
            '[data-id="therapist-catalog-short-filters"] ._s-select._ml-auto ._inline-flex > div').click()
        browser.element(by.text('Сначала дороже')).click()
        browser.element('.ysn-grid-without-outer-padding span._t-body-accent').should(have.exact_text("4950 ₽"))

        return self

    @allure.step('Проверяем, что первым идет самый дорогой специалист')
    def check_sort_max_price(self):
        browser.element('.ysn-grid-without-outer-padding span._t-body-accent').should(have.exact_text("4950 ₽"))

    @allure.step('Клик на иконку информации рядом с ценой')
    def click_price_icon(self):
        browser.element(by.text('Отменить')).click()
        browser.all('.ysn-grid-without-outer-padding [data-v-005aaad4]')[3].click()
        return self

    @allure.step('Проверяем, что цена в попапе совпадает с ценой сессии терапевта')
    def check_price_in_popup(self):
        assert browser.element('.ysn-grid-without-outer-padding > div span._t-body-accent').get(
            query.text_content) == browser.element(
            'div[id^="headlessui-dialog-panel-"] ._s-popup_content span').get(query.text_content)

    @allure.step('Выбрать парную терапию')
    def choose_couple(self):
        browser.element('._s-popup_layer').element(by.text('Парная')).click()
        self.click_apply_filters_button('._s-popup_layer')
        return self

    @allure.step('Проверить, что у психолога выбрана парная')
    def check_couple(self):
        self.text_should_be_in_filters('Парная')


catalog = CatalogPage()
