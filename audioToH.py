import numpy as np

# Configuration
input_file = "audioTest.raw"  # Change this to your actual audio file
output_file = "audio_data.h"
var_name = "audioData"
samples_per_line = 16  # Adjust this for readability

# Load raw audio data
with open(input_file, "rb") as f:
    data = np.frombuffer(f.read(), dtype=np.uint8)

# Generate the header file
with open(output_file, "w") as f:
    f.write("#ifndef AUDIO_DATA_H\n#define AUDIO_DATA_H\n\n")
    f.write(f"const unsigned int audioLength = {len(data)};\n")
    f.write(f"const unsigned char {var_name}[] = {{\n")

    # Format data into multiple lines
    for i in range(0, len(data), samples_per_line):
        chunk = ", ".join(f"{x}" for x in data[i:i + samples_per_line])
        f.write(f"    {chunk},\n")

    f.write("};\n\n#endif // AUDIO_DATA_H\n")

print(f"Header file '{output_file}' generated successfully!")