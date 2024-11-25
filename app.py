from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/home')
def home():
    return """
    <html>
        <body>
            <h1>Witamy na stronie głównej!</h1>
            <p>Testujemy Flaska, tak tak backend</p>
        </body>
    </html>
    """
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/image")
def image():
    return """
    <html>
        <body>
            <h1> Obrazek </h1> 
            <img src = "https://www.skalnik.pl/blog/wp-content/uploads/2023/01/AdobeStock_116059788-scaled.jpeg" style="width: 400px; height: 400px;">
            <p> Tutaj jest obrazek </p> 
        </body>
    </html>
    """

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return 'Uzyto metody POST.'
    else: 
        return 'Uzyto metody GET.'

#Podzielność
@app.route('/number/<int:number>')
def check(number):
    if number % 2 == 0:
        return "liczba podzielna przez 2"
    elif number % 3 == 0:
        return "liczba podzielna przez 3"
    elif number % 5 == 0:
        return "liczba podzielna przez 5"
    else:
        return "liczba nie jest podzielna przez 2, 3 lub 5"
    
#Sortowanie
@app.route('/sort/<items>')
def sort_items(items):
    items_list = items.split(',')
    sorted_items = sorted(items_list)
    return f'Kolejność alfabetyczna: {",".join(sorted_items)}'


#Imie
@app.route('/about/<name>')
def about(name):
    return render_template('about.html', name=name)

#Formularz
@app.route('/form', methods=['GET', 'POST'])
def show_form():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        return render_template('result.html', name=name, surname=surname, age=age)
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    surname = request.form['surname']
    age = request.form['age']
    return render_template('result.html', name=name, surname=surname, age=age)

#API
@app.route('/api')
def yesorno():
    # Wysyłanie zapytania do API
    response = requests.get('https://yesno.wtf/api')
    data = response.json()
    
    # Wyciągnięcie odpowiedzi
    answer = data['answer']
    
    # Zwrócenie odpowiedzi na stronie
    if answer == 'yes':
        return render_template('yesno.html', answer='YES', color='green')
    else:
        return render_template('yesno.html', answer='NO', color='red')

