from selene import browser, be, have, by, query
import allure


class CatalogPage:
    filters_for_catalog_popup = {
        "": "Стресс",
        'Возраст': '45-55 лет',
        'Психотерапевтический подход': 'Гештальт-терапия',
        'Опыт': 'Более 5 лет',
        'Пол': 'Мужской',
        'Дополнительные настройки': 'Без доступного времени'
    }

    def __init__(self):
        self.count = 0
        self.psychologists_cards = '.ysn-grid-without-outer-padding > div'
        self.popup = '._s-popup_layer'
        self.short_filters = '[data-id="therapist-catalog-short-filters"] div._overflow-auto span._whitespace-nowrap'
        self.price_in_card = '.ysn-grid-without-outer-padding > div span._t-body-accent'
        self.sorter_element = '[data-id="therapist-catalog-short-filters"] ._s-select._ml-auto ._inline-flex > div'
        self.price_in_popup = 'div[id^="headlessui-dialog-panel-"] ._s-popup_content span'
        self.items_in_therapists_card = '.ysn-grid-without-outer-padding [data-v-005aaad4]'
        self.apply = 'button._btn-base-primary:not([data-v-92448bd6])'
        self.cancel = 'button._btn-base-secondary'
        self.see_more_button = 'button._btn-base-secondary'
        self.short_filter_select = 'div[data-v-d3bbf6ba]._tw-ui-dropdown__content'
        self.price_with_space = '3 950 ₽'
        self.price = '3950 ₽'
        self.time_with_space = 'Ближайшее время'
        self.time = 'Ближайшее'

    @allure.step('Выбираем значение в фильтре')
    def choose_item_in_filter(self, filters, item, locator='body'):
        browser.element(locator).element(by.text(filters)).click()
        browser.element(locator).element(by.text(item)).click()
        return self

    def click_apply_filters_button(self, locator):
        print(browser.element(locator).element(self.apply))
        browser.element(locator).element(self.apply).click()
        return self

    def click_close_filters_button(self, locator):
        browser.element(locator).element(self.cancel).click()
        return self

    @allure.step('сравниваем количество терапевтов с ответом сервера')
    def check_count(self, count):
        return count < len(browser.all(self.psychologists_cards))

    @allure.step('Открыть каталог терапевтов')
    def open(self):
        browser.open('/therapists')
        return self

    @staticmethod
    @allure.step('Проверяем результат в выбранных фильтрах')
    def check_filters(filters: dict, price, time) -> bool:
        for value in filters.values():
            if not browser.element(by.text(value)).should(be.visible):
                return False
        return browser.element(by.text(price)).should(be.visible) and browser.element(by.text(time)).should(be.visible)

    @allure.step('Проверяем результат в выбранном фильтре')
    def text_should_be_in_filters(self, text):
        browser.element(self.short_filters) \
            .should(have.exact_text(text))

    @allure.step('Проверяем, фильтры по-умолчанию пустые')
    def should_have_no_filters(self):
        browser.element(by.text('Отменить')).click()
        browser.element(self.short_filters).should(be.absent)

    @allure.step('Заполняем все фильтры в попапе')
    def fill_filters(self, filters: dict, price, time):
        self.choose_item_in_filter('Цена',  price, locator=self.popup)
        self.choose_item_in_filter('Время сессии', time, locator=self.popup)
        for key, value in filters.items():
            self.choose_item_in_filter(key, value, locator=self.popup)
        return self

    @allure.step('Заполняем пресет')
    def fill_filters_for_preset(self):
        popup = browser.element(self.popup)
        popup.element(by.text('Стресс')).click()
        popup.element(by.text('Приступы страха и тревоги')).click()
        return self

    @allure.step('Проверяем название страницы')
    def check_preset_title(self):
        browser.element(by.text('Помощь и консультация психолога при стрессе')).should(be.existing)

    @allure.step('Посчитать количество терапевтов')
    def count_therapists(self):
        self.click_close_filters_button(locator=self.popup)
        self.count = self.cont_of_therapists_on_page()
        return self

    def cont_of_therapists_on_page(self):
        return len(browser.all(self.psychologists_cards))

    @allure.step('Нажать кнопку показать еще')
    def see_more(self):
        browser.element(self.see_more_button).click()
        return self

    @allure.step('проверить, что психологов стало больше')
    def check_count(self):

        assert self.count < self.cont_of_therapists_on_page()

    @allure.step('Сортировка по убыванию цены')
    def choose_sort_max_price(self):
        browser.element(by.text('Отменить')).click()
        browser.element(self.sorter_element).click()
        browser.element(by.text('Сначала дороже')).click()

        return self

    @allure.step('Проверяем, что первым идет самый дорогой специалист')
    def check_sort_max_price(self):
        browser.element(self.price_in_card).should(have.exact_text("4950 ₽"))

    @allure.step('Клик на иконку информации рядом с ценой')
    def click_price_icon(self):
        self.click_close_filters_button(locator=self.popup)
        browser.all(self.items_in_therapists_card)[3].click()
        return self

    @allure.step('Проверяем, что цена в попапе совпадает с ценой сессии терапевта')
    def check_price_in_popup(self):
        assert browser.element(self.price_in_card).get(
            query.text_content) == browser.element(self.price_in_popup).get(query.text_content)

    @allure.step('Выбрать парную терапию')
    def choose_couple(self):
        browser.element(self.popup).element(by.text('Парная')).click()
        return self

    @allure.step('Проверить, что у психолога выбрана парная')
    def check_couple(self):
        self.text_should_be_in_filters('Парная')

    @allure.step('Проверить наличие парных симптомов')
    def check_couple_symptoms_in_popup(self):
        browser.element(self.popup).element(by.text('Созависимость')).should(be.existing)
        return self


catalog = CatalogPage()
