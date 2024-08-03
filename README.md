![](https://assets.yasno.live/assets/logo-v3-c38b04297d1f116bcd4aba74a4285775f3c7ef78155b4309da2df317147671f2.svg)
# Автотесты для страницы каталога
---
## Проверяем быстрые фильтры каталога
<details>
<summary>Запуск локально</summary>
1. Склонировать репозиторий
  
  ```git clone https://github.com/chaenkova/yasno_for_qa_guru/tree/main```
  
2. Установить зависимости


```
python -m venv .venv
source .venv/bin/activate
poetry install
```

3. Запустить тесты

```
pytest .
```
4. Открыть отчет

```
allure serve allure-results/
```
</details>

<details>
<summary>Запуск удаленно через jenkins </summary>

1. [Открыть проект](https://jenkins.autotests.cloud/job/C13-LadyOokami-hw_14/)
  
2. Запустить тесты 

  ![](https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/Снимок%20экрана%202024-08-02%20в%2012.58.47.png)
3. Открыть отчет
![](https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/Снимок%20экрана%202024-08-02%20в%2012.59.02.png)

</details>

## Пример отчета

<details>
<summary>Jenkins </summary>

![](https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/Снимок%20экрана%202024-08-02%20в%2012.57.56.png)

</details>

<details>
<summary>Telegram </summary>

![](https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/Снимок%20экрана%202024-08-02%20в%2012.58.08.png)

</details>

<details>
<summary>Видео с прохождением </summary>
</details>
