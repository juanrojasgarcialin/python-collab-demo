import random
import sys
import os

# ANSI color codes (common ones)
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"
COLOR_BLACK = "\033[30m"


def colored(text, color):
    return f"{color}{text}{COLOR_RESET}"


def greet():
    """Ask for user's name and greet them."""
    name = input("¿Cómo te llamas? ").strip()
    if not name:
        name = "amigo"
    print(colored(f"¡Hola, {name}! Bienvenido al demo de colaboración.", COLOR_CYAN))


def guess_the_number():
    """Simple number guessing game with 3 attempts."""
    print(colored("Estoy pensando en un número del 1 al 10. Tienes 3 intentos.", COLOR_YELLOW))
    secret_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            attempt = int(input("Ingresa un número: "))
        except ValueError:
            print(colored("Introduce un número válido.", COLOR_RED))
            continue

        if attempt == secret_number:
            print(colored("¡Correcto! Adivinaste el número.", COLOR_GREEN))
            return
        elif attempt < secret_number:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        attempts -= 1
        print(f"Te quedan {attempts} intentos.\n")

    print(colored(f"Se acabaron los intentos. El número era {secret_number}.", COLOR_RED))


def random_compliment():
    """Print a random friendly compliment."""
    compliments = [
        "Tienes una gran sonrisa.",
        "Eres una persona muy creativa.",
        "Tu curiosidad es inspiradora.",
        "Tienes buenas ideas.",
        "Hoy es un gran día para ti.",
    ]
    print(colored(random.choice(compliments), COLOR_GREEN))


def ascii_banner():
    """Show a small ASCII banner from user text."""
    text = input("Texto para banner (ej: Hola): ").strip()
    if not text:
        text = "Hola"
    # Simple big letters made from stars (very small)
    print(colored("\n" + "* " * (len(text) * 2), COLOR_YELLOW))
    print(colored(f"* {text} *", COLOR_CYAN))
    print(colored("" + "* " * (len(text) * 2) + "\n", COLOR_YELLOW))


def mad_libs():
    """Very small mad-libs style sentence generator."""
    noun = input("Dame un sustantivo: ").strip() or "programa"
    verb = input("Dame un verbo (infinitivo): ").strip() or "correr"
    adjective = input("Dame un adjetivo: ").strip() or "rápido"
    sentence = f"El {noun} puede {verb} muy {adjective} cuando hay café."
    print(colored(sentence, COLOR_CYAN))


def rock_paper_scissors():
    """Play rock-paper-scissors against the computer."""
    choices = ["piedra", "papel", "tijeras"]
    print("Juguemos Piedra-Papel-Tijeras. Escribe 'salir' para volver al menú.")
    while True:
        player = input("Tu elección: ").strip().lower()
        if player == "salir":
            return
        if player not in choices:
            print("Elección inválida. Elige piedra, papel o tijeras.")
            continue
        comp = random.choice(choices)
        print(f"Computadora eligió: {comp}")
        if player == comp:
            print(colored("Empate.", COLOR_YELLOW))
        elif (player == "piedra" and comp == "tijeras") or (player == "papel" and comp == "piedra") or (player == "tijeras" and comp == "papel"):
            print(colored("¡Ganaste!", COLOR_GREEN))
        else:
            print(colored("Perdiste.", COLOR_RED))


def show_program_info():
    """Show information about the program."""
    print(colored("=== Información del Programa ===", COLOR_GREEN))
    print("Proyecto: Python Collab Demo")
    print("Descripción: Demo interactivo con mini-juegos y opciones creativas.")
    print("Autor: Juan (o tu nombre aquí)")


def show_menu():
    """Display main menu with creative options."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Saludar")
        print("2. Adivina el número")
        print("3. Cumplido aleatorio")
        print("4. Banner ASCII")
        print("5. Mad Libs rápido")
        print("6. Piedra-Papel-Tijeras")
        print("7. Info del programa")
        print("8. Salir")

        choice = input("Elige una opción (1-8): ").strip()

        if choice == "1":
            greet()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            random_compliment()
        elif choice == "4":
            ascii_banner()
        elif choice == "5":
            mad_libs()
        elif choice == "6":
            rock_paper_scissors()
        elif choice == "7":
            show_program_info()
        elif choice == "8":
            print(colored("¡Adiós!", COLOR_YELLOW))
            break
        else:
            print(colored("Opción inválida. Intenta de nuevo.", COLOR_RED))


if __name__ == "__main__":
    show_menu()