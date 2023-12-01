import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Функция для выполнения запросов к базе данных с параметрами
def execute_query(column, operation, value):
    connection = sqlite3.connect('materials.db')
    cursor = connection.cursor()

    # Формируем SQL-запрос с использованием параметров
    query = f"SELECT ID, FormulaUnit FROM Materials WHERE {column} {operation} ?"
    cursor.execute(query, (value,))

    results = cursor.fetchall()
    connection.close()
    return results


# Основной маршрут для отображения результатов
@app.route('/')
def index():
    results = execute_query("mag", "=", "1")
    return render_template('index.html', results=results)


# Маршрут для отображения деталей элемента
@app.route('/details/<int:id>')
def details(id):
    connection = sqlite3.connect('materials.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Materials WHERE ID=?", (id,))
    result = cursor.fetchone()
    connection.close()

    if result:
        return render_template('details.html', result=result)
    else:
        return "Элемент не найден"


if __name__ == '__main__':
    app.run(debug=True)
