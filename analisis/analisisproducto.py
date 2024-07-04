from generators.generatorsproductos import generarProductos
import pandas as pd
 
def analizarDatos():
    datos=generarProductos()
    tabla=pd.DataFrame(datos,columns=["categoria","Tipo Producto"])
    tabla.to_csv("./data/tablaproductoApple.csv",index=False)
analizarDatos()
 