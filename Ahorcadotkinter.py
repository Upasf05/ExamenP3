import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("¡Ahorcado!")
        self.master.geometry("400x450")
        
        self.words = [
            "amor", "agua", "arbol", "amigo", "casa", "cielo", "ciudad", "comida", "corazon", "dinero",
            "dia", "escuela", "familia", "felicidad", "fiesta", "flor", "fuego", "gente", "guerra", "historia",
            "hombre", "jardin", "juego", "libro", "luz", "mañana", "mujer", "mundo", "niño", "noche",
            "nube", "paz", "pelicula", "perro", "persona", "plaza", "rio", "rojo", "salud", "semana",
            "sol", "tarde", "tierra", "trabajo", "tren", "universo", "viento", "vida", "viaje", "zapato",
            "aire", "amistad", "camino", "cancion", "corona", "destino", "espacio", "estrella", "futuro", "grito",
            "hora", "invierno", "isla", "juguete", "lluvia", "luna", "mar", "memoria", "montaña", "musica",
            "nieve", "niña", "oceano", "otoño", "palabra", "piedra", "puerta", "raton", "recuerdo", "risa",
            "silencio", "sueño", "templo", "tesoro", "trueno", "verano", "verdad", "ventana", "viento", "voz",
            "camisa", "estrella", "madera", "parque", "solucion", "cultura", "ciudadano", "felicidad", "lenguaje", "nacion"
]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        
        self.word_label = tk.Label(master, text="", font=("Arial", 24))
        self.attempts_label = tk.Label(master, text="", font=("Arial", 16))
        self.letter_entry = tk.Entry(master, width=5, font=("Arial", 16))
        self.guess_button = tk.Button(master, text="Adivinar", command=self.guess_letter)
        self.reset_button = tk.Button(master, text="Reiniciar", command=self.reset_game)
        self.canvas = tk.Canvas(master, width=300, height=300)

        # Setup UI
        self.canvas.create_line(50, 250, 250, 250, width=4)  # Base
        self.canvas.create_line(100, 250, 100, 50, width=4)  # Poste vertical
        self.canvas.create_line(100, 50, 200, 50, width=4)   # Poste horizontal
        self.canvas.create_line(200, 50, 200, 80, width=4)   # Cuerda
        self.canvas.pack()
        
        self.word_label.pack()
        self.attempts_label.pack()
        self.letter_entry.pack()
        self.guess_button.pack()
        self.reset_button.pack()
        
        self.update_word_display()
        self.update_attempts_display()
        self.draw_hangman()
        
    def is_game_over(self):
        return self.check_win() or self.check_loss()
    
    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word_to_guess)
    
    def check_loss(self):
        return self.attempts == 0
    
    def guess_letter(self):
        letter = self.letter_entry.get().lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in self.guessed_letters:
                messagebox.showinfo("Ahorcado", "Ya está esa letra")
            elif letter in self.word_to_guess:
                self.guessed_letters.append(letter)
                self.update_word_display()
                if self.check_win():
                    messagebox.showinfo("Ahorcado", "¡Has ganado!")
                    self.reset_game()
            else:
                self.guessed_letters.append(letter)
                self.attempts -= 1
                self.update_attempts_display()
                self.draw_hangman()
                if self.check_loss():
                    messagebox.showinfo("Ahorcado", "Has perdido, la palabra era: " + self.word_to_guess)
                    self.reset_game()
            self.letter_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Ahorcado", "Por favor, introduce una sola letra.")
    
    def reset_game(self):
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        self.update_word_display()
        self.update_attempts_display()
        self.draw_hangman()
    
    def update_word_display(self):
        display_word = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
            display_word += " "
        self.word_label.config(text=display_word)
    
    def update_attempts_display(self):
        self.attempts_label.config(text=f"Intentos: {self.attempts}")
    
    def draw_hangman(self):
        self.canvas.delete("hangman")
        if self.attempts < 6:
            self.canvas.create_oval(180, 80, 220, 120, width=4, tags="hangman")  # Cabeza
        if self.attempts < 5:
            self.canvas.create_line(200, 120, 200, 180, width=4, tags="hangman")  # Cuerpo
        if self.attempts < 4:
            self.canvas.create_line(200, 140, 180, 160, width=4, tags="hangman")  # Brazo izquierdo
        if self.attempts < 3:
            self.canvas.create_line(200, 140, 220, 160, width=4, tags="hangman")  # Brazo derecho
        if self.attempts < 2:
            self.canvas.create_line(200, 180, 180, 220, width=4, tags="hangman")  # Pierna izquierda
        if self.attempts < 1:
            self.canvas.create_line(200, 180, 220, 220, width=4, tags="hangman")  # Pierna derecha

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()