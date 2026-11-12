import math
import tkinter as tk
from tkinter import messagebox, ttk


# --- CLASE DE LOGICA (MODELO) ---
class CalculosNumericos:
    """
    Clase que realiza calculos matematicos (logaritmo neperiano y raiz cuadrada)
    validando el dominio numerico mediante excepciones.
    """

    def calcular_logaritmo_neperiano(self, valor):
        """
        Calcula el logaritmo neperiano de un valor positivo.
        Lanza ArithmeticError si el valor es menor o igual a cero.
        """
        if valor <= 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular el logaritmo."
            )
        return math.log(valor)

    def calcular_raiz_cuadrada(self, valor):
        """
        Calcula la raiz cuadrada de un valor no negativo.
        Lanza ArithmeticError si el valor es menor a cero.
        """
        if valor < 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular la raíz cuadrada."
            )
        return math.sqrt(valor)


# --- CLASE DE INTERFAZ GRAFICA (VISTA) ---
class InterfazCalculos:
    """Interfaz grafica en Tkinter para ejecutar los calculos numericos."""

    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("400x290")
        self.root.resizable(False, False)

        self.calculos = CalculosNumericos()
        self.var_logaritmo = tk.StringVar()
        self.var_raiz = tk.StringVar()

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _construir_interfaz(self):
        # Contenedor de entrada de datos
        frame_entrada = ttk.LabelFrame(
            self.root, text=" Valor de Entrada ", padding=12
        )
        frame_entrada.pack(fill="x", padx=15, pady=(10, 5))
        frame_entrada.columnconfigure(1, weight=1)

        ttk.Label(frame_entrada, text="Valor numérico:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_valor = ttk.Entry(frame_entrada)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Contenedor de botones de calculo
        frame_botones = ttk.Frame(self.root, padding=(15, 5))
        frame_botones.pack(fill="x")
        frame_botones.columnconfigure((0, 1), weight=1)

        btn_logaritmo = ttk.Button(
            frame_botones,
            text="Logaritmo Neperiano",
            command=self.ejecutar_logaritmo,
        )
        btn_logaritmo.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_raiz = ttk.Button(
            frame_botones,
            text="Raíz Cuadrada",
            command=self.ejecutar_raiz,
        )
        btn_raiz.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Contenedor de resultados dentro de la misma ventana
        frame_resultados = ttk.LabelFrame(
            self.root, text=" Resultados ", padding=12
        )
        frame_resultados.pack(fill="x", padx=15, pady=5)
        frame_resultados.columnconfigure(1, weight=1)

        ttk.Label(frame_resultados, text="Logaritmo neperiano:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        entry_res_log = ttk.Entry(
            frame_resultados, textvariable=self.var_logaritmo, state="readonly"
        )
        entry_res_log.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_resultados, text="Raíz cuadrada:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        entry_res_raiz = ttk.Entry(
            frame_resultados, textvariable=self.var_raiz, state="readonly"
        )
        entry_res_raiz.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        btn_limpiar = ttk.Button(
            frame_resultados, text="Limpiar", command=self.limpiar
        )
        btn_limpiar.grid(row=2, column=0, columnspan=2, pady=(8, 0), sticky="ew")

        self.entry_valor.focus()

    def _obtener_valor(self):
        """Convierte el texto ingresado a float o lanza ValueError si no es valido."""
        texto = self.entry_valor.get().strip()
        if not texto:
            raise ValueError("Campo vacio")
        return float(texto)

    def ejecutar_logaritmo(self):
        """Maneja el evento del boton Logaritmo Neperiano y sus excepciones."""
        try:
            valor = self._obtener_valor()
            resultado = self.calculos.calcular_logaritmo_neperiano(valor)
            self.var_logaritmo.set(f"{resultado:.6f}")
        except ValueError:
            self.var_logaritmo.set("Error de entrada")
            messagebox.showerror(
                "Error de formato",
                "El valor debe ser numérico para calcular el logaritmo.",
            )
        except ArithmeticError as error:
            self.var_logaritmo.set("Error aritmético")
            messagebox.showerror("Error aritmético", str(error))

    def ejecutar_raiz(self):
        """Maneja el evento del boton Raiz Cuadrada y sus excepciones."""
        try:
            valor = self._obtener_valor()
            resultado = self.calculos.calcular_raiz_cuadrada(valor)
            self.var_raiz.set(f"{resultado:.6f}")
        except ValueError:
            self.var_raiz.set("Error de entrada")
            messagebox.showerror(
                "Error de formato",
                "El valor debe ser numérico para calcular la raíz cuadrada.",
            )
        except ArithmeticError as error:
            self.var_raiz.set("Error aritmético")
            messagebox.showerror("Error aritmético", str(error))

    def limpiar(self):
        """Limpia el campo de entrada y los resultados."""
        self.entry_valor.delete(0, tk.END)
        self.var_logaritmo.set("")
        self.var_raiz.set("")
        self.entry_valor.focus()


# --- PUNTO DE ENTRADA PRINCIPAL ---
def main():
    root = tk.Tk()
    InterfazCalculos(root)
    root.mainloop()


if __name__ == "__main__":
    main()