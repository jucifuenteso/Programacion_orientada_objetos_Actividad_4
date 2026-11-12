import tkinter as tk
from tkinter import messagebox, ttk


# --- CLASES DE LOGICA (MODELO) ---
class Programador:
    """Clase que modela a un integrante del equipo de maraton."""

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    """
    Clase que modela un equipo de maraton de programacion con capacidad
    de 2 a 3 integrantes y validaciones de texto.
    """

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamano_equipo = 0
        self.programadores = []

    def esta_lleno(self):
        """Determina si el equipo alcanzo el maximo de 3 programadores."""
        return self.tamano_equipo >= 3

    def validar_campo(self, valor, campo):
        """
        Valida que un campo de texto no este vacio, no contenga digitos
        y tenga una longitud estrictamente menor a 20 caracteres.
        """
        if not valor:
            raise ValueError(f"El campo {campo} no puede estar vacío.")

        if any(caracter.isdigit() for caracter in valor):
            if campo == "nombre":
                raise ValueError("El nombre no puede tener dígitos.")
            raise ValueError("Los apellidos no pueden tener dígitos.")

        if len(valor) >= 20:
            if campo == "nombre":
                raise ValueError(
                    "El nombre no puede tener una longitud igual o superior a 20 caracteres."
                )
            raise ValueError(
                "Los apellidos no pueden tener una longitud igual o superior a 20 caracteres."
            )

    def anadir_programador(self, programador):
        """
        Anade un programador al equipo si hay cupo disponible.
        Lanza ValueError si el equipo ya tiene 3 integrantes.
        """
        if self.esta_lleno():
            raise ValueError(
                "El equipo está completo. No se pueden añadir más de 3 programadores."
            )
        self.programadores.append(programador)
        self.tamano_equipo += 1

    def verificar_equipo(self):
        """
        Verifica que el equipo cumpla con el minimo de 2 programadores
        y retorna el resumen completo del equipo.
        """
        if self.tamano_equipo < 2:
            raise ValueError(
                "El equipo debe tener mínimo 2 programadores para poder participar."
            )

        integrantes = "\n".join(
            f"  {i}. {p.nombre} {p.apellidos}"
            for i, p in enumerate(self.programadores, start=1)
        )
        return (
            f"Equipo: {self.nombre_equipo}\n"
            f"Universidad: {self.universidad}\n"
            f"Lenguaje: {self.lenguaje_programacion}\n"
            f"Total integrantes: {self.tamano_equipo}\n\n"
            f"Programadores inscritos:\n{integrantes}"
        )


# --- CLASE DE INTERFAZ GRAFICA (VISTA) ---
class InterfazEquipoMaraton:
    """Interfaz grafica en Tkinter para registrar un equipo de maraton."""

    def __init__(self, root):
        self.root = root
        self.root.title("Equipo Maratón de Programación")
        self.root.geometry("430x420")
        self.root.resizable(False, False)

        self.equipo = None

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _construir_interfaz(self):
        # Seccion 1: Datos del equipo
        frame_equipo = ttk.LabelFrame(
            self.root, text=" Datos del Equipo ", padding=12
        )
        frame_equipo.pack(fill="x", padx=15, pady=(10, 5))
        frame_equipo.columnconfigure(1, weight=1)

        ttk.Label(frame_equipo, text="Nombre del equipo:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_equipo = ttk.Entry(frame_equipo)
        self.entry_equipo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_equipo, text="Universidad:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_universidad = ttk.Entry(frame_equipo)
        self.entry_universidad.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_equipo, text="Lenguaje:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_lenguaje = ttk.Entry(frame_equipo)
        self.entry_lenguaje.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.btn_crear_equipo = ttk.Button(
            frame_equipo, text="Crear Equipo", command=self.crear_equipo
        )
        self.btn_crear_equipo.grid(
            row=3, column=0, columnspan=2, pady=(8, 2), sticky="ew"
        )

        # Seccion 2: Registro de programadores
        frame_prog = ttk.LabelFrame(
            self.root, text=" Añadir Programadores (Mín. 2 - Máx. 3) ", padding=12
        )
        frame_prog.pack(fill="x", padx=15, pady=5)
        frame_prog.columnconfigure(1, weight=1)

        ttk.Label(frame_prog, text="Nombre:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_nombre_prog = ttk.Entry(frame_prog, state="disabled")
        self.entry_nombre_prog.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_prog, text="Apellidos:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.entry_apellidos_prog = ttk.Entry(frame_prog, state="disabled")
        self.entry_apellidos_prog.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.btn_anadir = ttk.Button(
            frame_prog,
            text="Añadir Programador",
            command=self.anadir_programador,
            state="disabled",
        )
        self.btn_anadir.grid(
            row=2, column=0, columnspan=2, pady=(8, 2), sticky="ew"
        )

        # Seccion 3: Acciones generales
        frame_acciones = ttk.Frame(self.root, padding=(15, 8))
        frame_acciones.pack(fill="x")
        frame_acciones.columnconfigure((0, 1), weight=1)

        self.btn_verificar = ttk.Button(
            frame_acciones,
            text="Verificar Equipo",
            command=self.verificar_equipo,
            state="disabled",
        )
        self.btn_verificar.grid(row=0, column=0, padx=5, sticky="ew")

        btn_limpiar = ttk.Button(
            frame_acciones, text="Limpiar Todo", command=self.limpiar
        )
        btn_limpiar.grid(row=0, column=1, padx=5, sticky="ew")

        self.entry_equipo.focus()

    def crear_equipo(self):
        """Valida los datos generales e instancia el objeto EquipoMaratonProgramacion."""
        nombre = self.entry_equipo.get().strip()
        universidad = self.entry_universidad.get().strip()
        lenguaje = self.entry_lenguaje.get().strip()

        if not nombre or not universidad or not lenguaje:
            messagebox.showwarning(
                "Campos incompletos",
                "Debe ingresar el nombre del equipo, la universidad y el lenguaje.",
            )
            return

        self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)

        # Bloquear edicion del equipo y habilitar registro de integrantes
        self.entry_equipo.config(state="disabled")
        self.entry_universidad.config(state="disabled")
        self.entry_lenguaje.config(state="disabled")
        self.btn_crear_equipo.config(state="disabled")

        self.entry_nombre_prog.config(state="normal")
        self.entry_apellidos_prog.config(state="normal")
        self.btn_anadir.config(state="normal")
        self.btn_verificar.config(state="normal")

        messagebox.showinfo(
            "Equipo Creado",
            f"Equipo '{nombre}' registrado. Ahora puede añadir entre 2 y 3 programadores.",
        )
        self.entry_nombre_prog.focus()

    def anadir_programador(self):
        """Valida los atributos del programador y lo agrega al equipo."""
        if self.equipo is None:
            return

        nombre = self.entry_nombre_prog.get().strip()
        apellidos = self.entry_apellidos_prog.get().strip()

        try:
            self.equipo.validar_campo(nombre, "nombre")
            self.equipo.validar_campo(apellidos, "apellidos")

            programador = Programador(nombre, apellidos)
            self.equipo.anadir_programador(programador)

            self.entry_nombre_prog.delete(0, tk.END)
            self.entry_apellidos_prog.delete(0, tk.END)
            self.entry_nombre_prog.focus()

            messagebox.showinfo(
                "Programador Añadido",
                f"Se añadió a {nombre} {apellidos}.\n"
                f"Integrantes actuales: {self.equipo.tamano_equipo} de 3.",
            )
        except ValueError as error:
            messagebox.showerror("Error de validación", str(error))

    def verificar_equipo(self):
        """Comprueba el minimo de integrantes y muestra el resumen completo."""
        if self.equipo is None:
            return

        try:
            resumen = self.equipo.verificar_equipo()
            messagebox.showinfo("Equipo Validado", resumen)
        except ValueError as error:
            messagebox.showerror("Equipo Incompleto", str(error))

    def limpiar(self):
        """Reinicia todos los campos y restaura el estado inicial de la ventana."""
        self.equipo = None

        self.entry_equipo.config(state="normal")
        self.entry_universidad.config(state="normal")
        self.entry_lenguaje.config(state="normal")
        self.btn_crear_equipo.config(state="normal")

        self.entry_equipo.delete(0, tk.END)
        self.entry_universidad.delete(0, tk.END)
        self.entry_lenguaje.delete(0, tk.END)

        self.entry_nombre_prog.config(state="normal")
        self.entry_apellidos_prog.config(state="normal")
        self.entry_nombre_prog.delete(0, tk.END)
        self.entry_apellidos_prog.delete(0, tk.END)

        self.entry_nombre_prog.config(state="disabled")
        self.entry_apellidos_prog.config(state="disabled")
        self.btn_anadir.config(state="disabled")
        self.btn_verificar.config(state="disabled")

        self.entry_equipo.focus()


# --- PUNTO DE ENTRADA PRINCIPAL ---
def main():
    root = tk.Tk()
    InterfazEquipoMaraton(root)
    root.mainloop()


if __name__ == "__main__":
    main()