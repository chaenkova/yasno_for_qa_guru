from selene import browser, be, have, by
import allure


class CatalogPage:

    @allure.step('Открыть каталог терапевтов')
    def open(self):
        browser.open('/therapists')
        return self

    @allure.step('Выбираем стресс в симптомах')
    def chose_stress(self):
        browser.element(by.text('Отменить')).click()
        browser.element(by.text('Симптомы')).click()
        browser.element(by.text('Стресс')).click()
        browser.element(by.text('Показать')).click()
        return self

    @allure.step('Выбираем кпт в подходах')
    def chose_kpt(self):
        browser.element(by.text('Отменить')).click()
        browser.element(by.text('Подход')).click()
        browser.element(by.text('КПТ')).click()
        browser.element(by.text('Показать')).click()
        return self

    @allure.step('Выбираем 2850 в цене')
    def chose_price(self):
        browser.element(by.text('Отменить')).click()
        browser.element(by.text('Цена')).click()
        browser.element(by.text('2850 ₽')).click()
        browser.element(by.text('Показать')).click()
        return self

    @allure.step('Выбираем мужской пол')
    def chose_sex(self):
        browser.element(by.text('Отменить')).click()
        browser.element(by.text('Пол')).click()
        browser.element(by.text('Мужской')).click()
        browser.element(by.text('Показать')).click()
        return self

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

    #TODO: отрефакторить и добавить датакласс. Проходить в цикле все поля и искать их на странице
    @allure.step('Заполняем все фильтры в попапе')
    def fill_filters(self):
        popup = browser.element('._s-popup_layer')
        popup.element(by.text('Стресс')).click()
        popup.element(by.text('Цена')).click()
        popup.element(by.text('2 850 ₽')).click()
        popup.element(by.text('Возраст')).click()
        popup.element(by.text('25-35 лет')).click()
        popup.element(by.text('Психотерапевтический подход')).click()
        popup.element(by.text('КПТ')).click()
        popup.element(by.text('Опыт')).click()
        popup.element(by.text('Более 5 лет')).click()
        popup.element(by.text('Пол')).click()
        popup.element(by.text('Мужской')).click()
        popup.element(by.text('Время сессии')).click()
        popup.element(by.text('Ближайшее')).click()
        popup.element(by.text('Дополнительные настройки')).click()
        popup.element(by.text('Без доступного времени')).click()
        popup.element(by.text('Показать')).click()
        return self

    @allure.step('Заполняем пресет')
    def fill_filters_for_preset(self):
        popup = browser.element('._s-popup_layer')
        popup.element(by.text('Стресс')).click()
        popup.element(by.text('Приступы страха и тревоги')).click()
        popup.element(by.text('Показать')).click()
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

    @allure.step('Проверяем результат в выбранных фильтрах')
    def check_filters(self):
        browser.element(by.text('Стресс')).should(be.existing)
        browser.element(by.text('2 850 ₽')).should(be.existing)
        browser.element(by.text('25-35 лет')).should(be.existing)
        browser.element(by.text('КПТ')).should(be.existing)
        browser.element(by.text('Более 5 лет')).should(be.existing)
        browser.element(by.text('Мужской')).should(be.existing)
        browser.element(by.text('Ближайшее время')).should(be.existing)
        browser.element(by.text('Без доступного времени')).should(be.existing)
        return self

    @allure.step('Сортировка по убыванию цены')
    def chose_sort_max_price(self):
        browser.element(by.text('Отменить')).click()
        browser.element(
            '[data-id="therapist-catalog-short-filters"] ._s-select ._inline-flex > div').click()
        browser.element('[data-v-70ec965c]').click()
        browser.element('.ysn-grid-without-outer-padding span._t-body-accent').should(have.exact_text("4950 ₽"))

        return self

    @allure.step('Проверяем, что первым идет самый дорогой специалист')
    def check_sort_max_price(self):
        browser.element('.ysn-grid-without-outer-padding span._t-body-accent').should(have.exact_text("4950 ₽"))

    @allure.step('Клик на иконку информации рядом с ценой')
    def click_price_icon(self):
        browser.element(by.text('Отменить')).click()
        browser.element('[data-v-005aaad4]').click()
        return self

    @allure.step('Проверяем, что цена в попапе совпадает с ценой сессии терапевта')
    def check_price_in_popup(self):
        assert browser.element('.ysn-grid-without-outer-padding > div span._t-body-accent').value == browser.element(
            'div[id^="headlessui-dialog-panel-"] _s-popup_content span').value

    @allure.step('Выбрать парную терапию')
    def chose_couple(self):
        browser.element('._s-popup_layer').element(by.text('Парная')).click()
        browser.element('._s-popup_layer').element(by.text('Показать')).click()
        return self

    @allure.step('Проверить, что у психолога выбрана парная')
    def check_couple(self):
        self.text_should_be_in_filters('Парная')


catalog = CatalogPage()
