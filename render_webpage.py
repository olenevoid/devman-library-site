from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from os import path, makedirs
import json
from more_itertools import chunked


TEMPLATES_FOLDER = 'templates'
HTML_FOLDER = '.'
STATIC = 'static'
MEDIA = 'media'
NUMBER_OF_COLUMNS = 2
ITEMS_ON_PAGE = 10
PAGES_FOLDER = 'pages'


def load_books():
    filepath = f'{MEDIA}/meta_data.json'
    with open(filepath, 'r', encoding='utf-8') as file:
        books = json.loads(file.read())
        pages_of_books = chunked(books, ITEMS_ON_PAGE)

        return [chunked(page, NUMBER_OF_COLUMNS) for page in pages_of_books]


def rebuild():
    jinja_environment = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    books = load_books()

    template = jinja_environment.get_template(
        path.join(TEMPLATES_FOLDER, 'index.html')
    )

    makedirs(PAGES_FOLDER, exist_ok=True)

    for number, page in enumerate(books, start=1):
        rendered_page = template.render(
            books=page,
            media=MEDIA,
            static=STATIC
        )

        with open(f'{PAGES_FOLDER}/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


def main():
    books = load_books()
    print(books)
    rebuild()

    server = Server()

    server.watch(f'{TEMPLATES_FOLDER}/*.html', rebuild)

    server.watch(STATIC)

    server.serve(root=HTML_FOLDER)


if __name__ == '__main__':
    main()
