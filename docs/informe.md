#			# Sistema de Laboratorio de Modulaciones Digitales

## Este documento contiene los informes de laboratorio de las modulaciones digitales:
- ASK
- FSK
- PSK

## Objetivos

- Comprender las modulaciones digitales básicas
- Implementar transmisores y receptores
- Simular un canal inalámbrico
- Analizar BER
- Comparar desempeño frente al ruido

--------------------------------------------------

# 1. ASK — Amplitude Shift Keying

## Introducción

La modulación ASK transmite información digital modificando la amplitud de una señal portadora sinusoidal.

En este sistema:

- bit 0 → amplitud baja
- bit 1 → amplitud alta

La frecuencia y la fase permanecen constantes.

## Modelo matemático

$$
s_i(t)=A_i cos(2πf_c t)
$$

donde:

- A_i = amplitud asociada al bit
- f_c = frecuencia portadora

## Arquitectura del sistema


```text
BitStream
   ↓
ASK Modulator
   ↓
Power Amplifier
   ↓
TX Antenna
   ↓
Wireless Channel
   ↓
RX Antenna
   ↓
RF Front-End
   ↓
ASK Demodulator
   ↓
Bit Decoder
   ↓
BER Analyzer
```

## Canal inalámbrico

El canal implementa:

atenuación
delay
ruido AWGN

Modelo:

$$
r(t)=αs(t-τ)+n(t)
$$

donde:

α = atenuación
τ = delay
n(t) = ruido gaussiano

## Demodulación

El receptor detecta amplitud o energía.

$$
E = Σ |r(t)|
$$

y compara contra un umbral.

## Ventajas

implementación sencilla
bajo costo computacional
fácil análisis académico

## Desventajas

alta sensibilidad al ruido
poca robustez

# 2. FSK — Frequency Shift Keying

## Introducción

La modulación FSK transmite información modificando la frecuencia de la portadora.

Cada bit usa una frecuencia distinta.

## Modelo matemático

$$
s_i(t)=A cos(2πf_i t)
$$

donde:

f_i = frecuencia asociada al bit
A = amplitud constante

## Arquitectura del sistema

```
BitStream
   ↓
FSK Modulator
   ↓
Power Amplifier
   ↓
TX Antenna
   ↓
Wireless Channel
   ↓
RX Antenna
   ↓
RF Front-End
   ↓
FSK Demodulator
   ↓
Bit Decoder
   ↓
BER Analyzer

## BFSK implementado
```

El sistema implementa BFSK:

bit 0 → f_0
bit 1 → f_1

Frecuencias usadas:

f_0 = 4.0 MHz
f_1 = 4.1 MHz

## Demodulación

El receptor realiza correlación coherente:

$$
C_0 = Σ r(t)cos(2πf_0 t)
$$

$$
C_1 = Σ r(t)cos(2πf_1 t)
$$

La mayor correlación determina el bit recibido.

## Ventajas

mejor inmunidad al ruido
robustez media

## Desventajas

mayor ancho de banda
menor eficiencia espectral

# 3. PSK — Phase Shift Keying

## Introducción

La modulación PSK transmite información modificando la fase de la portadora.

La amplitud y frecuencia permanecen constantes.

## Modelo matemático

$$
s_i(t)=A cos(2πf_c t + φ_i)
$$

donde:

φ_i = fase asociada al bit

## BPSK implementado

El sistema implementa BPSK:

bit 0 → fase 0
bit 1 → fase π

## Arquitectura del sistema

```
BitStream
   ↓
BPSK Modulator
   ↓
Power Amplifier
   ↓
TX Antenna
   ↓
Wireless Channel
   ↓
RX Antenna
   ↓
RF Front-End
   ↓
BPSK Demodulator
   ↓
Bit Decoder
   ↓
BER Analyzer
```

## Demodulación

El receptor usa correlación coherente.

$$
C = Σ r(t)cos(2πf_c t)
$$

Decisión:

C > 0 → bit 0
C < 0 → bit 1

## Ventajas

alta inmunidad al ruido
buena eficiencia energética
ampliamente utilizada

## Desventajas

requiere sincronización precisa
mayor complejidad

# Comparación de modulaciones

Modulación	Cambia	Robustez	BW
ASK	amplitud	baja	bajo
FSK	frecuencia	media	medio
PSK	fase	alta	eficiente

# BER — Bit Error Rate

La calidad del sistema se evaluó usando BER:

$$
BER = N_errores / N_bits
$$

donde:

N_errores = bits detectados incorrectamente
N_bits = bits transmitidos

# Resultados Experimentales

Durante las pruebas de laboratorio se ejecutaron los tres sistemas de modulación digital implementados:

- ASK
- FSK
- PSK

Los resultados obtenidos fueron los siguientes.

--------------------------------------------------

## Resultado ASK

```bash
v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 ASK_tx_rx.py

[1 1 0 1 0 1 0 0 1 0 0 1 0 1 1 1 1 1 1 0]

TX bits:
[1 1 0 1 0 1 0 0 1 0 0 1 0 1 1 1 1 1 1 0]

RX bits:
[1 1 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1]

Errores: 6
BER: 0.3
```

## Análisis ASK

La modulación ASK presentó errores significativos en presencia de ruido AWGN.

Se observó:

BER elevado
sensibilidad al canal
degradación por amplitud

Esto ocurre porque ASK codifica la información directamente en amplitud, parámetro altamente vulnerable al ruido.

## Resultado PSK

```
v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 PSK_tx_rx.py

[1 0 1 1 1 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1]

TX bits:
[1 0 1 1 1 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1]

RX bits:
[1 0 1 1 1 1 0 1 1 0 0 1 0 0 0 0 1 1 0 1]

Errores: 0
BER: 0.0
```

## Análisis PSK

La modulación BPSK presentó el mejor desempeño entre los sistemas evaluados.

Características observadas:

BER nulo
alta inmunidad al ruido
excelente recuperación de bits

El sistema demostró gran robustez gracias al uso de detección coherente por correlación de fase.

## Resultado FSK

```
v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 FSK_tx_rx.py

[0 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0]

TX bits:
[0 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0]

RX bits:
[0 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0]

Errores: 0
BER: 0.0
```

## Análisis FSK

La modulación BFSK mostró excelente comportamiento frente al ruido.

Resultados observados:

BER nulo
correcta detección frecuencial
buena estabilidad

El uso de dos frecuencias separadas permitió mejorar la inmunidad al ruido respecto a ASK.

## Segunda ejecución ASK

```
v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 ASK_tx_rx.py

[0 0 0 0 0 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0]

TX bits:
[0 0 0 0 0 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0]

RX bits:
[0 0 0 0 0 1 1 1 0 1 1 1 1 0 0 0 1 1 1 1]

Errores: 3
BER: 0.15
```

## Observación

Incluso en diferentes ejecuciones, ASK continuó presentando errores de detección debido a:

sensibilidad a amplitud
atenuación
perturbaciones AWGN

## Error de ejecución detectado

v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 BSK_tx_rx.py

python3: can't open file 'BSK_tx_rx.py':
[Errno 2] No such file or directory

## Análisis

El error ocurrió debido a una referencia incorrecta del archivo.

Nombre correcto:

PSK_tx_rx.py

No existe:

BSK_tx_rx.py

## Ejecución adicional ASK

v-box@Dell-Inspiron:~/Escritorio/fb/Labamfmpm/src$ python3 ASK_tx_rx.py

[1 1 0 1 0 1 1 1 0 0 1 1 0 1 0 1 1 1 0 1]

TX bits:
[1 1 0 1 0 1 1 1 0 0 1 1 0 1 0 1 1 1 0 1]

RX bits:
[1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1]

Errores: 6
BER: 0.3

## Comparación final de desempeño

Modulación	BER observado	Desempeño
ASK	0.15 – 0.30	Bajo
FSK	0.0	Excelente
PSK	0.0	Excelente

## Conclusiones experimentales

Las pruebas permitieron comprobar experimentalmente el comportamiento de las modulaciones digitales.

Resultados principales:

ASK presentó mayor vulnerabilidad al ruido
FSK mostró buena robustez frecuencial
PSK obtuvo el mejor desempeño general

Se verificó que:

$$
PSK ≈ FSK > ASK
$$

en términos de BER bajo canal AWGN.


# Conclusiones

Las simulaciones permitieron analizar el comportamiento de las modulaciones digitales clásica   s.

Resultados observados:

ASK presenta alta sensibilidad al ruido
FSK mejora la robustez mediante separación espectral
PSK ofrece mejor desempeño BER

La arquitectura implementada permite futuras extensiones hacia:

QPSK
QAM
OFDM
SDR
canales multipath
sincronización avanzada
