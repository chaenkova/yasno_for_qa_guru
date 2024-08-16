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


catalog = CatalogPage()
