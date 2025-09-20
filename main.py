from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculodecompras', methods=['GET', 'POST'])
def calculodecompras():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        # Calcular descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento
        total_descuento = total_sin_descuento - total_con_descuento

        return render_template(
            'calculodecompras.html',
            nombre=nombre,
            edad=edad,
            cantidad=cantidad,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento,
            total_descuento=total_descuento
        )
    return render_template('calculodecompras.html')

@app.route('/iniciodesesion', methods=['GET', 'POST'])
def iniciodesesion():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    mensaje = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        # Validar credenciales
        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = f"Bienvenido Administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."
        return render_template('iniciodesesion.html',
                                   mensaje=mensaje, usuarios=usuarios, password=password,usuario=usuario
                                   )
    return render_template('iniciodesesion.html')

if __name__ == '__main__':
    app.run(debug=True)