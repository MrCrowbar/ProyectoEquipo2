# Analizador de sentimientos verbales y escritos. 

#### El código que se encuentra en este repositorio fue desarrollado con la intención de que este fuese utilizado como una herramienta complementaria en tareas de detección temprana de síntomas de depresión. 

Utilizando modelos considerados dentro del estado del arte en el área de procesamiento del lenguaje natural, el modelo resulta útil para analizar tanto fragmentos de texto como de audio. Es capaz de realizar inferencias no solo en base a la semántica del fragmento que esté analizando, sino también en base a otros aspectos relacionados con el habla (tales como la velocidad o el tono), entregando de esta forma resultados más robustos bajo un sistema de carácter redundante (es decir con una doble certeza al momento de análizar fragmentos de sónido).


### Modelos empleados:
* BERT (Representación de Codificador Bidireccional de Transformadores): Este potente modelo para clasificación del lenguaje desarrollado por Google, es la base para nuestro análisis de texto.A este se le hizo pasar por un proceso de afinamiento (fine tuning) para poder utilizarlo como clasificador. 
* M11:  

### Base de datos utilizada: 
Se recurrió a IEMOCAP (Captura de Movimiento Emocional Diádica). Esta base de datos de la Universidad de California del Sur tiene como propósito el reconocimiento y análisis de las expresiones emocionales en diversas interacciones, se basa en interacciones (tanto con guion como interacciones improvisadas) entre un grupo de actores (5 hombres y 5 mujeres).

Esta base de datos cuenta con: 
* Información de la captura de movimiento del rostro. 
* Grabaciones.
* Vídeos.
* Información sobre el ángulo y movimiento de la cabeza. 
* Transcripciones de las interacciones.
* Alineamientos a nivel de palabra, sílaba y fonema. 

El modelo fue entrenado utilizando las transcripciones y grabaciones. 

Para aumentar el volumen de información para entrenamiento, se llevó a cabo procesos para el aumento de datos en ambos níveles. 

### Aumento de datos para audio: 

### Aumento de datos para texto:

## Resultados Obtenidos: 



### Integrantes
* Julio César García
* David Garza
* Gustavo De Los Ríos Alatorre
* Jacobo Cruz


## Entorno de implementación
La implementación del proyecto se encuentra en Google Colab por lo que no es necesario descargar ningún repositorio.
Los archivos necesarios para ejecutar el proyecto se encuentran en esta [carpeta](https://drive.google.com/drive/folders/1f7iqqmGVeLMWsZp_4v4rY02mGnyxDVS6?usp=sharing) compartida.

De igual manera se ha incluído un archivo 'requirements.txt' en el cual se mencionan las bibliotecas necesarias para correr el script. 

## Base de datos
Enlace a la base de datos utilizada: https://sail.usc.edu/iemocap/
