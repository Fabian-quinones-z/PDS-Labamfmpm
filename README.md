```
proyecto_fsk/
│
├── docs/
│   ├── informe.md
│   ├── figuras/        #Guardar aquí las gràficas de la docmentación
│   └── referencias.bib
├── src/
│   ├── ASK_tx_rx.py  
│   ├── FSK_tx_rx.py  
│   └── PSK_tx_rx.py
├── outputs/           #Dirifir aqui las plot 
│
└── README.md
```

# Las tres primeras modulaciones clásicas que normalmente se estudian son:


AM — Amplitude Modulation
La información modifica la amplitud de la portadora.


FM — Frequency Modulation
La información modifica la frecuencia de la portadora.


PM — Phase Modulation
La información modifica la fase de la portadora.


En comunicaciones digitales, estas evolucionan hacia esquemas discretos:


AM → ASK (Amplitude Shift Keying)


FM → FSK (Frequency Shift Keying)


PM → PSK (Phase Shift Keying)


Tu sistema actual corresponde a:
Sistema BFSK
(Binary Frequency Shift Keying)
porque usas dos frecuencias:


FREQ_0 = 4e6


FREQ_1 = 4.1e6


y cada frecuencia representa un bit distinto:

$$
bit 0 → f0f_0f0​
$$

$$
bit 1 → f1f_1f1​
$$

La relación conceptual es:

$$
s(t)=Acos⁡(2πfit)s(t)=A\cos(2\pi f_i t)s(t)=Acos(2πfi​t)
$$

donde:


AAA = amplitud constante


fif_ifi​ = frecuencia seleccionada según el bit transmitido



Introducción técnica del sistema
El código implementa una simulación completa de un sistema de comunicaciones digitales inalámbricas basado en modulación BFSK. El flujo reproduce varias etapas reales de una cadena RF:


generación de bits,


modulación,


amplificación,


transmisión,


propagación por canal inalámbrico,


recepción,


filtrado RF,


demodulación,


análisis BER.


La arquitectura está correctamente organizada en bloques funcionales orientados a objetos, lo que facilita futuras extensiones hacia:


BPSK,


QPSK,


OFDM,


SDR,


sincronización,


ecualización,


canales multipath,


fading.



Qué hace cada bloque
## 1. Fuente binaria
Clase:
BitStreamGenerator
Genera una secuencia aleatoria de bits:

$$
b[n]∈{0,1}b[n] \in \{0,1\}b[n]∈{0,1}
$$

## 2. Modulador BFSK
Clase:
BFSKModulator
Convierte bits en señales sinusoidales.


Si el bit es 0:
$$
f=f0f=f_0f=f0​
$$

Si el bit es 1:

$$
f=f1f=f_1f=f1​
$$

La señal transmitida es:

$$
si(t)=Acos⁡(2πfit)s_i(t)=A\cos(2\pi f_i t)si​(t)=Acos(2πfi​t)
$$

## 3. Amplificador RF
Clase:
PowerAmplifier
Incrementa potencia:

$$
samp(t)=G⋅s(t)s_{amp}(t)=G\cdot s(t)samp​(t)=G⋅s(t)
$$

## 4. Canal inalámbrico
Clase:
WirelessChannel
Simula fenómenos físicos reales:


Atenuación


Delay


Ruido AWGN


Modelo simplificado:

$$
r(t)=αs(t−τ)+n(t)r(t)=\alpha s(t-\tau)+n(t)r(t)=αs(t−τ)+n(t)
$$

donde:

$$
α\alphaα = atenuación
$$

$$
τ\tauτ = delay
$$

$$
n(t)n(t)n(t) = ruido gaussiano
$$


## 5. Front-End RF
Clase:
RFFrontend
Implementa un filtro pasabanda Butterworth para eliminar ruido fuera del espectro útil.

## 6. Demodulador BFSK
Clase:
BFSKDemodulator
Usa detección coherente por correlación.
Compara:

$$
∑r(t)cos⁡(2πf0t)\sum r(t)\cos(2\pi f_0 t)∑r(t)cos(2πf0​t)
$$

contra:

$$
∑r(t)cos⁡(2πf1t)\sum r(t)\cos(2\pi f_1 t)∑r(t)cos(2πf1​t)
$$

y decide cuál energía es mayor.

## 7. BER Analyzer
Clase:
BERAnalyzer
Calcula:


número de errores


BER (Bit Error Rate)


Definición:
BER=NerroresNbitsBER=\frac{N_{errores}}{N_{bits}}BER=Nbits​Nerrores​​

## Evaluación técnica inicial
El sistema está bien planteado para un primer laboratorio de comunicaciones digitales porque ya incorpora:


arquitectura modular,


simulación de canal,


detección coherente,


métricas BER,


procesamiento RF básico.


Además, los parámetros son coherentes:
ParámetroValorFrecuencias4 MHz / 4.1 MHzSampling8.7 MHzBit rate10 kbps
La condición de Nyquist se cumple:

$$
fs>2fmaxf_s > 2f_{max}fs​>2fmax​
$$

porque:

$$
fmax=4.1 MHzf_{max}=4.1\text{ MHz}fmax​=4.1 MHz
$$

$$
2fmax=8.2 MHz2f_{max}=8.2\text{ MHz}2fmax​=8.2 MHz
$$

$$
fs=8.7 MHzf_s=8.7\text{ MHz}fs​=8.7 MHz
$$


Plan de trabajo recomendado
## Fase 1 — Validación BFSK básica
Objetivo:
verificar funcionamiento ideal.
Tareas:


probar sin ruido,


probar sin delay,


verificar BER = 0,


visualizar señales TX/RX.



## Fase 2 — Evaluación de canal
Objetivo:
medir robustez.
Tareas:


variar NOISE_STD,


variar atenuación,


variar delay,


construir curvas BER vs SNR.



## Fase 3 — Análisis espectral
Objetivo:
entender ocupación de banda.
Tareas:


FFT de la señal BFSK,


ancho de banda,


separación entre tonos,


eficiencia espectral.



## Fase 4 — Comparación con otras modulaciones
Objetivo:
comparar desempeño.
Implementar:


ASK,


BPSK,


QPSK.


Comparar:


BER,


inmunidad al ruido,


ancho de banda,


complejidad.



## Fase 5 — Canal realista
Objetivo:
aproximación a RF real.
Agregar:


fading Rayleigh,


interferencia,


offset de frecuencia,


sincronización imperfecta.



## Fase 6 — SDR / Hardware
Objetivo:
migrar a entorno físico.
Posibles plataformas:


Ettus Research USRP


Analog Devices PlutoSDR


Raspberry Pi Foundation Raspberry Pi RF


HackRF



## Conclusión
El proyecto ya dejó de ser únicamente “un modulador” y ahora representa una cadena básica de comunicaciones digitales RF completa. La estructura es suficientemente buena para evolucionar hacia:

simulaciones académicas avanzadas,

SDR,

enlaces inalámbricos experimentales,

investigación BER/SNR,

sistemas IoT RF,

modem digital real.

