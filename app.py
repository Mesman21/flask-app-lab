from flask import Flask, render_template

# Ініціалізація додатку
app = Flask(__name__)

# Маршрут для сторінки Резюме (головна сторінка)
@app.route('/')
def resume():
    # Рендеримо resume.html і передаємо динамічний заголовок
    return render_template('resume.html', title='Резюме | Лабораторна №2')

# Маршрут для сторінки Контакти
@app.route('/contacts')
def contacts():
    # Рендеримо contacts.html і передаємо динамічний заголовок
    return render_template('contacts.html', title='Контакти')

# Запуск локально
if __name__ == '__main__':
    # Використовуйте налаштування з .flaskenv
    app.run()