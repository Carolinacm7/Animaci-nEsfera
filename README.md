# Animación Esfera
1. Haciendo uso de la Librería PyGame, construir una animación de
una esfera que controlado por el teclado que se traslade del punto A al punto B, superando el obstáculo que se interpone en el trayecto. Tener
en cuenta los siguientes requerimientos:
a. La esfera se mueve del recuadro delimitado.
b. Al iniciar la aplicación, la esfera se ubicará automáticamente en el
punto A. Para finalizar la aplicación, la esfera debe tocar el punto
B. Cuando la esfera alcance el punto B, la aplicación emitirá el
mensaje 'Objetivo Alcanzado' y se ofrece al usuario la opción de
reiniciar la animación. Si el usuario elige reiniciar, la esfera
volverá automáticamente a la posición inicial. El punto Ay B es un
cuadrado de 50X50 Píxeles.
c. La esfera se mueve en la dirección indicada por la tecla de flecha
presionada por el usuario así:
Tabla No. 1 Nombre de la tecla de dirección en PyGame y efecto
en la animación.
Nombre de la Tecla en
PyGame
Movimiento de la esfera al
presionar:
K_UP Arriba
K_DOWN Abajo
K_RIGHT Derecha
K_LEFT Izquierda
Fuente: El autor.
d. Cuando el usuario no presiona ninguna tecla o no corresponde a
las teclas de dirección la esfera se detiene.
e. Si la esfera colisiona con el obstáculo o con los bordes del marco,
se detiene hasta que el usuario cambie su dirección utilizando las
teclas de flecha.
f. El obstáculo debe estar ubicado en la parte inferior del marco,
centrado horizontalmente, y ocupar el 90% de la altura.
g. En el marco en un espacio libre escribir los nombres y apellidos
del autor.
2. Utilizando las bibliotecas necesarias de Python, implemente un
cronómetro con hilos que se visualice en la interfaz gráfica. Este
cronómetro debe medir el tiempo que tarda el usuario en mover la
esfera desde el punto A hasta el punto B. Cuando la esfera alcance
el punto B, el cronómetro debe detenerse. Al iniciar una nueva
animación, el cronómetro debe reiniciarse a 00:00:00.

