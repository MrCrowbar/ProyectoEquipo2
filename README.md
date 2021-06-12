# Analizador de sentimientos verbales y escritos. 

#### El código que se encuentra en este repositorio fue desarrollado con la intención de que este fuese utilizado como una herramienta complementaria en tareas de detección temprana de síntomas de depresión. La versión de Python utilizada, fue la 3.7.10.

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
Se utilizó TorchAudio y sox para modificar ciertos aspectos de los audios muestra tales como la velocidad o el tono y de esta forma, generar nuevos datos. 
### Aumento de datos para texto:
Se utilizó la biblioteca NLP AUG, la cual nos permitió utilizar BERT para generar nuevas oraciones para el Dataset de Texto. 
## Resultados Obtenidos: 
Se logró acumular un total de 9000 datos dentro de un Dataset balanceado en el área de texto. 
Se complementaron los fragmentos de audio originales de IEMOCAP para proveer una base robusta de entrenamiento para el modelo M11. 

Se logró conseguir resultados de hasta 80% de precisión tanto con el módulo de análisis de BERT como con M11, dando como resultado un sistema capaz de analizar entradas de audio y texto (o pasar una entrada de audio a texto), analizando tanto los aspectos semánticos como los aspectos auditivos de las entradas. 

Para visualizar los resultados de forma más gráfica, hemos plasmado nuestros resultados y motivos detrás de este trabajo en el siguiente [póster académico](https://drive.google.com/file/d/16whBIQsrSBjzAK8Jcwbz-kL9XE8Cowzr/view?usp=sharing) 


### Integrantes
* Julio César García
* David Garza
* Gustavo De Los Ríos Alatorre
* Jacobo Cruz


## Entorno de implementación
La implementación del proyecto se encuentra en Google Colab por lo que no es necesario descargar ningún repositorio.
Los archivos necesarios para ejecutar el proyecto se encuentran en esta [carpeta](https://drive.google.com/drive/folders/1f7iqqmGVeLMWsZp_4v4rY02mGnyxDVS6?usp=sharing) compartida.

De igual manera se ha incluído un archivo 'requirements.txt' en el cual se mencionan las bibliotecas necesarias para correr el script. 

## OBSERVACIONES EXTRAS
Al inicio del COLAB viene la estructura del programa. *NO* se deben ejecutar todas las celdas puesto que la ejecución de Colab se queda sin memoria RAM y truena. La mayoría de las celdas son el compendio de todo el proceso que se llevó a cabo, el objetivo es ilustrar los pasos necesarios.
Con que se incluyan las librerías y utilerías se pueden pasar directamente a la parte de inferencias con los mejores pesos que se obtuvieron.

## Base de datos
Enlace a la base de datos utilizada: https://sail.usc.edu/iemocap/
