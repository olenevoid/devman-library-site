from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from os import path
import json
from more_itertools import chunked


TEMPLATES_FOLDER = 'templates'
HTML_FOLDER = '.'
STATIC = 'static'
BOOKS_ROOT = 'books'
NUMBER_OF_COLUMNS = 2


def load_books():
    filepath = 'books/meta_data.json'
    with open(filepath, 'r', encoding='utf-8') as file:
        books = json.loads(file.read())

        return chunked(books, NUMBER_OF_COLUMNS)


def rebuild():
    jinja_environment = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = jinja_environment.get_template(
        path.join(TEMPLATES_FOLDER, 'index.html')
    )

    rendered_page = template.render(
        books=load_books(),
        books_root=BOOKS_ROOT,
        static=STATIC
    )

    with open(f'{HTML_FOLDER}/index.html', 'w', encoding="utf8") as file:
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
