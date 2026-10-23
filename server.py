from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Inicio', mensaje='Bienvenido a la Biblioteca Universitaria'
    )

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo='Catálogo', mensaje='Consulta los materiales disponibles en nuestra biblioteca')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Conoce los servicios que ofrecemos a nuestra comunidad universitaria')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Encuentra nuestros medios de contacto y horarios de atención')

if __name__ == '__main__':
    app.run(debug=True)