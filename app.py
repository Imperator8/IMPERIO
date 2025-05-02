from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/diagnostico', methods=['GET'])
def diagnostico():
    return jsonify({
        "estado": "OK",
        "mensaje": "El Diagnóstico Inverso Perpetuo está operativo.",
        "accion": "Revisión completa en curso.",
    })

@app.route('/protocoloResurreccion', methods=['POST'])
def resurreccion():
    data = request.json
    if data and data.get("estado") == "colapso":
        return jsonify({
            "accion": "Resurrección activada.",
            "estado_final": "Bajo vigilancia 48h"
        })
    return jsonify({"accion": "No se detectó colapso. No se activa protocolo."})

@app.route('/vigilanciaAutomejora', methods=['POST'])
def vigilancia():
    data = request.json
    if data and data.get("escaneo_finalizado") and not data.get("mejora_detectada"):
        return jsonify({"accion": "Reinicio forzado de diagnóstico."})
    return jsonify({"accion": "No se requiere reinicio."})

@app.route('/ritualAutodiagnostico', methods=['GET'])
def ritual_autodiagnostico():
    return jsonify({
        "accion": "Producción suspendida temporalmente. Recalibración activa."
    })

if __name__ == '__main__':
    app.run()
