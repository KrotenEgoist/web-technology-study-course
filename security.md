# Обеспечение безопасности своего сервиса

#### Большое количество запросов к api vk

Так как вк ограничивает большое количество запросов на своей стороне можно:
* Запустить больше ботов воркеров:
  1. Использовать для них мобильные прокси.
  2. Распределять все запросы пользователей между ними.
* Ограничивать количество запросов пользователей:
  1. Ограничивать количество запросов по времени.
  2. Блокировать ip адреса с подозрительной активностью запросов.
  3. Распределять запросы в очередь, чтобы распределить нагрузку по времени.
  4. Отключать сервис во избежание блокировок своих ботов сайта.
* Переложить запросы к api vk на пользователей:
  1. Просить пользователей авторизоваться через oauth.
  2. Запросить нужные разрешения на просмотр картинок.
  3. Формировать запросы к вк уже от имени пользователей.
* Периодически пропускать запросы к вк:
  1. Сохранять некоторое количество ссылок на картинки из альбомов в redis.
  2. С некоторой случайной периодичность, если пользователь хочет получить
   картинку из того же альбома, выдавать им картинки.
   из redis, тем самым минуя запросы к вк, создавая иллюзию случайного повтора
   картинки.

#### Запрос к приватной информации

1. Не выдавать доступ к приватным альбомам.
2. Проверять альбом на общедоступность.

#### DDoS

1. Переложить защиту на хостинг (Хостинг где расположен этот учебный сайт предлагает
  от защиту 0.5 Мбит/с до 20 Мбит/с).
2. Отключить доступ к сервису, если атака прошла.

#### XSS

1. Проверка вводимые данные в формы, исключать или удалять через регулярные выражения html теги.
2. Проверка, что введенные данные являются числами.

---

# Обеспечение безопасности сайта vk.com

#### Фишинг

1. Уникальный дизайн сайта.
2. Скупка фишинговых доменов, перенаправление с них на оф. сайт.
3. Обучение пользователей.
4. Сохранять в базе фишинговые сайты по жалобе пользователей.

#### Борьба с ботами

1. Ограничивать доступ к методам, например количество постов, сообщений в секунду.
2. Капчи.
3. Блокировка пользователей с подозрительной активностью.
4. Блокировка по ip, подсетям.
5. Система репортов.
<br>
(вообще от ботов сложно избавиться, но какие-то простые методы лучше применить, чем просто ничего не делать).

#### Взлом страниц пользователей

1. Замораживать взломанных пользователей, по подозрительной активности или жалобам пользователей.
2. Актуализировать данные пользователей для восстановления доступа к страницам.
3. Просить пользователей менять пароли.
4. Проверять задаваемые пароли на "сложность", исключать "легкие пароли" или пароли из баз.

#### Уязвимости в методах api

1. В вк есть система тестировщиков, которые репортуют о проблемах в отчетах. Им может любой достаточно знающий пользователь.
2. Обновление версий api, не поддерживать устаревшие и уязвимые методы.
3. Настроить CORS заголовки.
4. Возможность удалять токен доступа и настройка его разрешений, если токен угнали злоумышленники.
5. Настроить время жизни токена.