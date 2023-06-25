import tkinter as tk
class Aplicacion(tk.Tk):
   def __init__(self):
       
      super().__init__()
      self.__dolar = tk.StringVar()
      self.__pesos = tk.StringVar()
      self.title("Corversor de moneda")
      self.geometry("300x400")
      opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
      
      Dolar_entry= tk.Entry(self, textvariable = self.__dolar)
      Dolar_entry.grid(row=0, column=2, **opts)
      
      dolares=tk.Label(self, text="Dolares")
      dolares.grid(row=0, column=4, **opts)
      
      equivalente=tk.Label(self, text="es equivalente a" )
      equivalente.grid(row=3, column=0, **opts)
      
      pesos=tk.Label(self, text="Pesos")
      pesos.grid(row=3, column=4, **opts)
      
      Atributos_de_botones = {"width":9, "height":1}
      
      Calcular=tk.Button(self,text="Calcular", **Atributos_de_botones, command=calcular)
      Calcular.grid(row=6 ,column=0, **opts)
      
      Salir=tk.Button(self, text = "Salir", **Atributos_de_botones, command=self.Salir)
      Salir.grid( row=5, column=2)
      
      
   
   def calcular(self):
      
   
   def Salir(self):
      self.destroy()
      

      
      
      
      
      
      
      
      self.mainloop()