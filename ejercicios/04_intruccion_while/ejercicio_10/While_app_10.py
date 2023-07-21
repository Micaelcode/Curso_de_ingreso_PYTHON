import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
micael
fernandez


Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        positivos=0
        negativos=0
        cant_positivos=0
        cant_negativos=0
        cant_ceros=0
        
        
        
        
        
        while (True):
            numero=prompt("utn","Ingresa numeros")
            if numero==None:
                break
            else:
                numero=int(numero)
                if numero >0:
                    positivos+=numero
                    cant_positivos=cant_positivos+1
                elif numero <0:
                    negativos+=numero
                    cant_negativos=cant_negativos+1
                elif numero==0:
                    cant_ceros+=1
        diferencia= cant_positivos-cant_negativos     
                    
                    
        alert("UTN",f"Los positivos son ingresados son {positivos}, los negativos ingresados son {negativos},la cantidad de positivos ingresados son {cant_positivos}, la cantidad de negativos ingresados son {cant_negativos}, la cantidad de ceros son {cant_ceros} y el diferencia es {diferencia} ")           
        
        
        
        
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
