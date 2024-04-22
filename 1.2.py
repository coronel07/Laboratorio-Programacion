personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 22}
]

for diccionario in personas:
    for clave, valor in diccionario.items():
        print(clave + ":", valor)
    print()  
