# Библиотека

Каталог книг с постраничной навигацией на Bootstrap.
<img width="1473" height="1126" alt="image" src="https://github.com/user-attachments/assets/310ed9e5-1979-48f4-9834-35302737d588" />

## Демо

[Открыть библиотеку](https://olenevoid.github.io/devman-library-site)

## Возможности

- Каталог книг с обложками, жанрами и ссылками на чтение
- Постраничная навигация по каталогу
- Адаптивная вёрстка

## Запуск

Требуется Python 3.12+.

```bash
pip install -r requirements.txt
python render_webpage.py
```

После генерации перейдите по адресу [127.0.0.1:5500](http://127.0.0.1:5500) в браузере — откроется первая страница каталога.

Для разработки с автоперезагрузкой:

```bash
python render_webpage.py
```

## Структура

```
media/          — книги и обложки
pages/          — сгенерированные HTML-страницы каталога
static/         — CSS и JS (Bootstrap, favicon)
templates/      — Jinja2 шаблоны
render_webpage.py — генерация страниц
index.html      — редирект на pages/index1.html
```

## Технологии

- Python, Jinja2, Bootstrap 5, LiveReload
