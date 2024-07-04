import random
 
def generarProductos():
    productos=["Musica","TV","APP","PC","Cel","tablets","Accesorios"]
    datos=[]
    for producto in productos:
        responsable={}
        categoria=random.choice(["plus",'Mega','Basico'])
        responsable=[categoria,producto]
        datos.append(responsable)
    return datos
print(generarProductos())