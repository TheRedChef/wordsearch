from app import app

@app.route('/')
@app.route('/index')
def index():
	return app.send_static_file('index.html')
	
@app.route('/animals')
def animals():
	return app.send_static_file('animals.html')

@app.route('/candy')
def candy():
	return app.send_static_file('candy.html')
	
@app.route('/monsters')
def monsters():
	return app.send_static_file('monsters.html')

@app.route('/movies')
def movies():
	return app.send_static_file('movies.html')

@app.route('/villains')
def villains():
	return app.send_static_file('villains.html')