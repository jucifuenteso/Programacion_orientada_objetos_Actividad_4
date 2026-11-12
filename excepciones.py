import tkinter as tk
from tkinter import messagebox, ttk


# --- CLASE DE LOGICA (MODELO) ---
class PruebaExcepciones:
    """
    Clase que encapsula los bloques try-except-finally del ejercicio
    y registra los mensajes generados durante la ejecucion.
    """

    def __init__(self):
        self.mensajes = []

    def ejecutar_flujo(self):
        """Ejecuta los dos bloques try y retorna la lista de mensajes."""
        self.mensajes.clear()

        # Primer bloque try
        try:
            self.mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0  # Se lanza ZeroDivisionError
            # Esta instruccion nunca sera ejecutada
            self.mensajes.append("Después de la división")
        except ZeroDivisionError:
            # Se captura la excepcion aritmetica
            self.mensajes.append("División por cero")
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepcion
            self.mensajes.append("Ingresando al primer finally")

        # Segundo bloque try
        try:
            self.mensajes.append("Ingresando al segundo try")
            objeto = None
            # Equivalente a invocar un metodo sobre null; lanza AttributeError
            objeto.to_string()
            # Esta instruccion nunca sera ejecutada porque se lanzo una excepcion
            self.mensajes.append("Imprimiendo objeto")
        except ZeroDivisionError:
            # La excepcion lanzada no es de este tipo
            self.mensajes.append("División por cero")
        except Exception:
            # Se captura la excepcion general
            self.mensajes.append("Ocurrió una excepción")
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepcion
            self.mensajes.append("Ingresando al segundo finally")

        return self.mensajes


# --- CLASE DE INTERFAZ GRAFICA (VISTA) ---
class InterfazExcepciones:
    """Interfaz grafica en Tkinter para visualizar la ejecucion de PruebaExcepciones."""

    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de Excepciones")
        self.root.geometry("420x380")
        self.root.resizable(False, False)

        self.prueba = PruebaExcepciones()

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _construir_interfaz(self):
        # Contenedor de botones de accion
        frame_botones = ttk.LabelFrame(
            self.root, text=" Control de Ejecución ", padding=10
        )
        frame_botones.pack(fill="x", padx=15, pady=10)
        frame_botones.columnconfigure((0, 1), weight=1)

        btn_ejecutar = ttk.Button(
            frame_botones, text="Ejecutar Programa", command=self.ejecutar
        )
        btn_ejecutar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_limpiar = ttk.Button(
            frame_botones, text="Limpiar", command=self.limpiar
        )
        btn_limpiar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Contenedor de salida en pantalla
        frame_salida = ttk.LabelFrame(
            self.root, text=" Resultado en Pantalla ", padding=10
        )
        frame_salida.pack(fill="both", expand=True, padx=15, pady=10)

        scrollbar = ttk.Scrollbar(frame_salida)
        scrollbar.pack(side="right", fill="y")

        self.lista_salida = tk.Listbox(
            frame_salida,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
        )
        self.lista_salida.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lista_salida.yview)

    def ejecutar(self):
        """Ejecuta el flujo de excepciones y muestra cada linea en el Listbox."""
        self.limpiar()
        resultados = self.prueba.ejecutar_flujo()
        for linea in resultados:
            self.lista_salida.insert(tk.END, linea)
        messagebox.showinfo(
            "Ejecución finalizada",
            "Se completaron los dos bloques try-except-finally.",
        )

    def limpiar(self):
        """Limpia los resultados mostrados en pantalla."""
        self.lista_salida.delete(0, tk.END)


# --- PUNTO DE ENTRADA PRINCIPAL ---
def main():
    root = tk.Tk()
    InterfazExcepciones(root)
    root.mainloop()


if __name__ == "__main__":
    main()