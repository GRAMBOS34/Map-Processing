from gpiozero import LED
import time
from lcd import LCD
from gpiozero import Device
from gpiozero.pins.native import NativeFactory
Device.pin_factory = NativeFactory()

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x3f, True)

# Constants
LED_PIN = 20
BUZZER_PIN = 21
DOT_PULSE_LENGTH = 0.5
DASH_PULSE_LENGTH = DOT_PULSE_LENGTH * 3

# Initialize output pins
# I'm using the led header cuz im lazy lol
led = LED(LED_PIN)
buzzer = LED(BUZZER_PIN)

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
# i got lazy lol so.
# code from: https://www.geeksforgeeks.org/morse-code-translator-python/
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

def LED_out(morseMsg):
    for i in morseMsg:
        if i == ".":
            led.on()
            time.sleep(DOT_PULSE_LENGTH)

        if i == "-":
            led.on()
            time.sleep(DASH_PULSE_LENGTH)
        led.off()
        time.sleep(0.1) # it wont blink without this for some reason

        if i == " ":
            time.sleep(DASH_PULSE_LENGTH)

def BUZZER_out(morseMsg):
    for i in morseMsg:
        if i == ".":
            buzzer.on()
            time.sleep(DOT_PULSE_LENGTH)
            buzzer.off()

        if i == "-":
            buzzer.on()
            time.sleep(DASH_PULSE_LENGTH)
        buzzer.off()
        time.sleep(0.1) # it wont blink without this for some reason

        if i == " ": 
            time.sleep(DASH_PULSE_LENGTH)

# Main Function
while True:
    msg = str(input("Message to translate to Morse Code: "))

    while True:
        choice = int(input("Which mode?: [1 for Light, 2 for sound]: "))

        if choice == 1:
            lcd.message("Message: ", 1)
            lcd.message(msg, 2)
            LED_out(encrypt(msg.upper()))
            break

        if choice == 2:
            lcd.message("Message: ", 1)
            lcd.message(msg, 2)
            BUZZER_out(encrypt(msg.upper()))
            break

        else:
            print("That isn't one of the choices. Please try again")


    lcd.clear()
    lcd.message("Finished!", 1)

