import sqlite3
import webbrowser

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Функция для выполнения запросов к базе данных с параметрами
def execute_query(column=None, operation=None, value=None):
    connection = sqlite3.connect('materials.db')
    cursor = connection.cursor()

    # Формируем SQL-запрос в зависимости от наличия параметров
    if column and operation and value:
        query = f"SELECT id, compound FROM Materials WHERE {column} {operation} ?"
        cursor.execute(query, (value,))
    else:
        query = "SELECT ID, compound FROM Materials"
        cursor.execute(query)

    results = cursor.fetchall()
    connection.close()
    return results


# Маршрут для отображения всех записей
@app.route('/')
def index():
    search_query = request.args.get('search', default='')  # Получаем значение параметра 'search' из запроса

    if search_query:
        # Если введен поисковый запрос, выполняем поиск
        search_params = search_query.split()
        if len(search_params) == 3:
            # Проверяем, что введены все три параметра для поиска
            column, operation, value = search_params
            results = execute_query(column, operation, value)
        else:
            return "Неверное количество параметров для поиска"
    else:
        # Иначе, выводим все записи
        results = execute_query()

    return render_template('index.html', results=results, search_query=search_query)


# Маршрут для отображения деталей элемента
@app.route('/details/<int:id>')
def details(id):
    search_query = request.args.get('search', default='')

    connection = sqlite3.connect('materials.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Materials WHERE ID=?", (id,))
    result = cursor.fetchone()
    connection.close()

    if result:
        return render_template('details.html', result=result, search_query=search_query)
    else:
        return "Элемент не найден"


if __name__ == '__main__':
    # Определите порт, на котором будет запущен Flask
    port = 5000  # Вы можете выбрать любой доступный порт

    # Строка с адресом запуска Flask приложения
    url = f"http://127.0.0.1:{port}/"

    # Открывает браузер по умолчанию с указанным URL-адресом
    webbrowser.open(url)

    # Запускает Flask приложение на указанном порту
    app.run(debug=True, port=port)