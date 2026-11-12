import tkinter as tk
from tkinter import messagebox, ttk


# --- CLASE DE LOGICA (MODELO) ---
class Vendedor:
    """
    Clase que modela un vendedor con nombre, apellidos y edad,
    incluyendo la validacion de su mayoria de edad y rango permitido.
    """

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None

    def verificar_edad(self, edad):
        """
        Verifica que la edad este en el rango de 0 a 120 y que sea
        mayor o igual a 18. Lanza ValueError si no cumple.
        """
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad

    def imprimir(self):
        """Retorna una cadena con los valores de los atributos del vendedor."""
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor = {self.edad}"
        )


# --- CLASE DE INTERFAZ GRAFICA (VISTA) ---
class InterfazVendedor:
    """Interfaz grafica en Tkinter para registrar y validar un Vendedor."""

    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendedor")
        self.root.geometry("380x250")
        self.root.resizable(False, False)

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _construir_interfaz(self):
        # Contenedor del formulario de entrada
        frame_datos = ttk.LabelFrame(
            self.root, text=" Datos del Vendedor ", padding=12
        )
        frame_datos.pack(fill="x", padx=15, pady=10)
        frame_datos.columnconfigure(1, weight=1)

        ttk.Label(frame_datos, text="Nombre:").grid(
            row=0, column=0, padx=5, pady=6, sticky="w"
        )
        self.entry_nombre = ttk.Entry(frame_datos)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=6, sticky="ew")

        ttk.Label(frame_datos, text="Apellidos:").grid(
            row=1, column=0, padx=5, pady=6, sticky="w"
        )
        self.entry_apellidos = ttk.Entry(frame_datos)
        self.entry_apellidos.grid(row=1, column=1, padx=5, pady=6, sticky="ew")

        ttk.Label(frame_datos, text="Edad:").grid(
            row=2, column=0, padx=5, pady=6, sticky="w"
        )
        self.entry_edad = ttk.Entry(frame_datos)
        self.entry_edad.grid(row=2, column=1, padx=5, pady=6, sticky="ew")

        # Contenedor de botones
        frame_botones = ttk.Frame(self.root, padding=(15, 5))
        frame_botones.pack(fill="x")
        frame_botones.columnconfigure((0, 1), weight=1)

        btn_verificar = ttk.Button(
            frame_botones, text="Verificar y Mostrar", command=self.procesar
        )
        btn_verificar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_limpiar = ttk.Button(
            frame_botones, text="Limpiar", command=self.limpiar
        )
        btn_limpiar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.entry_nombre.focus()

    def procesar(self):
        """Captura los datos, valida la edad y muestra el resultado o error."""
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        edad_texto = self.entry_edad.get().strip()

        if not nombre or not apellidos or not edad_texto:
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, complete todos los campos antes de continuar.",
            )
            return

        try:
            edad = int(edad_texto)
        except ValueError:
            messagebox.showerror(
                "Error de formato",
                "La edad debe ser un número entero válido.",
            )
            return

        try:
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            messagebox.showinfo("Datos del Vendedor", vendedor.imprimir())
        except ValueError as error:
            messagebox.showerror("Error de validación", str(error))

    def limpiar(self):
        """Limpia los campos de texto y devuelve el foco al primer campo."""
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_nombre.focus()


# --- PUNTO DE ENTRADA PRINCIPAL ---
def main():
    root = tk.Tk()
    InterfazVendedor(root)
    root.mainloop()


if __name__ == "__main__":
    main()