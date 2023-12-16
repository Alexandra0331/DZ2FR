#Задание №6
#Создать страницу, на которой будет форма для ввода имени
#и возраста пользователя и кнопка "Отправить"
#При нажатии на кнопку будет произведена проверка
#возраста и переход на страницу с результатом или на
#страницу с ошибкой в случае некорректного возраста.







from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('form6.html')


@app.post('/')
def index_post():
    name = request.form.get('input')
    age = int(request.form.get('age'))

    if age >= 18:
        result = "Можно"
    else:
        result = 'Нельзя'

    return render_template('form6.html', text=age, result=result)

if __name__ == '__main__':
    app.run(debug=True)