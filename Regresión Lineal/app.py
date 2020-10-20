import time, json
from flask import Flask, render_template, request
from regresion import information

# Instancia de Flask. Aplicación
app = Flask(__name__)

information = information()
# Se crea la ruta a home
@app.route('/home')
def template():
 # templates/form.html
 return render_template("index.html")

# Definimos el route con el método GET
@app.route('/informacion',methods=['GET'])
def datos():
 # Retornamos la respuesta
 time.sleep(1)
 data_string = json.dumps(information[1])
 decoded = json.loads(data_string)
 precision0 = str(decoded["0"]["precision"])
 precision1 = str(decoded["1"]["precision"])
 return "<h1>El valor obtenido para el score de presición es </h1>" + "<h3>"+str(information[0])+"</h3>" + "<h1>El resumen de la información es: </h1>"+ "<h3> La presición para 0 es "+precision0+"</h3>" + "<h3> La presición para 1 es "+precision1+"</h3>" 


if __name__ == '__main__':
 # Iniciamos la apicación en modo debug
 app.run(debug=True)
