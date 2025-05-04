from flask import Flask
from flask_cors import CORS
from adelitas import adelitas_bp

app = Flask(__name__)
CORS(app)

# Registrar las Adelitas
app.register_blueprint(adelitas_bp, url_prefix='/adelita')

@app.route('/')
def raiz():
    return {
        "estado": "Imperio operativo - Fase Adelita",
        "gpts_activos": [f"Adelita-{i:02d}" for i in range(3, 28)],
        "modo": "clonado-simbólico",
        "mensaje": "Servidor funcional con múltiples Adelitas"
    }

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
