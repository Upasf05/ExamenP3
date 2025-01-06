import tkinter as tk #Librería Tkinter
from tkinter import messagebox
from PIL import Image, ImageTk #Importar la librería Pillow para colocar iágenes y ajustar sus tamaños.
import random #Librería random, será útil para decidir 

class SplashScreen: #Pantalla de inicio que se ejecuta durante unos segundos.
    def __init__(self, master): #Método splash para la patalla de inicio
        self.master = master
        self.master.title("Cargando...")
        self.master.geometry("400x400")
        self.master.configure(bg="white")

        # Imagen del splash
        image_path = r"C:\\Users\\user\\Documents\\Trabajosphyton\\Ahorcado\\splash_image.png"  #Imagen que aparece en la pantalla de carga
        original_image = Image.open(image_path).resize((400, 400)) #Ajustar tamaño de imagen con Pillow
        self.image = ImageTk.PhotoImage(original_image)
        self.image_label = tk.Label(master, image=self.image, bg="white")
        self.image_label.pack()

        # Configuración para cerrar el splash después de 4 segundos
        self.master.after(4000, self.close_splash)  # 4000 ms = 4 segundos #Llamar al método close splash luego de pasados unos segundos

    def close_splash(self): #Método para cerrar la pantalla de carga
        self.master.destroy()
        main_window = tk.Tk()
        HangmanMenu(main_window)
        main_window.mainloop()

class HangmanMenu: #Pantalla de menú
    def __init__(self, master): #Método para el menú
        self.master = master
        self.master.title("Menú - Ahorcado")
        self.master.geometry("400x600")
        self.master.configure(bg="white")

        # Imagen del menú
        image_path = r"C:\\Users\\user\\Documents\\Trabajosphyton\\Ahorcado\\imagen.png"  # Cambia esta ruta si necesitas
        original_image = Image.open(image_path).resize((130, 200))
        self.image = ImageTk.PhotoImage(original_image)
        self.image_label = tk.Label(master, image=self.image, bg="white")
        self.image_label.pack()

        # Título del menú
        self.title_label = tk.Label(master, text="¡Ahorcado!", font=("Arial", 24, "bold"), bg="white", fg="black")
        self.title_label.pack(pady=20)

        # Botones de los modos de juego
        button_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#007BFF",
            "fg": "white",
            "activebackground": "#0056b3",
            "activeforeground": "white",
            "relief": "flat",
            "cursor": "hand2"
        }

        modes = [
            ("Modo Clásico", "classic"),
            ("Animales", "animals"),
            ("Tecnología y programación", "tech"),
            ("Ciencia", "science"),
            ("Geografía y países", "geography"),
            ("Deportes", "sports")
        ]

        for text, mode in modes:
            tk.Button(master, text=text, command=lambda m=mode: self.start_game(m), **button_style).pack(pady=5)

        tk.Button(master, text="Salir", command=self.master.quit, **button_style).pack(pady=20)

    def start_game(self, mode): #Método para iniciar el juego sin importar el modo seleccionado.
        self.master.withdraw()
        game_window = tk.Toplevel(self.master)
        HangmanGame(game_window, mode)

class HangmanGame: #Clase donde se ejecuta el juego
    def __init__(self, master, mode):
        self.master = master
        self.master.title(f"Modo - {mode.capitalize()}")
        self.master.geometry("400x500")
        self.master.configure(bg="white")

        # Palabras que aparecerán en la partida (una aparecerá aleatoriamente)
        self.words = { 
            "classic": ["amor", "agua", "arbol", "amigo", "casa", "cielo", "ciudad", "comida", "corazon", "dinero",
            "dia", "escuela", "familia", "felicidad", "fiesta", "flor", "fuego", "gente", "guerra", "historia",
            "hombre", "jardin", "juego", "libro", "luz", "mañana", "mujer", "mundo", "niño", "noche",
            "nube", "paz", "pelicula", "perro", "persona", "plaza", "rio", "rojo", "salud", "semana",
            "sol", "tarde", "tierra", "trabajo", "tren", "universo", "viento", "vida", "viaje", "zapato"],
            "animals": ["perro", "gato", "elefante", "caballo", "vaca", "oveja", "cerdo", "gallina", "pato", "conejo", "raton", "loro", "tigre", "leon", "jirafa", "cebra", "hipopotamo", "rinoceronte", "pinguino", "canguro", "koala", "puma", "lince", "cocodrilo", "tiburon", "ballena", "delfin", "oso", "mapache", "zorro", "murcielago", "aguila", "pajaro", "condor", "lobo", "ciervo", "antilope", "armadillo", "tejon", "mono", "camello", "llama", "pavo", "ganso", "paloma", "tortuga"],
            "tech": ["python", "codigo", "internet", "javascript", "java", "html", "css", "c++", "ruby", "php", "swift", "typescript", "nodejs", "git", "github", "sql", "api", "algoritmo", "frontend", "backend", "rest", "graphql", "json", "xml", "mvc", "kotlin", "exe", "python3", "docker", "windows", "vscode", "linux", "react", "angular", "vue", "flutter", "android", "ios", "androidstudio", "scala", "go", "rust", "machinelearning", "deeplearning", "tensorflow", "pytorch", "webdev"],
            "science": ["atomo", "molecula", "gravedad", "celula", "adn", "proteina", "enzima", "carbohidrato", "lipido", "acido", "base", "solucion", "ph", "ion", "metabolismo", "mitocondria", "ribosoma", "nucleo", "membrana", "cromosoma", "vacuna", "antigeno", "anticuerpo", "microbio", "bacteria", "virus", "hongos", "glucosa", "oxigeno", "nitrogeno", "hidrogeno", "calcio", "hierro", "sangre", "plasma", "globulos rojos", "globulos blancos", "hormona", "insulina", "respiracion", "circulacion", "digestion", "sistema nervioso", "cerebro", "corazon", "pulmon"],
            "geography": ["montaña", "rio", "oceano", "continente", "pais", "ciudad", "desierto", "selva", "bosque", "isla", "peninsula", "archipielago", "valle", "lago", "playa", "cordillera", "volcan", "costa", "río", "ecuador", "españa", "estadosunidos", "colombia", "peru", "venezuela", "bolivia", "argentina", "chile", "brasil", "mexico", "canada", "francia", "alemania", "italia", "rusia", "egipto", "india", "china", "japon", "corea", "australia", "inglaterra", "arabiasaudi", "america", "europa", "africa", "asia", "oceania"],
            "sports": ["futbol", "tenis", "natacion", "baloncesto", "beisbol", "voleibol", "rugby", "boxeo", "gimnasia", "atletismo", "ciclismo", "escalada", "esgrima", "karate", "taekwondo", "judo", "surf", "esqui", "snowboard", "yoga", "ejercicio", "golf", "hockey", "futsal", "badminton", "pingpong", "lucha", "cricket", "motocross", "carrera", "halterofilia", "futbolamericano", "esquiacuatico", "paracaidismo", "balonmano", "waterpolo", "patinaje", "hipismo", "vela", "barcelona", "emelec", "aucas", "nacional", "liga", "deportivoquito", "independientedelvalle"]
        }.get(mode, ["amor", "agua", "arbol"])

        self.word_to_guess = random.choice(self.words) #Seleccionar una palabra a través de la biblioteca random
        self.guessed_letters = []
        self.attempts = 6

        # Estilos para los botones
        label_style = {"font": ("Arial", 24), "bg": "white", "fg": "black"}
        small_label_style = {"font": ("Arial", 14), "bg": "white", "fg": "black"}
        button_style = {"font": ("Arial", 14, "bold"), "bg": "#007BFF", "fg": "white"}

        # Widgets y botones en la ventana de partida
        self.word_label = tk.Label(master, text="", **label_style)
        self.word_label.pack(pady=20)

        self.attempts_label = tk.Label(master, text="", **small_label_style)
        self.attempts_label.pack(pady=10)

        self.letter_entry = tk.Entry(master, font=("Arial", 16), width=5, justify="center")
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Adivinar", command=self.guess_letter, **button_style)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset_game, **button_style)
        self.reset_button.pack(pady=10)

        # Dibujar la figura del ahorcado
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white", highlightthickness=0)
        self.canvas.create_line(50, 250, 250, 250, width=4)
        self.canvas.create_line(100, 250, 100, 50, width=4)
        self.canvas.create_line(100, 50, 200, 50, width=4)
        self.canvas.create_line(200, 50, 200, 80, width=4)
        self.canvas.pack(pady=10)

        self.update_word_display()
        self.update_attempts_display()

    def update_word_display(self): #Modificar la palabra cuando se acierta una letra
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess])
        self.word_label.config(text=display_word)

    def update_attempts_display(self): #Restar intentos cada intento
        self.attempts_label.config(text=f"Intentos restantes: {self.attempts}")

    def guess_letter(self): #Método que registra cada intento
        letter = self.letter_entry.get().strip().lower()
        if letter and letter not in self.guessed_letters:
            if letter in self.word_to_guess:
                self.guessed_letters.append(letter)
            else:
                self.attempts -= 1

            self.update_word_display()
            self.update_attempts_display()

            if "_" not in self.word_label.cget("text"):
                messagebox.showinfo("¡Victoria!", "¡Has ganado!")
                self.reset_game()
            elif self.attempts <= 0:
                messagebox.showerror("¡Derrota!", f"¡Perdiste! La palabra era: {self.word_to_guess}")
                self.reset_game()

        self.letter_entry.delete(0, tk.END)

    def reset_game(self): #Método para reiniciar la partida con una nueva palabra.
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        self.update_word_display()
        self.update_attempts_display()

if __name__ == "__main__":
    splash = tk.Tk()
    SplashScreen(splash)
    splash.mainloop()
