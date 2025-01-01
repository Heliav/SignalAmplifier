import numpy as np
import scipy.io.wavfile as wav

# Define signal properties
fs = 44100  # Sampling rate (Hz)
duration = 1  # Duration (seconds)
frequency = 440  # Frequency (Hz)
amplitude = 0.5  # Amplitude

# Generate a sine wave
t = np.linspace(0, duration, int(fs * duration))
sine_wave = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.float32)

# Save as WAV file
wav.write('input.wav', fs, sine_wave)
print("input.wav file successfully generated!")
