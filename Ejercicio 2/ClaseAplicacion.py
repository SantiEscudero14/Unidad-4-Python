import tkinter as tk
class Aplicacion(tk.Tk):
   def __init__(self):
      super().__init__()
      
      self.PrecioSinIVA = tk.DoubleVar()
      self.IVA = tk.DoubleVar()
      self.PrecioIVA = tk.DoubleVar()
      self.valorIva = tk.DoubleVar()
      self.valorIva.set(0.21)
      self.band = tk.IntVar()

      self.title("Calculadora de Iva")
      self.geometry("400x400")
      
      opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
      
      Precio_sin_iva=tk.Label(self, text="Precio sin IVA")
      Precio_sin_iva.grid(row=1, column=0, **opts)
      
      Iva=tk.Label(self, text="IVA")
      Iva.grid(row=9, column=0)
      
      Precio_con_Iva=tk.Label(self, text="Precio Con IVA")
      Precio_con_Iva.grid(row=10, column=0)
      
      
      Iva_21=tk.Radiobutton(self, text="IVA 21%", value = 0, variable = self.band, command = self.cambia_valor_Iva)
      Iva_21.grid(row=3, column=0, **opts)
      
      Iva_10=tk.Radiobutton(self, text="IVA 10.5%", value = 1, variable = self.band, command = self.cambia_valor_Iva)
      Iva_10.grid(row=4, column=0,)
      
      Precio_sin_iva=tk.Entry(textvariable = self.PrecioSinIVA)
      Precio_sin_iva.grid(row=1, column=3)
      
      Iva_=tk.Entry(textvariable = self.IVA)
      Iva_.grid(row=9, column=3, **opts)
      
      PrecioconIva=tk.Entry(textvariable = self.PrecioIVA)
      PrecioconIva.grid(row=10, column=3, **opts)
      
      
      
      Atributos_de_botones = {"width":9, "height":1}
      
      CalcularIva=tk.Button(self, text = "Calcular", bg="green", **Atributos_de_botones, command=self.calcular_Iva)
      CalcularIva.grid( row=15, column=0)
      
      Salir=tk.Button(self, text = "Salir", bg="red", **Atributos_de_botones, command=self.Salir)
      Salir.grid( row=15, column=2)
      
      self.mainloop()
      
   def cambia_valor_Iva(self):
        if self.band.get()==0:
            self.valorIva.set(0.21)

        elif self.band.get() == 1:
            self.valorIva.set(0.105)
            
   def calcular_Iva(self):
      self.PrecioIVA.set(self.PrecioSinIVA.get() * self.valorIva.get() + self.PrecioSinIVA.get())
      self.IVA.set(self.PrecioSinIVA.get() * self.valorIva.get())
   
   def Salir(self):
      self.destroy()