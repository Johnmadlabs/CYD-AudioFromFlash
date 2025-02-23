# CYD-AudioFromFlash
Hello, this is a very simple, barebones audio player for the CYD display, might work with any esp32 or Arduino, haven't tested

The code should run on the CYD just like that, output should sound like audioTest.mp3, but here is how you change the audio file:

First prepare audio file:
- Get a small audio file! under 1mb is preferred, but feel free to experiment and find what gives you the proper audio_data.h size (under 5mb for the CYD)
- open your audio file in Audacity
- Split Stereo to Mono (dropdown on the left where it says the song name)
- Change Project Rate (Hz) to something low, 8000 works quite well and takes up the least space
- File > Export > Export Audio
- Change header to RAW (header-less)
- Change encoding to Unsigned 8-bit PCM
- Save the file



Then Run the python script in command prompt:
- open python file in notepad
- change "audioTest.raw" to whatever your file is called
- save and close
- open cmd
- cd to this folder 
- type "python audioToH.py" to run the program
- pip install numpy if you get an error 
- audio_data.h file will be replaced with your music




Finally 
- open your Audio player.ino file and change the sample rate or audio pin (if needed)
- compile and upload to the CYD
