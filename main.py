import random

# Definir las imágenes de las opciones
opciones = {
    0: {"nombre": "Piedra", "imagen": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''},
    1: {"nombre": "Papel", "imagen": '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    '''},
    2: {"nombre": "Tijeras", "imagen": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''},
    3: {"nombre": "Spock", "imagen": '''
        _______
    ---'   ____)__
                  )
            ---˙˙˙
            ---..._
            _______)
    ---.__________)
    '''},
    
    4: {"nombre": "Lagarto", "imagen": '''
         / \_
       /     \___
      /          |
     /    _______/
    /_____/ 
    '''},
    5: {"nombre": "Papa", "imagen": '''
        ____
    ---' |  |________
          |  | ______)
           |_/_______)
          (____)
    ---.__(___)
    '''},
    6: {"nombre": "Heavy", "imagen": '''
        _______
    ---'   ____)___
            _______)
           (____)
           (____)_
    ---.__________)
    '''}
}

# Definir las reglas del juego
reglas = {
    (0, 2): "Piedra aplasta Tijeras",
    (2, 1): "Tijeras cortan Papel",
    (1, 0): "Papel cubre Piedra",
    (0, 4): "Piedra aplasta Lagarto",
    (4, 3): "Lagarto envenena Spock",
    (3, 2): "Spock rompe Tijeras",
    (2, 4): "Tijeras decapitan Lagarto",
    (4, 1): "Lagarto come Papel",
    (1, 3): "Papel desautoriza Spock",
    (3, 0): "Spock vaporiza Piedra",
    (0, 5): "Piedra aplasta Papa",
    (5, 6): "Papa cocina Heavy",
    (6, 3): "Heavy aplasta Spock",
    (3, 5): "Spock vaporiza Papa",
    (5, 2): "Papa destruye Tijeras",
    (2, 6): "Tijeras cortan Heavy",
    (6, 4): "Heavy aplasta Lagarto",
    (4, 5): "Lagarto envenena Papa",
    (5, 0): "Papa destruye Piedra",
}

# Solicitar al usuario que elija una opción
while True:
    usuario = input("¿Qué eliges?\n0 - Piedra\n1 - Papel\n2 - Tijeras\n3 - Spock\n4 - Lagarto\n5 - Papa\n6 - Heavy\nEscribe el número de la opción: ")
    if usuario in ['0', '1', '2', '3', '4', '5', '6']:
        usuario = int(usuario)
        break
    else:
        print("Entrada inválida. Por favor, ingresa un número válido.")

print(f"Tu elección: {opciones[usuario]['nombre']}")
print("Tu imagen:")
print(opciones[usuario]["imagen"])

# Generar la elección aleatoria de la computadora
computadora = random.randint(0, 6)
print(f"Computadora: {opciones[computadora]['nombre']}")
print("Imagen de la Computadora:")
print(opciones[computadora]["imagen"])

# Determinar el resultado del juego
if usuario == computadora:
    print("Empate")
elif (usuario, computadora) in reglas:
    print(f"{opciones[usuario]['nombre']} {reglas[(usuario, computadora)]} {opciones[computadora]['nombre']}. ¡Tú ganas!")
else:
    print(f"{opciones[computadora]['nombre']} {reglas[(computadora, usuario)]} {opciones[usuario]['nombre']}. ¡Tú pierdes!")
