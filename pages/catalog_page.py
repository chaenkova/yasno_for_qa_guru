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
            'div._relative._z-\[90\] > div._bg-white-100.md\:_px-5._px-4._pt-3._rounded-b-2xl._flex._gap-3._border-t._border-grey-500 > div._flex-1._flex._gap-4._overflow-auto._pb-3.md\:_flex-wrap > div > div > span')
         .should(have.exact_text(text)))

    @allure.step('Проверяем, фильтры по-умолчанию пустые')
    def should_have_no_filters(self):
        browser.element(by.text('Отменить')).click()
        browser.element(
            'div._relative._z-\[90\] > div._bg-white-100.md\:_px-5._px-4._pt-3._rounded-b-2xl._flex._gap-3._border-t._border-grey-500').should(
            be.absent)

#TODO: отрефакторить и добавить датакласс. Проходить в цикле все поля и искать их на странице
    @allure.step('Заполняем все фильтры в попапе')
    def fill_filters(self):
        browser.element(by.text('Стресс')).click()
        browser.element(by.text('Цена')).click()
        browser.element(by.text('2 850 ₽')).click()
        browser.element(by.text('Возраст')).click()
        browser.element(by.text('25-35 лет')).click()
        browser.element(by.text('Психотерапевтический подход')).click()
        browser.element(by.text('КПТ')).click()
        browser.element(by.text('Опыт')).click()
        browser.element(by.text('Более 5 лет')).click()
        browser.element(by.text('Пол')).click()
        browser.element(by.text('Мужской')).click()
        browser.element(by.text('Время сессии')).click()
        browser.element(by.text('Ближайшее')).click()
        browser.element(by.text('Дополнительные настройки')).click()
        browser.element(by.text('Без доступного времени')).click()
        browser.element(by.text('Показать')).click()
        return self

    @allure.step('Проверяем результат в выбранных фильтрах')
    def check_filters(self):
        browser.element(by.text('Cтресс')).should(be.existing)
        browser.element(by.text('2 850 ₽')).should(be.existing)
        browser.element(by.text('25-35 лет')).should(be.existing)
        browser.element(by.text('КПТ')).should(be.existing)
        browser.element(by.text('Более 5 лет')).should(be.existing)
        browser.element(by.text('Мужской')).should(be.existing)
        browser.element(by.text('Ближайшее время')).should(be.existing)
        browser.element(by.text('Без доступного времени')).should(be.existing)


catalog = CatalogPage()
