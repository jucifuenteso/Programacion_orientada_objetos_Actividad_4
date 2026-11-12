import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText


# --- CLASE DE LOGICA (MODELO) ---
class LectorArchivo:
    """Clase que modela la lectura eficiente de un archivo de texto."""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_y_mostrar(self):
        """
        Lee el archivo linea por linea usando bufer y retorna el contenido completo.
        Lanza FileNotFoundError si el archivo no existe.
        """
        if not self.ruta_archivo:
            raise ValueError("No se ha especificado una ruta de archivo válida.")

        contenido = []
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    contenido.append(linea)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"El archivo no se encontró en la ruta:\n{self.ruta_archivo}"
            )
        except UnicodeDecodeError:
            raise ValueError(
                "El archivo no está codificado en UTF-8 y no se puede leer.\n"
                "Por favor, guarde el archivo 'prueba.txt' con codificación UTF-8."
            )
        except Exception as error:
            raise Exception(
                f"Ocurrió un error inesperado al leer el archivo:\n{error}"
            )

        return "".join(contenido)


# --- CLASE DE INTERFAZ GRAFICA (VISTA) ---
class InterfazLector:
    """Interfaz grafica en Tkinter para visualizar el contenido de un archivo."""

    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos de Texto")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        self.ruta_seleccionada = None

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _construir_interfaz(self):
        # Seccion de controles
        frame_controles = ttk.Frame(self.root, padding=10)
        frame_controles.pack(fill="x", padx=10, pady=(10, 5))

        btn_examinar = ttk.Button(
            frame_controles,
            text="Seleccionar Archivo",
            command=self.seleccionar_archivo,
        )
        btn_examinar.pack(side="left", padx=5)

        self.btn_leer = ttk.Button(
            frame_controles,
            text="Leer y Mostrar",
            command=self.leer_archivo,
            state="disabled",
        )
        self.btn_leer.pack(side="left", padx=5)

        btn_limpiar = ttk.Button(
            frame_controles, text="Limpiar", command=self.limpiar
        )
        btn_limpiar.pack(side="right", padx=5)

        # Etiqueta para mostrar la ruta seleccionada
        self.lbl_ruta = ttk.Label(
            self.root,
            text="Ningún archivo seleccionado.",
            font=("Segoe UI", 9),
            foreground="gray",
        )
        self.lbl_ruta.pack(fill="x", padx=20, pady=(0, 5))

        # Area de visualizacion de texto (desplazable y de solo lectura)
        frame_texto = ttk.LabelFrame(
            self.root, text=" Contenido del Archivo ", padding=5
        )
        frame_texto.pack(fill="both", expand=True, padx=15, pady=5)

        self.txt_contenido = ScrolledText(
            frame_texto,
            wrap="word",
            font=("Consolas", 10),
            state="disabled",
            bg="#f9f9f9",
            relief="flat",
        )
        self.txt_contenido.pack(fill="both", expand=True)

        # Barra de estado
        status_bar = ttk.Label(
            self.root, text="Listo", relief="sunken", anchor="w"
        )
        status_bar.pack(side="bottom", fill="x")

    def seleccionar_archivo(self):
        """Abre el explorador para seleccionar el archivo .txt y habilita la lectura."""
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de prueba",
            filetypes=(
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*"),
            ),
        )
        if ruta:
            self.ruta_seleccionada = ruta
            self.lbl_ruta.config(
                text=f"Archivo seleccionado: {ruta}", foreground="black"
            )
            self.btn_leer.config(state="normal")
            self.txt_contenido.config(state="normal")
            self.txt_contenido.delete("1.0", tk.END)
            self.txt_contenido.config(state="disabled")
            self.root.focus_set()

    def leer_archivo(self):
        """Instancia el modelo, lee el archivo y muestra el resultado en pantalla."""
        if not self.ruta_seleccionada:
            return

        try:
            lector = LectorArchivo(self.ruta_seleccionada)
            contenido = lector.leer_y_mostrar()

            self.txt_contenido.config(state="normal")
            self.txt_contenido.delete("1.0", tk.END)
            self.txt_contenido.insert(tk.END, contenido)
            self.txt_contenido.config(state="disabled")

        except (FileNotFoundError, ValueError) as error:
            messagebox.showerror("Error de Lectura", str(error))
            self.limpiar()
        except Exception as error:
            messagebox.showerror("Error Crítico", str(error))
            self.limpiar()

    def limpiar(self):
        """Limpia la ruta seleccionada y el area de texto."""
        self.ruta_seleccionada = None
        self.lbl_ruta.config(
            text="Ningún archivo seleccionado.", foreground="gray"
        )
        self.btn_leer.config(state="disabled")
        self.txt_contenido.config(state="normal")
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.config(state="disabled")


# --- PUNTO DE ENTRADA PRINCIPAL ---
def main():
    root = tk.Tk()
    InterfazLector(root)
    root.mainloop()


if __name__ == "__main__":
    main()