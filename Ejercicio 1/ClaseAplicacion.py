import tkinter as tk
class Aplicacion(tk.Tk):
   def __init__(self):
      self.__datos = []
      super().__init__()
      self.title("Calculadora")
      self.geometry("400x400")
     
      Item = tk.Label(self, text="Item")
      Cantidad = tk.Label(self, text="Cantidad")
      Precio_Año_Base = tk.Label(self, text="Precio Año Base")
      Precio_año_Actual = tk.Label(self, text="Precio Año Actual")
     
      opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
     
      Item.grid(row=0, column=0, **opts)
      Cantidad.grid(row=0, column=1, **opts)
      Precio_Año_Base.grid(row=0, column=2, **opts)
      Precio_año_Actual.grid(row=0, column=3, **opts)
      
      Vestimenta= tk.Label(self, text="Vestimenta")
      Alimentos=  tk.Label(self, text="Alimentos")
      Educacion= tk.Label(self, text="Educación")
      
      Vestimenta.grid(row=1, column=0, **opts)
      Alimentos.grid(row=2, column=0, **opts)
      Educacion.grid(row=3, column=0, **opts)
      for i in range(0, 3):
         filas=[]
         for j in range(0,3):
            dato = tk.DoubleVar()
            ingresar = tk.Entry(textvariable = dato)
            ingresar.grid(row = i + 1, column = j + 1, **opts)
            filas.append(dato)
         self.__datos.append(filas)
            
      Atributos_de_botones = {"width":9, "height":1}
      
      CalcularIPC=tk.Button(self, text = "Calcular IPC", **Atributos_de_botones, command=self.Calcular)
      CalcularIPC.grid( row=5, column=1)
      
      Salir=tk.Button(self, text = "Salir", **Atributos_de_botones, command=self.Salir)
      Salir.grid( row=5, column=2)
      self.mainloop()
   
   def Calcular(self):
      attributos = {"padx": 5, "pady": 5,"ipadx":10, "ipady": 10}
      dato_Actual = 0
      dato_Base = 0
      band = True
      for i in self.__datos:
         for dato in i:
                if band:
                    multiplicador = dato.get()
                    band = False
                elif i.index(dato) == 1:
                    dato_Base += dato.get() * multiplicador
                else:
                    dato_Actual += dato.get() * multiplicador
         band = True
      resultado = tk.Label(self, text = "IPC " + str(int(dato_Base)*100) + " % " + str(int(dato_Actual)*100) + " % ")
      resultado.grid(row = 6, column = 1, **attributos)
   
   def Salir(self):
      self.destroy()
      
      
   
     