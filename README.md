![](https://assets.yasno.live/assets/logo-v3-c38b04297d1f116bcd4aba74a4285775f3c7ef78155b4309da2df317147671f2.svg)
# Автотесты для страницы каталога
---
## Что покрыто тестами?
1. быстрые фильтры по параметрам: пол, возраст, опыт, симптомы, цена
2. расширеные фильтры
3. скрытие полосы с фильтрами в дефолтном состоянии фильтра


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


  ![](https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/b5f8f9b81dba1fadbaca07d7069533e2.gif)
</details>

# Используемый стек

<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" width="50"> <img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/68747470733a2f2f616c6c7572657265706f72742e6f72672f7075626c69632f696d672f616c6c7572652d7265706f72742e737667.svg" width="50">
<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/68747470733a2f2f63646e2d69636f6e732d706e672e666c617469636f6e2e636f6d2f3531322f323131312f323131313634362e706e67.png" width="50">
<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/file-type-python.svg" width="50">
<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/jenkins-original.186x256.png" width="50">
<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/pytest.svg" width="50">
<img src="https://github.com/chaenkova/yasno_for_qa_guru/blob/main/images/selenium.svg" width="50">



