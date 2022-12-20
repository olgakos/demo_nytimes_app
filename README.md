# demo_nytimes_app
Some mobile tests to New York Times App

Мобильное приложенеи взято из публичного источника: https://nytimes.en.uptodown.com/android
Возможности приложения описаны здесь: https://help.nytimes.com/hc/en-us/articles/115015970768-Android-News-App

Дженкинс: https://jenkins.autotests.cloud/job/C02_OlgaKos_python_newyorktimes_app_test/

Тест 1: 
1. Открыть приложение app
2. Клик на иконку "Профиль"
3. Клик на Theme
4. Клик на Dark

Тест 2: 
1. Открыть приложение app
2. Клик на иконку Sections
2. Клик на иконку "Лупа"   
3. Найти строку поиcка
4. Впечатать: "harry potter"
5. Нажать кнопку `Go`   
6. Проверить, что выдача содержить текст "Tom Felton"

Сборка в Дженкинс: https://jenkins.autotests.cloud/job/C02_OlgaKos_python_newyorktimes_app_test/

BS: 
"userName" : "olga_ouHam9", "accessKey" : "iDs7wY8LzQqGhHiJ1369"

Токер приложения в BS bs://0e73cacaa99b3e3085b1aa1533521c6a24df4de0



