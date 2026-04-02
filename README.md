# Библиотека

Каталог книг с постраничной навигацией на Bootstrap.

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

После генерации откройте `index.html` в браузере — откроется первая страница каталога.

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
