import tkinter as tk
from tkinter import messagebox
import math


# Clase para manejar la conversión de calificaciones
class Calificacion:
    def __init__(self, nota):
        self.nota = nota

    def convertir_a_literal(self):
        if 90 <= self.nota <= 100:
            return "A"
        elif 80 <= self.nota < 90:
            return "B"
        elif 70 <= self.nota < 80:
            return "C"
        elif 60 <= self.nota < 70:
            return "D"
        elif 0 <= self.nota < 60:
            return "F"
        else:
            return "Error: Calificación fuera de rango"


# Clase para manejar el ordenamiento de tres números
class OrdenarNumeros:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def ordenar(self):
        numeros = [self.num1, self.num2, self.num3]
        numeros.sort()
        return numeros


# Clase para manejar la conversión entre grados y radianes
class ConvertirGradosRadianes:
    @staticmethod
    def grados_a_radianes(grados):
        return math.radians(grados)

    @staticmethod
    def radianes_a_grados(radianes):
        return math.degrees(radianes)


# Clase para manejar la interfaz gráfica
class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Multifuncional")

        # Frame para elegir funcionalidad
        self.opcion_frame = tk.Frame(root)
        self.opcion_frame.grid(row=0, columnspan=3)

        # Botones para seleccionar funcionalidades
        tk.Button(self.opcion_frame, text="Convertir Calificación", command=self.mostrar_calificaciones).grid(row=0,
                                                                                                              column=0)
        tk.Button(self.opcion_frame, text="Ordenar Números", command=self.mostrar_ordenar_numeros).grid(row=0, column=1)
        tk.Button(self.opcion_frame, text="Convertir Grados/Radianes", command=self.mostrar_conversion).grid(row=0,
                                                                                                             column=2)

        # Frame para calificaciones
        self.calificaciones_frame = tk.Frame(root)
        tk.Label(self.calificaciones_frame, text="Introduce la calificación numérica:").grid(row=0, column=0)
        self.nota = tk.Entry(self.calificaciones_frame)
        self.nota.grid(row=0, column=1)
        tk.Button(self.calificaciones_frame, text="Convertir a Literal", command=self.convertir_calificacion).grid(
            row=1, columnspan=2)
        self.resultado_calificacion = tk.Label(self.calificaciones_frame, text="Calificación Literal: ")
        self.resultado_calificacion.grid(row=2, columnspan=2)

        # Frame para ordenar números
        self.ordenar_frame = tk.Frame(root)
        tk.Label(self.ordenar_frame, text="Introduce el primer número:").grid(row=0, column=0)
        tk.Label(self.ordenar_frame, text="Introduce el segundo número:").grid(row=1, column=0)
        tk.Label(self.ordenar_frame, text="Introduce el tercer número:").grid(row=2, column=0)
        self.num1 = tk.Entry(self.ordenar_frame)
        self.num2 = tk.Entry(self.ordenar_frame)
        self.num3 = tk.Entry(self.ordenar_frame)
        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)
        self.num3.grid(row=2, column=1)
        tk.Button(self.ordenar_frame, text="Ordenar", command=self.ordenar_numeros).grid(row=3, columnspan=2)
        self.resultado_orden = tk.Label(self.ordenar_frame, text="Números ordenados: ")
        self.resultado_orden.grid(row=4, columnspan=2)

        # Frame para conversión de grados y radianes
        self.conversion_frame = tk.Frame(root)
        tk.Label(self.conversion_frame, text="Introduce el valor:").grid(row=0, column=0)
        self.valor = tk.Entry(self.conversion_frame)
        self.valor.grid(row=0, column=1)
        tk.Button(self.conversion_frame, text="Convertir a Radianes", command=self.convertir_a_radianes).grid(row=1,
                                                                                                              column=0)
        tk.Button(self.conversion_frame, text="Convertir a Grados", command=self.convertir_a_grados).grid(row=1,
                                                                                                          column=1)
        self.resultado_conversion = tk.Label(self.conversion_frame, text="Resultado: ")
        self.resultado_conversion.grid(row=2, columnspan=2)

    def mostrar_calificaciones(self):
        self.ordenar_frame.grid_forget()
        self.conversion_frame.grid_forget()
        self.calificaciones_frame.grid(row=1, columnspan=2)

    def mostrar_ordenar_numeros(self):
        self.calificaciones_frame.grid_forget()
        self.conversion_frame.grid_forget()
        self.ordenar_frame.grid(row=1, columnspan=2)

    def mostrar_conversion(self):
        self.calificaciones_frame.grid_forget()
        self.ordenar_frame.grid_forget()
        self.conversion_frame.grid(row=1, columnspan=2)

    def convertir_calificacion(self):
        try:
            nota = float(self.nota.get())
            calificacion = Calificacion(nota)
            literal = calificacion.convertir_a_literal()
            self.resultado_calificacion.config(text=f"Calificación Literal: {literal}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

    def ordenar_numeros(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            num3 = float(self.num3.get())
            ordenar = OrdenarNumeros(num1, num2, num3)
            numeros_ordenados = ordenar.ordenar()
            self.resultado_orden.config(text=f"Números ordenados: {numeros_ordenados}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def convertir_a_radianes(self):
        try:
            grados = float(self.valor.get())
            radianes = ConvertirGradosRadianes.grados_a_radianes(grados)
            self.resultado_conversion.config(text=f"Resultado: {radianes:.5f} radianes")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

    def convertir_a_grados(self):
        try:
            radianes = float(self.valor.get())
            grados = ConvertirGradosRadianes.radianes_a_grados(radianes)
            self.resultado_conversion.config(text=f"Resultado: {grados:.5f} grados")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")


# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()