from pydub import AudioSegment
from pydub.playback import play
import time

# Load the audio files for short and long beeps
beep = AudioSegment.from_mp3("morseshort.mp3")
beeeep = AudioSegment.from_mp3("morselong.mp3")

# Define the morse code
morse_code = {
    "A": '.-',
    "B": '-...',
    "C": '-.-.',
    "D": '-..',
    "E": '.',
    "F": '..-.',
    "G": '--.',
    "H": '....',
    "I": '..',
    "J": '.---',
    "K": '-.-',
    "L": '.-..',
    "M": '--',
    "N": '-.',
    "O": '---',
    "P": '.--.',
    "Q": '--.-',
    "R": '.-.',
    "S": '...',
    "T": '-',
    "U": '..-',
    "V": '...-',
    "W": '.--',
    "X": '-..-',
    "Y": '-.--',
    "Z": '--..',
}

#Ask the user for an input
print("What would you like trasnlated into morse code")
# Define the phrase 
phrase = input(" ")

# Translate the phrase into morse code and play the corresponding sounds
for char in phrase:
    if char.upper() in morse_code:  # Check if the character has a morse code equivalent
        morse = morse_code[char.upper()]
        print(f"Morse code for {char}: {morse}")
        
        for symbol in morse:
            if symbol == ".":
                play(beep)  # Short beep for dot
                time.sleep(0.2)  # Pause between sounds (duration of one dot)
            elif symbol == "-":
                play(beeeep)  # Long beep for dash
                time.sleep(0.6)  # Pause between sounds (duration of one dash)
        
        time.sleep(0.5)  # Pause between characters

    elif char == " ":  # Pause between words
        print("Space detected, pausing between words.")
        time.sleep(1)  # Pause between words


