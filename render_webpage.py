from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from os import path


TEMPLATES_FOLDER = 'templates'
HTML_FOLDER = 'rendered'
STATIC = 'static'


def rebuild():
    jinja_environment = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = jinja_environment.get_template(
        path.join(TEMPLATES_FOLDER, 'index.html')
    )

    rendered_page = template.render(
        books=[{'book1':'book path'}],
        static=STATIC
    )

    with open(f'{HTML_FOLDER}/index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    rebuild()

    server = Server()

    server.watch(f'{TEMPLATES_FOLDER}/*.html', rebuild)

    server.watch(f'{STATIC}/*.css')

    server.serve(root=HTML_FOLDER)


if __name__ == '__main__':
    main()
