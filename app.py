from flask import Flask, render_template, request

app = Flask(__name__)

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para obtener categoría, dietas e imagen
def obtener_resultado(imc):
    if imc < 18.5:
        categoria = "Por debajo de lo normal"
        dietas = ["Dieta alta en calorías", "Suplementos vitamínicos", "Aumento de carbohidratos"]
        imagen = "static/images/bajo_peso.png"
    elif 18.5 <= imc <= 24.9:
        categoria = "Saludable"
        dietas = ["Dieta balanceada", "Mantén una actividad física regular", "Comer frutas y verduras"]
        imagen = "static/images/saludable.png"
    elif 25 <= imc <= 29.9:
        categoria = "Sobrepeso"
        dietas = ["Reducir azúcares y grasas", "Incrementar actividad física", "Alimentos ricos en fibra"]
        imagen = "static/images/sobrepeso.png"
    elif 30 <= imc <= 34.9:
        categoria = "Obesidad I"
        dietas = ["Dieta baja en calorías", "Evitar bebidas azucaradas", "Ejercicio regular"]
        imagen = "static/images/obesidad1.png"
    elif 35 <= imc <= 39.9:
        categoria = "Obesidad II"
        dietas = ["Dieta controlada por un nutricionista", "Evitar comidas rápidas", "Actividades físicas diarias"]
        imagen = "static/images/obesidad2.png"
    else:
        categoria = "Obesidad III"
        dietas = ["Tratamiento médico supervisado", "Baja en carbohidratos", "Ejercicio supervisado"]
        imagen = "static/images/obesidad3.png"
    
    return categoria, dietas, imagen

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura']) / 100  # Convertir a metros
    imc = calcular_imc(peso, altura)
    categoria, dietas, imagen = obtener_resultado(imc)
    
    return render_template('result.html', imc=imc, categoria=categoria, dietas=dietas, imagen=imagen)

if __name__ == '__main__':
    app.run(debug=True)
