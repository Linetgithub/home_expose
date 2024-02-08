from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for houses (you can replace this with a database)
houses = [
    {"id": 1, "title": "Beautiful House", "description": "Lorem ipsum...", "price": 5000000},
    {"id": 2, "title": "Cozy Cottage", "description": "Lorem ipsum...", "price": 7500000},
    {"id": 3, "title": "Spacious Villa", "description": "Lorem ipsum...", "price": 2000000},
]

@app.route('/')
def index():
    return render_template('index.html', houses=houses)

@app.route('/house/<int:id>')
def house(id):
    house = next((house for house in houses if house['id'] == id), None)
    if house:
        return render_template('house.html', house=house)
    else:
        return "House not found", 404

@app.route('/add_house', methods=['GET', 'POST'])
def add_house():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        # Add the new house to the list (you can save it to a database instead)
        new_house = {"id": len(houses) + 1, "title": title, "description": description, "price": int(price)}
        houses.append(new_house)
        return redirect(url_for('index'))
    return render_template('add_house.html')

if __name__ == '__main__':
    app.run(debug=True)

