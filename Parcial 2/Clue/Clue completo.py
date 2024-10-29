import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class ClueJuego:
    def __init__(self):
        self.personajes = ["Rojo", "Blanco", "Azul", "Amarillo", "Verde"]
        self.lugares = ["Estudio", "Cocina", "Biblioteca", "Billar", "Comedor"]
        self.armas = ["Candelabro", "Cuchillo de cocina", "Revólver", "Cuerda", "Llave inglesa"]

        self.historias = [
            {
                "personajes": {
                    "Rojo": "Rojo dice que estaba en la Biblioteca estudiando y no vio ningun objeto.",
                    "Blanco": "Blanco estaba en la Cocina preparando el almuerzo y vio el objeto revólver.",
                    "Azul": "Azul estaba en el Billar arreglando una tubería rota y vio la llave inglesa.",
                    "Amarillo": "Amarillo estaba en el Estudio leyendo un libro de cocina y vio el candelabro.",
                    "Verde": "Verde estaba en el Comedor tomando una siesta y vio la cuerda."
                },
                "lugares": {
                    "Biblioteca": "Rojo fue visto en la biblioteca.",
                    "Cocina": "Blanco estaba en la Cocina preparando el almuerzo y vio el objeto revólver.",
                    "Billar": "Azul estaba en el Billar arreglando una tubería rota y vio la llave inglesa.",
                    "Estudio": "Amarillo estaba en el Estudio de estar leyendo un libro de cocina y vio el candelabro.",
                    "Comedor": "Verde estaba en el Comedor tomando una siesta y vio la cuerda."
                },
                "armas": {
                    "Cuchillo de cocina": "El cuchillo estaba en la bilioteca antes del asesinato.",
                    "Revólver": "Blanco estaba en la Cocina preparando el almuerzo y vio el objeto revólver.",
                    "Llave inglesa": "Azul estaba en el Billar arreglando una tubería rota y vio la llave inglesa.",
                    "Candelabro": "Amarillo estaba en el Estudio leyendo un libro de cocina y vio el candelabro.",
                    "Cuerda": "Verde estaba en el Comedor tomando una siesta y vio la cuerda."
                },
                "lugar": "Biblioteca",
                "arma": "Cuchillo de cocina",
                "culpable": "Rojo"
            },
            {
                "personajes": {
                    "Rojo": "Rojo estaba en la Cocina dando una charla sobre historia a los empleados del hotel y vio el objeto revolver.",
                    "Blanco": "Blanco dice que estaba en la Biblioteca revisando unos informes médicos.",
                    "Azul": "Azul estaba en la Biblioteca hablando por teléfono con un colega y vio la cuerda. Y dice que no habia nadie mas con el",
                    "Amarillo": "Amarillo estaba en el Comedor descansando después de preparar la cena y vio la llave inglesa.",
                    "Verde": "Verde dice que estaba en el Billar escribiendo un artículo para su periódico y vio el cuchillo."
                },
                "lugares": {
                    "Cocina": "Rojo estaba en la Cocina dando una charla sobre historia a los empleados del hotel y vio el objeto revolver.",
                    "Biblioteca": "Azul estaba en la Biblioteca hablando por teléfono con un colega y vio la cuerda.",
                    "Estudio": "Las camaras en el estudio no estaban funcionando. Nadie dijo haber estadoa ahi",
                    "Comedor": "Amarillo estaba en el Comedor descansando después de preparar la cena y vio la llave inglesa.",
                    "Billar": "Verde estaba en el Billar escribiendo un artículo para su periódico y vio el cuchillo."
                },
                "armas": {
                    "Candelabro": "El candelabro fue encontrado en el Estudio.",
                    "Revólver": "Rojo estaba en la Cocina dando una charla sobre historia a los empleados del hotel y vio el objeto revolver.",
                    "Llave inglesa": "Amarillo estaba en el Comedor descansando después de preparar la cena y vio la llave inglesa.",
                    "Cuchillo de cocina": "Verde estaba en el Billar escribiendo un artículo para su periódico y vio el cuchillo.",
                    "Cuerda": "Azul estaba en el Estudio hablando por teléfono con un colega y vio la cuerda."
                },
                "lugar": "Estudio",
                "arma": "Candelabro",
                "culpable": "Blanco"
            },
            {
                "personajes": {
                    "Rojo": "Rojo estaba en la Biblioteca.",
                    "Blanco": "Blanco estaba en el Estudio y vio el cuchillo.",
                    "Azul": "Azul estaba en la Cocina.",
                    "Amarillo": "Amarillo estaba en el Billar y vio la cuerda.",
                    "Verde": "Verde estaba en el Comedor y vio la llave inglesa."
                },
                "lugares": {
                    "Biblioteca": "Rojo estaba en la Biblioteca.",
                    "Estudio": "Blanco estaba en el Estudio y vio el cuchillo.",
                    "Cocina": "Las camaras detectaron a azul en la cocina antes del asesinato y despues dejaron de funcionar",
                    "Billar": "Amarillo estaba en el Billar y vio la cuerda.",
                    "Comedor": "Verde estaba en el Comedor y vio la llave inglesa."
                },
                "armas": {
                    "Revólver": "El relvolver se encontro escocndido en la cocina.",
                    "Cuchillo de cocina": "Blanco estaba en el Estudio y vio el cuchillo.",
                    "Candelabro": "Las camaras detectaron el candelabro en la biblioteca.",
                    "Llave inglesa": "Verde estaba en el Comedor y vio la llave inglesa.",
                    "Cuerda": "Amarillo estaba en el Billar y vio la cuerda."
                },
                "lugar": "Cocina",
                "arma": "Revólver",
                "culpable": "Azul"
            },
            {
                "personajes": {
                    "Rojo": "Rojo estaba solo en la cocina.",
                    "Blanco": "Blanco estaba en el Estudio discutiendo con su esposo por teléfono y vio el candelabro.",
                    "Azul": "Azul estaba en el Comedor leyendo un manual de ingeniería y vio la llave inglesa.",
                    "Amarillo": "Amarillo dijo que estaba en la Cocina cocinando pescado para la cena y no vio ningun objeto.",
                    "Verde": "Verde estaba en la Biblioteca investigando para un reportaje y vio el chuchillo."
                },
                "lugares": {
                    "Billar": "Las camaras en Billar no estaban funcionando",
                    "Estudio": "Blanco estaba en el Estudio discutiendo con su esposo por teléfono y vio el candelabro.",
                    "Comedor": "Azul estaba en el Comedor leyendo un manual de ingeniería y vio la llave inglesa.",
                    "Cocina": "Amarillo dice que estaba en la Cocina cocinando pescado para la cena y no vio ningun objeto.",
                    "Biblioteca": "Verde estaba en la Biblioteca investigando para un reportaje."
                },
                "armas": {
                    "Cuerda": "No se encontro la cuerda.",
                    "Candelabro": "Blanco estaba en el Estudio discutiendo con su esposo por teléfono y vio el candelabro.",
                    "Llave inglesa": "Azul estaba en el Comedor leyendo un manual de ingeniería y vio la llave inglesa.",
                    "Revólver": "Amarillo dice que estaba en la Cocina cocinando pescado para la cena y no vio ningun objeto.",
                    "Cuchillo de cocina": "Verde estaba en la Biblioteca investigando para un reportaje y vio el chuchillo."
                },
                "lugar": "Billar",
                "arma": "Cuerda",
                "culpable": "Amarillo"
            },
            {
                "personajes": {
                    "Rojo": "Rojo estaba en el Comedor explorando el lugar en busca de objetos antiguos y encontro la llave inglesa debajo de un estante.",
                    "Blanco": "Blanco estaba en el Estudio revisando unos documentos históricos y vio el candelabro.",
                    "Azul": "Azul estaba en la Biblioteca intentando reparar un libro antiguo y vio el cuchillo.",
                    "Amarillo": "Amarillo estaba en el Billar pintando un paisaje del lugar y vio el revolver.",
                    "Verde": "Verde estaba en la Cocina buscando algo de comer entre los suministros viejos. Las camars en cocina no estaban funcionando"
                },
                "lugares": {
                    "Comedor": "Rojo estaba en el Comedor explorando el lugar en busca de objetos antiguos y vio la llave inglesa.",
                    "Estudio": "Blanco estaba en el Estudio revisando unos documentos históricos y vio el candelabro.",
                    "Biblioteca": "Azul estaba en la Biblioteca intentando reparar un libro antiguo y vio el cuchillo.",
                    "Billar": "Amarillo estaba en el Billar pintando un paisaje del lugar y vio el revolver.",
                    "Cocina": "Verde estaba en la Cocina buscando algo de comer entre los suministros viejos."
                },
                "armas": {
                    "Llave inglesa": "Rojo estaba en el Comedor explorando el lugar en busca de objetos antiguos y encontro la llave inglesa debajo de un estante.",
                    "Candelabro": "Blanco estaba en el Estudio revisando unos documentos históricos y vio el candelabro.",
                    "Cuchillo de cocina": "Azul estaba en la Biblioteca intentando reparar un libro antiguo y vio el cuchillo.",
                    "Revólver": "Amarillo estaba en el Billar pintando un paisaje del lugar y vio el revolver.",
                    "Cuerda": "Verde estaba en la Cocina buscando algo de comer entre los suministros viejos."
                },
                "lugar": "Comedor",
                "arma": "Llave inglesa",
                "culpable": "Verde"
            }
        ]

        self.historia_actual = random.choice(self.historias)
        self.pistas_restantes = 5


    def obtener_pista(self, tipo, seleccion):
        if tipo == "personaje":
            personaje = seleccion
            pista = self.historia_actual["personajes"].get(personaje, "")
        elif tipo == "lugar":
            pista = self.historia_actual["lugares"].get(seleccion, "")
        elif tipo == "arma":
            pista = self.historia_actual["armas"].get(seleccion, "")
        return pista

def mostrar_pista():
    if juego.pistas_restantes > 0:
        tipo_pista = seleccion_tipo_pista.get()
        seleccion = seleccion_opcion.get()
        pista = juego.obtener_pista(tipo_pista, seleccion)
        messagebox.showinfo("Pista", pista)
        juego.pistas_restantes -= 1
        etiqueta_pistas_restantes.config(text="Pistas restantes: {}".format(juego.pistas_restantes))
    if juego.pistas_restantes == 0:
        boton_pista.config(state=tk.DISABLED)
        mostrar_adivinanza()

def actualizar_lista(*args):
    categoria_seleccionada = seleccion_tipo_pista.get()
    if categoria_seleccionada == "personaje":
        lista_opciones["menu"].delete(0, "end")
        for personaje in juego.personajes:
            lista_opciones["menu"].add_command(label=personaje, command=tk._setit(seleccion_opcion, personaje))
    elif categoria_seleccionada == "lugar":
        lista_opciones["menu"].delete(0, "end")
        for lugar in juego.lugares:
            lista_opciones["menu"].add_command(label=lugar, command=tk._setit(seleccion_opcion, lugar))
    elif categoria_seleccionada == "arma":
        lista_opciones["menu"].delete(0, "end")
        for arma in juego.armas:
            lista_opciones["menu"].add_command(label=arma, command=tk._setit(seleccion_opcion, arma))

def mostrar_adivinanza():
    seleccion_opcion_culpable = tk.StringVar()
    seleccion_opcion_lugar = tk.StringVar()
    seleccion_opcion_arma = tk.StringVar()
    
    def comprobar_adivinanza():
        respuesta_culpable = seleccion_opcion_culpable.get()
        respuesta_lugar = seleccion_opcion_lugar.get()
        respuesta_arma = seleccion_opcion_arma.get()
        
        if (respuesta_culpable == juego.historia_actual["culpable"] and
            respuesta_lugar == juego.historia_actual["lugar"] and
            respuesta_arma == juego.historia_actual["arma"]):
            messagebox.showinfo("Resultado", "¡Felicidades! Has resuelto el misterio correctamente.")
        else:
            aciertos = []
            if respuesta_culpable == juego.historia_actual["culpable"]:
                aciertos.append("Culpable")
            if respuesta_lugar == juego.historia_actual["lugar"]:
                aciertos.append("Lugar")
            if respuesta_arma == juego.historia_actual["arma"]:
                aciertos.append("Arma")
            aciertos_str = ", ".join(aciertos) if aciertos else "ninguno"
            messagebox.showinfo("Resultado", "Lo siento, no has adivinado correctamente. Acertaste en: {}".format(aciertos_str))
    
    ventana_adivinanza = tk.Toplevel(ventana)
    ventana_adivinanza.title("Adivinanza Final")
    
    tk.Label(ventana_adivinanza, text="¿Quién es el culpable?").pack()
    seleccion_opcion_culpable.set("")
    menu_culpable = tk.OptionMenu(ventana_adivinanza, seleccion_opcion_culpable, *juego.personajes)
    menu_culpable.pack()
    
    tk.Label(ventana_adivinanza, text="¿Dónde ocurrió el asesinato?").pack()
    seleccion_opcion_lugar.set("")
    menu_lugar = tk.OptionMenu(ventana_adivinanza, seleccion_opcion_lugar, *juego.lugares)
    menu_lugar.pack()
    
    tk.Label(ventana_adivinanza, text="¿Con qué arma?").pack()
    seleccion_opcion_arma.set("")
    menu_arma = tk.OptionMenu(ventana_adivinanza, seleccion_opcion_arma, *juego.armas)
    menu_arma.pack()
    
    boton_comprobar = tk.Button(ventana_adivinanza, text="Comprobar", command=comprobar_adivinanza)
    boton_comprobar.pack()

# Configuración inicial del juego
juego = ClueJuego()

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("800x600") 
ventana.title("Clue: El Juego de Misterio")

# Configurar la imagen de fondo
ruta_imagen_fondo = "C:\\Users\\PC\\Documents\\GitHub\\Sistemas-Expertos-2024b\\Parcial 2\\Clue\\Tablero.png"
imagen_fondo = Image.open(ruta_imagen_fondo)
imagen_fondo = imagen_fondo.resize((800, 600), Image.Resampling.LANCZOS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de etiqueta para mostrar la imagen de fondo
etiqueta_fondo = tk.Label(ventana, image=imagen_fondo_tk)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear los widgets de la interfaz sobre la imagen de fondo
frame = tk.Frame(ventana, bg="white")
frame.pack(padx=20, pady=20)

etiqueta_tipo_pista = tk.Label(frame, text="Selecciona el tipo de pista:", bg="white")
etiqueta_tipo_pista.grid(row=0, column=0, padx=5, pady=5)
seleccion_tipo_pista = tk.StringVar()
seleccion_tipo_pista.set("personaje")
lista_tipos = tk.OptionMenu(frame, seleccion_tipo_pista, "personaje", "lugar", "arma")
lista_tipos.grid(row=0, column=1, padx=5, pady=5)

seleccion_tipo_pista.trace("w", actualizar_lista)

etiqueta_opcion = tk.Label(frame, text="Selecciona una opción:", bg="white")
etiqueta_opcion.grid(row=1, column=0, padx=5, pady=5)
seleccion_opcion = tk.StringVar()
lista_opciones = tk.OptionMenu(frame, seleccion_opcion, "")
lista_opciones.grid(row=1, column=1, padx=5, pady=5)

boton_pista = tk.Button(frame, text="Mostrar Pista", command=mostrar_pista)
boton_pista.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

etiqueta_pistas_restantes = tk.Label(frame, text="Pistas restantes: {}".format(juego.pistas_restantes), bg="white")
etiqueta_pistas_restantes.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Iniciar la interfaz
ventana.mainloop()
