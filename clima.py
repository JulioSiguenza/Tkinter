
from inspect import Parameter
from tkinter import *
from unicodedata import name
from urllib import request, response
from pip import main
import requests


#c2b3308a1ce68941067eda5add75f4df
#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def mostrar_clima(clima):
    try:
  
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp))+ "C°"
        descripcion["text"] = desc
    except:
        ciudad["text"]= "ha ocurrido un error, intentalo nuevamente"






def clima_json(ciudad):
    try:
        API_key="c2b3308a1ce68941067eda5add75f4df"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q":ciudad , "units":"metric", "lang": "es" }
        response = requests.get (URL,params= parametros)
        clima = response.json()
        #print(response.json())
        mostrar_clima(clima)

    except:
        print("error")


    
    print(clima["name"])
    print(clima["weather"][0]["description"])
    print(clima["main"]["temp"])



ventana = Tk()
ventana.geometry("350x550")
texto_ciudad = Entry(ventana, font = ("courier", 20, "normal"), justify=CENTER)
texto_ciudad.pack(padx=30 , pady=30)
obtener_clima = Button(ventana, text="Obtener Clima", font = ("courier", 20, "normal"), command=lambda: clima_json(texto_ciudad.get()))
obtener_clima.pack(padx=10 , pady=10)

#Etiquetas a mostrar del clima
ciudad = Label( font = ("courier", 20, "normal") )
ciudad.pack(padx=30 , pady=30)

temperatura = Label(  font = ("courier", 50, "normal") )
temperatura.pack(padx=30 , pady=30)

descripcion = Label(  font = ("courier", 20, "normal") )
descripcion.pack(padx=30 , pady=30)

ventana.mainloop()

 