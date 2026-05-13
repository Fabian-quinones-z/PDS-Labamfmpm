# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Configuración global
class Config:

    # RF
    FC = 4e6

    # Sampling
    FS = 8.7e6

    # Bit timing
    BIT_RATE = 10e3
    BIT_DURATION = 1 / BIT_RATE

    # Signal
    AMPLITUDE = 1.0

    # Channel
    NOISE_STD = 0.2
    ATTENUATION = 0.6
    DELAY_SEC = 20e-6

    # Simulation
    NUM_BITS = 20


# Fuente de bits
class BitStreamGenerator:

    def __init__(self, num_bits):
        self.num_bits = num_bits

    def generate(self):
        bits = np.random.randint(0, 2, self.num_bits)
        print(bits)
        return bits


# Modulador BPSK
class BPSKModulator:

    def __init__(self, config):
        self.cfg = config

    def modulate(self, bits):

        samples_per_bit = int(
            self.cfg.FS * self.cfg.BIT_DURATION
        )

        signal = []

        for bit in bits:

            phase = 0 if bit == 0 else np.pi

            t = np.arange(samples_per_bit) / self.cfg.FS

            carrier = self.cfg.AMPLITUDE * np.cos(
                2 * np.pi * self.cfg.FC * t + phase
            )

            signal.extend(carrier)

        return np.array(signal)


# Amplificador RF
class PowerAmplifier:

    def __init__(self, gain=2.0):
        self.gain = gain

    def amplify(self, signal):
        return signal * self.gain


# Antena
class Antenna:

    def transmit(self, signal):
        return signal

    def receive(self, signal):
        return signal


# Canal inalámbrico
class WirelessChannel:

    def __init__(self, config):
        self.cfg = config

    def propagate(self, signal):

        signal = signal * self.cfg.ATTENUATION

        delay_samples = int(
            self.cfg.DELAY_SEC * self.cfg.FS
        )

        delayed = np.concatenate([
            np.zeros(delay_samples),
            signal
        ])

        delayed = delayed[:len(signal)]

        noise = np.random.normal(
            0,
            self.cfg.NOISE_STD,
            len(delayed)
        )

        return delayed + noise


# Front-End RF
class RFFrontend:

    def __init__(self, config):
        self.cfg = config

    def bandpass_filter(self, signal):

        nyquist = self.cfg.FS / 2

        low = 3.8e6 / nyquist
        high = 4.2e6 / nyquist

        b, a = butter(4, [low, high], btype='band')

        return lfilter(b, a, signal)


# Demodulador BPSK
class BPSKDemodulator:

    def __init__(self, config):
        self.cfg = config

    def demodulate(self, signal):

        samples_per_bit = int(
            self.cfg.FS * self.cfg.BIT_DURATION
        )

        detected_bits = []

        t = np.arange(samples_per_bit) / self.cfg.FS

        ref = np.cos(
            2*np.pi*self.cfg.FC*t
        )

        total_bits = len(signal) // samples_per_bit

        for i in range(total_bits):

            start = i * samples_per_bit
            end = start + samples_per_bit

            segment = signal[start:end]

            corr = np.sum(segment * ref)

            bit = 0 if corr > 0 else 1

            detected_bits.append(bit)

        return np.array(detected_bits)


# BER
class BERAnalyzer:

    @staticmethod
    def compute(tx_bits, rx_bits):

        min_len = min(len(tx_bits), len(rx_bits))

        errors = np.sum(
            tx_bits[:min_len] != rx_bits[:min_len]
        )

        ber = errors / min_len

        return errors, ber


# Sistema completo
class CommunicationSystem:

    def __init__(self):

        self.cfg = Config()

        self.source = BitStreamGenerator(
            self.cfg.NUM_BITS
        )

        self.modulator = BPSKModulator(self.cfg)

        self.pa = PowerAmplifier()

        self.tx_ant = Antenna()

        self.channel = WirelessChannel(self.cfg)

        self.rx_ant = Antenna()

        self.rf = RFFrontend(self.cfg)

        self.demod = BPSKDemodulator(self.cfg)

    def run(self):

        tx_bits = self.source.generate()

        tx_signal = self.modulator.modulate(tx_bits)

        tx_signal = self.pa.amplify(tx_signal)

        tx_signal = self.tx_ant.transmit(tx_signal)

        rx_signal = self.channel.propagate(tx_signal)

        rx_signal = self.rx_ant.receive(rx_signal)

        rx_signal = self.rf.bandpass_filter(rx_signal)

        rx_bits = self.demod.demodulate(rx_signal)

        errors, ber = BERAnalyzer.compute(
            tx_bits,
            rx_bits
        )

        print("TX bits:")
        print(tx_bits)

        print("\nRX bits:")
        print(rx_bits)

        print(f"\nErrores: {errors}")
        print(f"BER: {ber}")

        self.plot(tx_signal, rx_signal)

    def plot(self, tx, rx):

        plt.figure(figsize=(15,6))

        plt.subplot(2,1,1)
        plt.title("TX Signal")
        plt.plot(tx[:3000])

        plt.subplot(2,1,2)
        plt.title("RX Signal")
        plt.plot(rx[:3000])

        plt.tight_layout()
        plt.show()


system = CommunicationSystem()
system.run()
