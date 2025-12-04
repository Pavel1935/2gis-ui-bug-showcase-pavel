

class DirectionsLocators:
    FROM_INPUT = "input[placeholder='Откуда']"
    # инпут "Откуда"
    FROM_SUGGESTION_MOSCOW = 'xpath=//div[contains(@class, "_ck1x80") and normalize-space()="Москва"]'
    # Подсказка "Москва" в выпадающем списке
    TO_INPUT = "input[placeholder='Куда']"
    # инпут "Куда"
    TO_SUGGESTION_YEREVAN = 'xpath=//div[contains(@class, "_ck1x80") and normalize-space()="Ереван"]'
    # Подсказка "Ереван" в выпадающем списке
    TO_SUGGESTION_TBILISI = 'xpath=//div[contains(@class, "_ck1x80") and normalize-space()="Тбилиси"]'
    # Подсказка "Тбилиси" в выпадающем списке
    ERROR = "text='Что-то пошло не так'"
    # текст ошибки
    ERROR_TBILISI = "text='Не удалось проложить маршрут'"
    # текст ошибки
    SUGGEST_LIST = "div[class*='suggest']"
    # контейнер списка подсказок
    SUGGEST_ITEM = "div[class*='suggest__item']"
    # отдельный пункт подсказки
