## Universidad de Antioquia 
### Facultad de Ingeniería 
Ingeniería de Telecomunicaciones 
Fabian quiñones Zúñiga , Lilina Marcela Barbosa Esteban

# Optical Modem

Sistema de comunicación óptica visible basado en transmisión Screen-to-Camera (S2C) mediante patrones luminosos mostrados en una pantalla y capturados por una cámara convencional.

El sistema implementa codificación binaria, modulación por colores RGB, detección mediante visión por computador y reconstrucción de mensajes digitales utilizando únicamente hardware de uso cotidiano

# Resumen

Se desarrolló un sistema de comunicación óptica visible capaz de transmitir información digital desde una pantalla de teléfono móvil hacia una cámara convencional.

Inicialmente se implementó una modulación binaria tipo OOK (On-Off Keying) para validar el canal óptico. Posteriormente se evolucionó hacia una modulación RGB multinivel capaz de representar dos bits por símbolo utilizando los colores rojo, verde, azul y blanco.

La arquitectura implementada permite:

* Conversión texto → bits.
* Conversión bits → símbolos RGB.
* Generación automática de tramas.
* Transmisión mediante pantalla.
* Captura mediante webcam convencional.
* Selección de región de interés (ROI).
* Clasificación cromática.
* Reconstrucción automática del mensaje.

Las pruebas experimentales demostraron la recuperación exitosa de mensajes completos como:

HOLA

y

HOLA FABIAN

utilizando transmisión óptica visible.

Posteriormente se implementó una matriz RGB 5×4 capaz de transportar 40 bits por trama equivalentes a 5 caracteres ASCII por frame.

Finalmente se construyó un video de transmisión compuesto por 100 frames y 500 caracteres totales, logrando recuperaciones experimentales superiores al 88% del mensaje original bajo condiciones reales de captura.

# Estado Actual

Implementado:

* Modulación OOK.
* Modulación RGB multinivel.
* Conversión texto → ASCII.
* Conversión ASCII → bits.
* Conversión bits → símbolos RGB.
* Generación automática de frames.
* Generación de mensajes largos.
* Matriz RGB 5×4.
* 20 símbolos por frame.
* 40 bits por frame.
* 5 caracteres por frame.
* Generación automática de 100 frames.
* Construcción de video MP4.
* Transmisión mediante pantalla de teléfono móvil.
* Captura mediante webcam Trust 1080p Full HD.
* Selección manual de ROI.
* Clasificación automática de colores.
* Recuperación automática de caracteres.
* Lectura de video frame a frame.
* Reconstrucción parcial y total de mensajes.

Pendiente:

* Corrección de errores.
* CRC.
* Reed-Solomon.
* Sincronización avanzada.
* Seguimiento automático.
* Detección automática de ROI.
* Calibración automática de color.
* Compensación de exposición.
* Matrices 8×8.
* Matrices 16×16.
* Modulación multinivel adaptativa.

# Arquitectura General

TX

MENSAJE
▼
TEXT_TO_BITS
▼
BITS_TO_RGB
▼
FRAME_BUILDER
▼
DISPLAY
▼
PANTALLA
▼
CANAL ÓPTICO
▼
RX

WEBCAM TRUST 1080P
▼
RoI
▼
EXTRACCIÓN DE CELDAS
▼
CLASIFICACIÓN RGB
▼
RECONSTRUCCIÓN DE BITS
▼
ASCII
▼
MENSAJE

# Estructura del Proyecto

```

pds_proyecto_optico/

├── generar_frames_texto.py
├── generar_frames_rgb_texto.py
├── generar_frame_rgb_prueba.py
├── receptor_multiframe_manual.py
├── receptor_rgb_manual.py
├── rx_video_rgb_5x4.py
├── capturar_frame.py
├── detectar_camaras.py
├── frames_tx/
├── frames_rgb/
├── frames_video_rgb/
├── evidencias/
└── evidencias_finales/

```

# Protocolo OOK

La primera versión del sistema empleó modulación OOK.

```

1 = Blanco
0 = Negro

```

Cada frame representaba un único carácter ASCII.
Flujo:

```

Texto
↓
ASCII
↓
Bits
↓
Pantalla
↓
Cámara
↓
Bits
↓
ASCII
↓
Texto

```

# Protocolo RGB

Posteriormente se implementó modulación RGB de cuatro símbolos.

```
00 = ROJO
01 = VERDE
10 = AZUL
11 = BLANCO

```

Cada símbolo transporta:

```

2 bits

```

incrementando la eficiencia espectral respecto a OOK.

# Matriz RGB 5×4

La versión principal del sistema utiliza una matriz:

```

5 columnas × 4 filas

```

Total de celdas:

```

20 símbolos RGB

```

Capacidad:

```

20 símbolos × 2 bits

=

40 bits

```

Equivalentes a:

```

5 caracteres ASCII por frame

```

# Pipeline del Transmisor

```

Mensaje

↓
text_to_bits()
↓
bits_to_rgb()
↓
build_frame()
↓
frame.png
↓
video.mp4
↓
Pantalla

```

# Pipeline del Receptor

```

Frame
↓
ROI
↓
Extracción de celdas
↓
Promedio BGR
↓
Clasificación RGB
↓
Reconstrucción binaria
↓
ASCII
↓
Mensaje

```

# Clasificación de Colores

La detección se basa en el canal dominante.

```

ROJO  → R dominante

VERDE → G dominante

AZUL  → B dominante

BLANCO → R,G,B altos

```

La clasificación utiliza promedios locales sobre cada celda para aumentar robustez frente a ruido y desenfoque.

# Experimentos

# Experimento 1

Transmisión OOK.

Resultado:

Recuperación correcta de caracteres individuales.

# Experimento 2

Transmisión RGB.

Resultado:

Recuperación correcta de mensajes:

```

HOLA

HOLA FABIAN

```

# Experimento 3

Matriz RGB 5×4.

Resultado:

Recuperación correcta de:

```

HOLA

```

a partir de un único frame.

Capacidad demostrada:

```

5 caracteres por frame

```

# Experimento 4

Video RGB 5×4.

Parámetros:

```

100 frames

10 FPS

10 segundos

500 caracteres

```
# Mapa de Símbolos del Sistema RGB

El sistema implementa una modulación digital de cuatro símbolos.

Cada símbolo representa:

```

log₂(4) = 2 bits

```

Tabla de símbolos:

```

Símbolo S0 → ROJO   → 00

Símbolo S1 → VERDE  → 01

Símbolo S2 → AZUL   → 10

Símbolo S3 → BLANCO → 11

```

# Relación con Modulación M-aria

OOK:

```

M = 2

log₂(M) = 1 bit/símbolo

```

RGB:

```

M = 4

log₂(M) = 2 bits/símbolo

```

Por tanto la eficiencia espectral se duplica.

# Ejemplo de Codificación

Carácter:

```

H

```

Código ASCII:

```

72₁₀

=

01001000₂

```

Agrupando de dos en dos:

```
01 00 10 00

```

Conversión a símbolos:

```
01 → VERDE
00 → ROJO
10 → AZUL
00 → ROJO

```

Representación visual:

```

[VERDE] [ROJO] [AZUL] [ROJO]

```

# Ejemplo con la Palabra HOLA

ASCII:

```

H = 01001000
O = 01001111
L = 01001100
A = 01000001

```

Bits:

```

01001000 01001111 01001100 01000001

```

Símbolos:

```
01 00 10 00
01 00 11 11
01 00 11 00
01 00 00 01

```

RGB:

```
[VERDE] [ROJO] [AZUL] [ROJO]
[VERDE] [ROJO] [BLANCO] [BLANCO]
[VERDE] [ROJO] [BLANCO] [ROJO]
[VERDE] [ROJO] [ROJO] [VERDE]
```

# Modelo de Señal

Transmisor:

```

Texto
↓
ASCII
↓
Bits
↓
Símbolos RGB
↓
Pantalla

```

Canal:

```

Canal Óptico Visible
(VLC)

```

Receptor:

```

Cámara
↓
Clasificador RGB
↓
Bits
↓
ASCII
↓
Texto

```

# Frecuencia de Símbolos
Versión RGB 5×4:

```

20 símbolos/frame

```

Cada símbolo:

```

2 bits

```

Por frame:

```

20 × 2 = 40 bits

```

Equivalente a:

```

5 caracteres ASCII

```

Frecuencia de refresco utilizada:

```

10 FPS

```

Por tanto:
Frecuencia de símbolos:

```

20 símbolos/frame × 10 frame/s
=
200 símbolos/s

```

Tasa binaria:

```

200 símbolos/s × 2 bits/símbolo
=
400 bit/s

```

```
             BLANCO 
             11 
                 *

VERDE                         00
01   *                      *  AZUL
    

             10  *
             ROJO
```

Tasa de caracteres:

```

400 / 8
=
50 caracteres/s

```

# Capacidad Experimental
Video generado:

```

100 frames
10 segundos

```

Capacidad:

```

5 caracteres/frame

×

100 frames

=

500 caracteres

```

Velocidad efectiva:

```

500 caracteres

÷
10 segundos
=
50 caracteres/s

```

# Interpretación desde Telecomunicaciones

OOK:

```

2 símbolos

1 bit/símbolo

```

RGB:

```

4 símbolos
2 bits/símbolo

```

La implementación RGB puede interpretarse como una modulación digital M-aria de cuatro estados, donde los niveles tradicionales de amplitud son sustituidos por símbolos cromáticos diferenciables mediante visión por computador.

Resultado experimental:

# Desarrollo Experimental

El proyecto fue desarrollado de forma incremental, validando cada etapa antes de avanzar hacia una arquitectura más compleja.

# Etapa 1: Modulación OOK

La primera implementación utilizó modulación On-Off Keying (OOK).
En esta etapa cada símbolo transmitía un único bit de información.

```

Negro = 0

Blanco = 1

```

El transmisor generaba imágenes binarias correspondientes a los caracteres del mensaje.

El receptor capturaba cada imagen mediante webcam y reconstruía el carácter recibido a partir de los bits detectados.

Prueba realizada:

```

HOLA FABIAN

```

Resultado:

Recepción correcta del mensaje mediante captura manual frame a frame.

# Etapa 2: Migración a Modulación RGB

Una vez validado el canal óptico binario, se implementó una modulación de cuatro símbolos basada en colores.

```

Rojo   = 00
Verde  = 01
Azul   = 10
Blanco = 11

```

Esta implementación permitió duplicar la capacidad de transmisión.

Mientras que OOK transmite:

```

log₂(2) = 1 bit por símbolo

```

RGB transmite:

```

log₂(4) = 2 bits por símbolo

```

Conceptualmente esta implementación equivale a una modulación digital M-aria de cuatro estados.

Prueba realizada:

```

HOLA FABIAN

```

Resultado:

Recepción correcta mediante clasificación cromática utilizando la webcam USB.

# Etapa 3: Optimización del Hardware de Recepción

Durante las pruebas se observó que la cámara integrada del computador no ofrecía resultados suficientemente estables.

Problemas detectados:

* Baja resolución efectiva.
* Dificultades de enfoque.
* Errores frecuentes de clasificación.
* Distancia máxima reducida.

Como solución se incorporó una webcam USB Trust 1080p Full HD.

Resultado:

```

Distancia de recepción estable ≈ 1 metro

```

La nueva cámara permitió mejorar significativamente la calidad de la recepción y la robustez del sistema.

# Etapa 4: Incremento de Capacidad mediante Matriz RGB 5×4

Con el canal RGB validado se diseñó una matriz de transmisión compuesta por:

```

5 columnas × 4 filas

```

Total:

```

20 símbolos RGB por frame

```

Capacidad:

```

20 símbolos × 2 bits = 40 bits

```

Equivalentes a:

```

5 caracteres ASCII por frame

```

Diseño:

```
[ c1 ][ c2 ][ c3 ][ c4 ][ c5 ]
[ c6 ][ c7 ][ c8 ][ c9 ][ c10]
[ c11][ c12][ c13][ c14][ c15]
[ c16][ c17][ c18][ c19][ c20]

```

Esta arquitectura permitió incrementar considerablemente la cantidad de información transmitida por imagen.
Prueba realizada:
Recuperación correcta de:

```

HOLA

```

utilizando un único frame RGB 5×4.

Resultado:

```

5 caracteres recuperados en una sola captura

```

# Etapa 5: Transmisión de Video

Una vez validado el funcionamiento de la matriz RGB 5×4 se desarrolló un generador automático de secuencias.
Archivo principal:

```

tx_rgb_5x4.py

```

Se generó una secuencia de:

```

100 frames

```

transportando:

```

500 caracteres

```

Posteriormente los frames fueron convertidos en un video MP4.
Parámetros:

```

100 frames
10 FPS
10 segundos
500 caracteres

```

# Fundamentación Teórica
La capacidad teórica se obtiene de:

```

20 celdas × 2 bits = 40 bits/frame

```

y considerando:

```

1 carácter ASCII = 8 bits

```

entonces:

```

40 bits ÷ 8 = 5 caracteres/frame

```

Finalmente:

```

5 caracteres/frame
×
10 FPS
×
10 segundos
=
500 caracteres

```

# Etapa 6: Recepción Automática de Video

Se desarrolló un receptor capaz de procesar automáticamente secuencias RGB.
Archivo principal:

```

rx_video_rgb_5x4.py

```

Funciones implementadas:
* Selección de ROI.
* Captura automática.
* Clasificación RGB.
* Reconstrucción binaria.
* Conversión ASCII.
* Acumulación automática de mensajes.

Resultados experimentales:
Prueba 1:

```

88 frames detectados
440 caracteres recuperados

```

Prueba 2:

```

100 frames detectados
500 caracteres recuperados

```

Durante la segunda prueba aparecieron errores de clasificación asociados a:

* Variaciones de iluminación.
* Enfoque imperfecto.
* Saturación de color.
* Sincronización temporal.

Sin embargo, se logró demostrar experimentalmente la recepción de la totalidad de los frames transmitidos.

# Etapa 7: Diseño Experimental 4×4

Con el objetivo de aumentar la robustez frente a errores de color se propuso una arquitectura alternativa:

```

4 × 4

```

La motivación principal consiste en:

* Celdas más grandes.
* Mayor separación entre símbolos.
* Menor interferencia cromática.
* Mejor tolerancia al desenfoque.

Capacidad:

```

16 símbolos × 2 bits
=
32 bits/frame
=
4 caracteres/frame

```

Aunque reduce la velocidad de transmisión respecto a la matriz 5×4, se espera una mejora significativa en confiabilidad y tasa de error.

# Lecciones Aprendidas

El desarrollo experimental permitió verificar que:

* La modulación RGB incrementa significativamente la capacidad de transmisión.
* La calidad óptica de la cámara es determinante.
* La sincronización entre reproducción y captura es crítica.
* El tamaño de las celdas influye directamente en la tasa de error.
* Existe un compromiso natural entre velocidad y robustez.

Los resultados obtenidos constituyen una validación práctica de los principios fundamentales de las comunicaciones digitales aplicados a un canal óptico visible de bajo costo.


```

100 frames detectados
500 caracteres recibidos
Recuperación parcial con errores debidos a clasificación cromática y sincronización temporal.

```

# Limitaciones

* Sensibilidad a iluminación ambiente.
* Dependencia del enfoque de la cámara.
* Saturación de colores.
* Variaciones de exposición automática.
* Errores de clasificación RGB.
* Dependencia de la selección manual de ROI.
* Pérdida de información por diferencias entre FPS de captura y reproducción.

# Trabajo Futuro

* Calibración automática de color.
* Corrección de errores Reed-Solomon.
* CRC.
* Sincronización avanzada.
* ROI automática.
* Seguimiento del transmisor.
* Modulación multinivel adaptativa.
* Matrices 8×8.
* Matrices 16×16.
* Optimización para transmisión en tiempo real.
* Estimación de BER.
* Evaluación de distancia máxima de transmisión.

# Conclusiones

El sistema desarrollado demuestra la viabilidad de implementar un canal de comunicación óptica visible utilizando únicamente una pantalla convencional y una cámara comercial.

La evolución desde una modulación OOK básica hasta una arquitectura RGB 5×4 permitió aumentar significativamente la capacidad de transmisión, alcanzando 40 bits por frame equivalentes a 5 caracteres ASCII.

Las pruebas experimentales permitieron transmitir y recuperar mensajes completos como HOLA y HOLA FABIAN, así como construir una transmisión de 500 caracteres distribuida en 100 frames y 10 segundos de duración.

Los resultados obtenidos constituyen una base sólida para futuras investigaciones en sistemas Screen-to-Camera de bajo costo orientados a comunicaciones ópticas visibles y procesamiento digital de señales.
