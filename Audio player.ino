#include "audio_data.h"

#define SPEAKER_PIN 26  // GPIO pin for speaker
#define SAMPLE_RATE 8000  // Hz (match your conversion rate)

unsigned long previousMicros = 0;
const unsigned long interval = 1000000 / SAMPLE_RATE;  // Time per sample
unsigned int i = 0;  // Keep track of audio position

void setup() {
    pinMode(SPEAKER_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMicros = micros();

    if (currentMicros - previousMicros >= interval) {
        previousMicros = currentMicros;

        dacWrite(SPEAKER_PIN, audioData[i]);  // Play current sample
        i++;  // Move to next sample

        if (i >= audioLength) {  // Restart playback when done
            i = 0;
            delay(3000);  // Pause 3 seconds before replaying
        }
    }
}
