from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)


