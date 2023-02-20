### Sombrero seleccionador reto ###

gryffindor = 0 
slytherin = 0
ravenclaw = 0
hufflepuff = 0
muggle = 0 

print("🧙🏽 🧙‍♀️ 🧙🏿‍♂️ Sombrero Seleccionador de Hogwarts  🧙🏻‍♂️ 🧙🏼‍♀️ 🧙🏽‍♂️")
print("           🦁🦅🦡🐍 🦅🦁🐍🦡 🦡🦁🐍🦅 🐍🦁🦅🦡   ")

#### Primera pregunta

print("I: ¿Qué momento del día te gusta más? ")
print(" 1.- Amanecer ")
print(" 2.- Medio dia ")
print(" 3.- Atardecer ")
print(" 4.- Anochecer ")
print(" 5.- Madrugada ")




answer = int(input("Elija de 1 a 5: ")) 

if answer == 1:
        muggle += 1

elif answer == 2:
        hufflepuff += 1

elif answer == 3:
        ravenclaw += 1

elif answer == 4:
        gryffindor += 1

elif answer == 5:
        slytherin == 1

else:
    print("Squid")


        

## Segunda pregunta

print("II: ¿Qué animal te gusta más? ")
print(" 1.- Dragón ")
print(" 2.- Hipogrifo ")
print(" 3.- Unicornio ")
print(" 4.- Tiburón ")
print(" 5.- Fénix ")

answer = int(input("Elija de 1 a 5: "))

if answer == 1:
        slytherin += 2

elif answer == 2:
        gryffindor += 2

elif answer == 3:
        hufflepuff += 2

elif answer == 4:
        muggle += 2
    
elif answer == 5:
        ravenclaw == 2

else:
    print("Wrong")

#### Tercera pregunta

print("IV: ¿Cómo te gustaría pasar tus fines de semana? ")
print(" 1.- Con unos buenos amigos y cervezas de mantequilla ")
print(" 2.- Practicando mis habilidades de Quidditch ")
print(" 3.- Montando una bicicleta ")
print(" 4.- Con un libro en la biblioteca ")
print(" 5.- Haciendo relaciones con los profesores")

answer = int(input("Elija de 1 a 5: "))


if answer == 1:
    hufflepuff += 3

elif answer == 2: 
    gryffindor += 3

elif answer == 3:
    muggle += 3

elif answer == 4:
    ravenclaw += 3

elif answer == 5:
    slytherin += 3

else:
    ("Repitelo Squid…")

#### Cuarta pregunta

print("V: ¿Cuál hechizo o encantamiento prefieres ")
print(" 1.- ¡EXPELIARMUS! ")
print(" 2.- ¡AVADA KADABRA! ")
print(" 3.- ¡ANAPNEO! ")
print(" 4.- Usar una pala ")
print(" 5.- ¡OBLIVIATE! ")

answer = int(input("Elija de 1 a 5: "))

if answer == 1:
    gryffindor += 4

elif answer == 2:
    slytherin += 4

elif answer == 3:
    hufflepuff += 4

elif answer == 4:
    muggle += 4

elif answer == 5:
    ravenclaw += 4

else:
    ("Repitelo Squid…")

##### Quinta pregunta

print("V: ¿Cuál es tu medio de transporte favorito? ")
print(" 1.- Aparición ")
print(" 2.- Chimenea ")
print(" 3.- Automovil ")
print(" 4.- Escoba ")
print(" 5.- Carruaje")

answer = int (input("Elija de 1 a 5: "))

if answer == 1:
    ravenclaw += 5

elif answer == 2:
    hufflepuff += 5

elif answer == 3:
    muggle += 5

elif answer == 4:
    gryffindor += 5

elif answer == 5:
    slytherin += 5

else:
    print("Repitelo Squid ")


# Resultados

if gryffindor >= slytherin and gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= muggle:
    print("🦁🦁🦁🦁 ¡¡¡¡¡ Gryffindor!!!!! 🦁🦁🦁🦁")

elif slytherin >= ravenclaw and slytherin >= hufflepuff and slice >= muggle:
    print("🐍🐍🐍🐍 ¡¡¡¡¡¡ Slytherin !!!!! 🐍🐍🐍🐍")

elif ravenclaw >= hufflepuff and ravenclaw >= muggle:
    print("🦅🦅🦅🦅 ¡¡¡¡¡¡ Ravenclaw !!!!! 🦅🦅🦅🦅")

elif hufflepuff >= muggle:
    print("🦡🦡🦡🦡 ¡¡¡¡¡Hufflepuff!!!!!! 🦡🦡🦡🦡")

else:
    print("Eres un Muggle… ¡EXPULSADO!")
 














