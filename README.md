# JUEGO_DE_LA_VIDA
Resumen: Este es un proyecto para la materia de programación donde tuvimos como objetivo programar el juego de la vida,creado por John Horton Conway en 1970, la elaboracion del mismo se llevo a cabo en tres etapas cuyas tareas fueron divididas de la siguiente manera entre las 3 integrantes del equipo ; 

Daniela Guzman Morales:Elaboración del tablero. 

Karen Gisela Rochin Sandoval:Establecimiento de las reglas del juego.

Estrella Yanet Mendez Reyes: Creación del Interfaz con ayuda de streamlit. 

La necesidades que aborda el juego es comprender el funcionamiento de sistemas células, simular procesos de supervivencia y muerte, observar como reglas simples generan comportamientos complejos, y a su vez aplicar conocimientos matematicos y de programación. 

---Objetivos--- 
General: El objetivo general de este proyecto es aprender a elaborar el juego de la vida con ayuda de codigo a través de Python, entender la lógica detrás de las reglas del juego y aplicar modulos y codigo para ejecutar de manera satisfactoria el juego, incentivar el aprendizaje autónomo de nuestra parte mediante la investigación.

•	Programar el juego de la vida, 
•	Entender la lógica detrás de las reglas del juego y aplicarlas a los módulos y código correspondiente.
•	Programar la animación del juego con ayuda de Streamlit.

Particular: Aprender el funcionamiento de nuevos programas y módulos implementables al funcionamiento del juego, incentivar el aprendizaje autónomo mediante la resolución de problemas (creación del juego). 

Intrucciones de instalación y ejecución:

1- Abrir la liga del repositorio en tu navegador. 


2- Crear una copia del repositorio en tu dispositivo.


<img width="328" height="269" alt="image" src="https://github.com/user-attachments/assets/25079716-4eb6-414a-a734-7a49fb83f007" />

Lo puedes hacer desde la terminal poniendo;
   git clone URL DEL REPOSITORIO
   
O descagando la carpeta como archivo zip y posteriormente descompromiendoló en tu dispositivo.


3- Abre el archivo JUEGO_VIDA.py desde tu terminal y coloca lo siguiente:

     streamlit run JUEGO_VIDA.py
     
     
4- Pon ENTER


5- Se abrirá una pantalla en streamlit con el juego :)


<img width="625" height="396" alt="image" src="https://github.com/user-attachments/assets/9763bd6d-d086-4434-a9e8-37f0098c1ebc" />

---Explicación de la solución--- 
- TABLERO

Para comprender mejor el funcionamiento de este código partiremos de una idea general: tablero de ajedrez con luces. Si lo imaginamos de esa manera, podemos notar que es un tablero enorme, de 40 filas por 60 columnas y cada casilla tiene un foco que solo puede estar:
-	Apagado (0) que es una célula muerta
-	Encendido (1) que es una célula viva

Esta parte del código que consiste en crear el Tablero hace una sola cosa: crear ese tablero de focos para que el resto del programa tenga con qué trabajar. El código se guarda como una matriz, que es una tabla de números con filas y columnas, como una hoja de Excel.
0 0 0 0 0
0 1 0 0 0
0 0 1 1 0
Las dos funciones que realicé:
Paso 1:
-	Crear_tablero_vacio(): el tablero en blanco 
np.zeroa ((FILAS, COLUMNAS), dtype=int)

En español se puede interpretar como: “crea una tabla de 40x60 llena de ceros”, es decir, todos los focos están apagados.
El dtype=int solo le dice a Python que use números enteros (0) y no decimales como (0.0).
Además, que el botón Limpiar borra todo y deja todo el tablero vacío.

Paso 2:
-	Crear_tablero_aleatorio(): el tablero con vida al azar 
(np.random.random.((FILAS, COLUMNAS)) <0.25). astype(int)

Esta línea es un poco más densa, por lo que es importante explicar cada componente. 
En np.random.random(…) le pone a cada casilla un número al azar entre 0y 1, por ejemplo 0.83, 0.12, 0.57.
En <0.25 es una pregunta que se le hace a cada casilla: “¿Tu número es menor a 0.25?”. Si la respuesta es Sí, la casilla queda en True, si es No queda False. Como la cuarta parte de los números cae por debajo de 0.25, más o menos 1 de cada 4 casillas sale verdadera.

En la parte .astype(int) traduce True a 1 y False a 0, para volver a tener un tablero de ceros y unos.Este paso tiene como objetivo que el tablero arranque el juego y el botón Aleatorio.
Prácticamente podemos decir que 0,25 “Es como decir que cada célula tiene 25% de probabilidad de nacer viva”.Mi parte crea el tablero: una tabla de 40x60 con ceros y unos, donde 0 es una célula muerta y 1 una viva. Puede empezar completamente vacía o con células vivas repartidas al azar.

  
- REGLAS
  
Es importante partir de la siguiente lógica una célula sobrevive si tiene 2 o 3 vecinas, Al inicio del código importamos la librería NumPy que sirve para crear arreglos (arreys) que funcionan como matrices, el tablero del juego en si es una matriz, lo que tuvimos que hacer en esta parte fue adecuar la matriz a las reglas del juego 
1 = célula viva 
0= célula muerta 
Si una célula está viva y sus células vecinas son 0 o 1, la célula muere
Si una célula esta viva y tiene 2 o 3 vecinas esa célula permanece viva.
Si una célula esta viva y tiene mas de 4 vecinos vivos, muere 
Nace una célula cuando hay 3 células vecinas.
Cualquier otra combinación, la célula muere.
Una célula muerta nace si tiene exactamente 3 vecinas.
Partiendo de esa idea generamos la primera función, un contador de células, vecinas en la matriz (en 8 direcciones), esto por medio de la siguiente matriz; 
vecinos = (
        p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:]  Esto corresponde a la fila de arriba (3)
        + p[1:-1, :-2] + p[1:-1, 2:]           Esto corresponde a los movimientos de izquierda y derecha (2)
        + p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:]     Y finalmente esto corresponde a la fila de abajo (3)
    )  
P= np.pad al inicio es una librería de NumPy que nos va a permitir construir los bordes de la matriz,  también se le conoce como relleno del arreglo o matriz. 
Para la función dos de esta parte del código, establecemos cuando es que una célula vive y cuando es que una  célula muere 
En esta parte decimos que una célula viva (igualada a 1 por la condición de viva=1)
tiene 2 o 3 vecinas: (tablero == 1) & ((vecinos == 2) | (vecinos == 3))
Después establecemos que una célula nace cuando: (tablero == 0) & (vecinos == 3), que sería la condición de que para que nazca una célula debe haber 3 celulas vecinas, por ello, vecinos = 3 y tablero =0 porque partimos de una célula muerta con 3 células vecinas vivas.
Por último usamos .astype(int) que convierte un valor, columna o conjunto de datos en un valor entero (0 o 1) , para que se cumpla la condición en las siguientes generaciones y entender si están vivas o nacen, la muerte al considerarse 0, no cumple ninguna condición, simplemente no aparece.


- INTERFAZ

Mi contribución al proyecto fue el desarrollo de la parte visual e interactiva del Juego de la Vida, que es en donde se conectan la parte 1 (tablero) y  2 (reglas) del código con un interfaz (es el medio mediante el cual el usuario puede interactuar con un programa) que permite así al usuario visualizar y controlar la simulación. Para lograrlo utilice la biblioteca Streamlit que es la que permite la creación de aplicaciones web en Python. Las principales funciones fueron:

•	Integre los modulos 1 y 2 (Tablero y Reglas) para así no repetir instrucciones.

•	Utilice una función llamada tablero_a_imagen, que transforma los valores 0 y 1 en colores para así poder representar las células vivas    y muertas.

•	Agregue un título, el tablero y los controles para que el usuario pueda interactuar. 

•	Utilice st.session.state para así poder conservar la información de el tablero, la generación y si el juego esta activo o en pausa.

•	Incorpore las opciones de iniciar, pausar, avanzar un paso, generar un tablero aleatorio y limpiar.

•	Por último, utilice sleep() y st.rerun() para actualizar automáticamente el tablero mientras la simulación esta activa.

Con todo esto logre que el Juego de la Vida no solamente realizara los cálculos intermitentes, sino que también pudiera visualizarse y manipularse de manera sencilla por el usuario.




Nos guiamos del siguiente video: https://youtu.be/qPtKv9fSHZY
para entender el funcionamiento del juego. Así de como también de la IA para entender la lógica de algunos modulos y líbrerias.




