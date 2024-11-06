from flask import Flask
app = Flask(__name__)

@app.route('/<int:cifra>')
def factorial(cifra):
    resultado=1
    for i in range(1,cifra+1):
        resultado=resultado*i
    return str(resultado)

if __name__ == '__main__':
    app.run(debug=True)
