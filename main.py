import os
import subprocess

# Generate input.wav if it doesn't exist
def generate_input_wav():
    if not os.path.exists('input.wav'):
        print("Generating input.wav file...")
        subprocess.run(['python', 'generate_input_wav.py'])
    else:
        print("input.wav file already exists.")

# Process audio signal and apply distortion
def process_audio():
    if os.path.exists('input.wav'):
        print("Processing input.wav and applying distortion...")
        subprocess.run(['python', 'tube_amp_simulation.py'])
    else:
        print("input.wav file not found. Please generate it first.")

# Main function to execute the workflow
def main():
    print("Starting the Tube Amplifier Simulation Project...")
    generate_input_wav()
    process_audio()
    print("Project successfully completed! Please check the output_tube_amp.wav file.")

# Entry point
if __name__ == '__main__':
    main()
