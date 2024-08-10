import pandas as pd


#DATAFRAME es la informacion basica con el nombre dfe las piezas y centimentros para poder armae el excel

#1.DICCIONARIO
data = {
    "Piezas:" : ["Pata", "Tablero", "Puertas", "Estante", "Panel Lateral"],
    "Centimetros:":[40,120,60,30,180]
}

#2.DATAFRAME
df = pd.DataFrame(data)

#Guarda data en archivo excel
try:
    df.to_excel("Muebles_Medidas.xlsx", index=False)
    print("Archivo guardado con éxito.")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")