<h2>1 - Запуск локальной версии проекта</h2>
<p>1.1 - Скопировать к себе удаленный репозиторий: git clone</p>
<p>1.2 - Установить все необходимые библиотеки: pip install -r requirements.txt</p>
<p>1.3 - Добавить файл .env с следующим:</p>
<small>NAME_PSQL = Название базы данных</small><br>
<small>USER_PSQL = Пользователь</small><br>
<small>PASSWORD_PSQL = Пароль</small><br>
<small>HOST_PSQL = Хост</small><br>
<small>PORT_PSQL = Порт</small><br>
<p>1.4 - Провести миграции: python manage.py migrate</p>
<p>1.5 - Запустить локальную версию сервиса: python manage.py runserver<p>
  <hr>

<h2>2 - Работа с api</h2>

<br><h4>2.1 - Добавить новый товар:</h4>
<p>POST /api/v1/electronics/</p>
<p>Параметры:</p>
<p>"name" - название товара, тип char ( обязательный )</p>
<p>"price" - стоимость товара, тип decimal ( обязательный )</p>
<p>"category" - категория товара, тип pk ( обязательный )</p>
<p>"manufacturer" - производитель товара, тип pk ( обязательный )</p>
<p>"quantity" - кол-во товара, тип int ( не обязательный )</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/</p>
<p>Тело запроса формата json:</p>
<p>


    {
        "name": "Цифровое фортепиано CASIO CDP-S100BK",
        "price": "1750",
        "category": 2,
        "manufacturer": 4,
        "quantity":7
    }

</p>
<p>Ответ от сервера:</p>
<p>status 201 - товар добавлен</p>
<p>status 400 - неправильный запрос (см код ошибки в теле ответа)</p>
<p>

    {
        "id": 1,
        "gross_cost": 12250.0,
        "code": "vcPicSU3",
        "name": "Цифровое фортепиано CASIO CDP-S100BK",
        "price": "1750.00",
        "quantity": 7,
        "update_date": "2021-09-04",
        "category": 2,
        "manufacturer": 4
    }

<p>id - Первычный ключ товара</p>
<p>gross_cost - отражает общую стоимость данного товара</p>
<p>update_date - дата создания товара, дата обновляется при добавлении товара на склад</p>

<br><h4>2.2 - Вывести список всей электроники:</h4>
<p>GET /api/v1/electronics/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/</p>

<p>Ответ от сервера:</p>
<p>status 200 - OK</p>


    {
        "id": 1,
        "gross_cost": 100000.0,
        "code": "dcq80f8G",
        "name": "Цифровое фортепиано CASIO CDP-S100BK",
        "price": "5000.00",
        "quantity": 20,
        "update_date": "2021-09-04",
        "category": 2,
        "manufacturer": 4
    },
    {
        "id": 5,
        "gross_cost": 0.0,
        "code": "dgc7MjyB",
        "name": "Наушники SENNHEISER HD",
        "price": "1750.00",
        "quantity": 0,
        "update_date": "2021-09-04",
        "category": 1,
        "manufacturer": 1
    },


<br><h4>2.3 - Вывести конкретный товар:</h4>
<p>GET /api/v1/electronics/&lt;id&gt;/</p>
<p>id - уникальный идентификатор товара</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/28/</p>
<p>Ответ от сервера:</p>
<p>status 200 - Ok</p>
<p>status 404 -  Not Found (Не найдено таких объектов)</p>

    {
        "id": 28,
        "gross_cost": 60000.0,
        "code": "vcPicSU3",
        "name": "Цифровое фортепиано CASIO",
        "price": "3000.00",
        "quantity": 20,
        "update_date": "2021-09-05",
        "category": 1,
        "manufacturer": 1
    }

<br><h4>2.4 - Изменить товар:</h4>
<p>PUT /api/v1/electronics/&lt;id&gt;/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/28/</p>
<p>Тело запроса формата json:</p>
<p>

    {
        "name": "Цифровое фортепиано CASIO",
        "price": "3000.00",
        "category": 1,
        "manufacturer": 1
    }

</p>
<p>Ответ от сервера:</p>
<p>status 200 - товар изменен</p>
<p>status 400 - неправильный запрос (см код ошибки в теле ответа)</p>
<p>status 404 - Not Found (Не найдено таких объектов)</p>

<br><h4>2.5 - Частично изменить товар:</h4>
<p>PATH /api/v1/electronics/&lt;id&gt;/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/28/</p>
<p>Тело запроса формата json:</p>
<p>

    {
        "quantity": 20,
    }
</p>
<p>Ответ от сервера:</p>
<p>status 200 - товар изменен</p>
<p>status 400 - неправильный запрос (см код ошибки в теле ответа)</p>
<p>status 404 - Not Found (Не найдено таких объектов)</p>

<br><h4>2.6 - Удалить товар:</h4>
<p>DELETE /api/v1/electronics/&lt;id&gt;/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/28/</p>

<p>Ответ от сервера:</p>
<p>status 204 - товар удален</p>
<p>status 404 - Not Found (Не найдено таких объектов)</p>


<br><h4>2.7 - Вывести список всех товаров данного типа или данного производителя</h4>
<p>GET /api/v1/electronics/</p>
<p>В get параметры необходимо передать type='уникальный идентификатор ( id ) типа' или manufacturer='уникальный идентификатор ( id ) бренда'</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/?manufacturer=2</p>
<p>Ответ от сервера:</p>
<p>status 200 - Ok</p>


<br><h4>2.8 - Показать сумму всех товаров на складе</h4>
<p>GET /api/v1/electronics/summary/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/summary/</p>
<p>Ответ от сервера:</p>
<p>status 200 - Ok</p>

    {
        "total_cost": 1381329.0
    }


<br><h4>2.8 - Показать сумму всех товаров данного типа или бренда</h4>
<p>GET /api/v1/electronics/summary/</p>
<p>В get параметры необходимо передать type='уникальный идентификатор ( id ) типа' или manufacturer='уникальный идентификатор ( id ) бренда'</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/summary/?type=2</p>
<p>Ответ от сервера:</p>
<p>status 200 - Ok</p>

    {
        "total_cost": 1161329.0
    }

<br><h4>2.9 - Найти товар по "code":</h4>
<p>GET /api/v1/electronics/code/&lt;code&gt;/</p>
<p>Пример запроса:</p>
<p>http://127.0.0.1:8000/api/v1/electronics/code/zaWpVRlF</p>
<p>Ответ от сервера:</p>
<p>status 200 - Ok</p>
<p>status 404 -  Not Found (Не найдено таких объектов)</p>

<br><h4>2.10 - Категория товара ( тип ) CRUD операции:</h4>
<p>Категория имеет: id - уникальный идентификатор, name - название категории</p>
<p>Добавить категорию: POST /api/v1/categories/ </p>
<p>Список всех категорий: GET /api/v1/categories/</p>
<p>Для следующих методов, необходимо в url передать уникальный идентификатор ( id )</p>
<p>Конкретная категория:GET api/v1/categories/&lt;id&gt;/</p>
<p>Изменение категории:PUT api/v1/categories/&lt;id&gt;/</p>
<p>Частичное изменение категории:PATH api/v1/categories/&lt;id&gt;/</p>
<p>Удаление категории:DELETE api/v1/categories/&lt;id&gt;/</p>


<br><h4>2.11 - Производитель товара CRUD операции:</h4>
<p>Производитель имеет: id - уникальный идентификатор, name - название производителя</p>
<p>Добавить категорию: POST /api/v1/manufacturers/ </p>
<p>Список всех категорий: GET /api/v1/manufacturers/</p>
<p>Для следующих методов, необходимо в url передать уникальный идентификатор ( id )</p>
<p>Конкретная категория:GET api/v1/manufacturers/&lt;id&gt;/</p>
<p>Изменение категории:PUT api/v1/manufacturers/&lt;id&gt;/</p>
<p>Частичное изменение категории:PATH api/v1/manufacturers/&lt;id&gt;/</p>
<p>Удаление категории:DELETE api/v1/manufacturers/&lt;id&gt;/</p>