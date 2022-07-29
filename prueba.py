#Crearemos un proxy para el siguiente de roblox: https://inventory.roblox.com/v2/users/2847919347/inventory/13?sortOrder=Desc&limit=100 
#En python, para utilizarlo desde roblox


#Importamos las librerias necesarias
import requests
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

#Sera con get, y el query podra ser el Orden, el limite, y el userid
@app.route("/", methods=["GET"])
def get_inventory():
    #Obtenemos los parametros
    user_id = request.args.get("user_id")
    limit = request.args.get("limit")
    sort_order = request.args.get("sort_order")

    #Creamos la url
    url = f"https://inventory.roblox.com/v2/users/{user_id}/inventory/13?sortOrder={sort_order}&limit={limit}"

    #Hacemos la peticion
    response = requests.get(url)

    #Retornamos la respuesta
    return jsonify(response.json())

#Ejecutamos el servidor
app.run()