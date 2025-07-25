from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data
users = {'admin': 'admin'}
books = []  # List of dicts: {title, author, year}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error="Invalid username or password")
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error="Username already exists")
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book = {
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        books.append(book)
        return redirect(url_for('view_books'))
    return render_template('add_book.html')

@app.route('/books')
def view_books():
    return render_template('view_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
