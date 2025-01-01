import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

# Define distortion function
def tube_amp_distortion(x, gain=5, threshold=0.8):
    x = gain * x
    x = np.clip(x, -threshold, threshold)
    return x / threshold

# Read input file
rate, data = wav.read('input.wav')
data = data / np.max(np.abs(data))  # Normalize input signal

# Apply FFT and distortion
spectrum = fft(data)
processed_data = tube_amp_distortion(np.real(ifft(spectrum)))
output = np.real(ifft(fft(processed_data)))
output = output / np.max(np.abs(output))  # Normalize output signal

# Save output file
output = (output * 32767).astype(np.int16)
wav.write('output_tube_amp.wav', rate, output)

# Display signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.title('Original Signal')
plt.plot(data[:1000])
plt.subplot(2, 1, 2)
plt.title('Processed Signal (Tube Amp Simulation)')
plt.plot(output[:1000])
plt.tight_layout()
plt.show()

print("Processing complete. Output saved as output_tube_amp.wav")
