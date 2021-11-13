import argparse
import detectEsp
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def cifrado(mensaje):
    espacios = 1
    while espacios > 0:
        espacios = mensaje.count(' ')
        if mensaje.isalpha() == False:
            espacios += 1
    key = len(mensaje)
    translated = ''
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

def decifrado(mensaje):
    espacios = 1
    while espacios > 0:
        espacios = mensaje.count(' ')
        if mensaje.isalpha() == False:
            espacios += 1
    key = len(mensaje)
    translated = ''
    for symbol in mensaje:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)
    
def crackeo(mensaje):
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in mensaje:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        if detectEsp.isEsp(translated):
            # Ask user if this is the correct decryption.
            print()
            print('Español detectado, posible resultado...')
            print('Key %s: %s' % (key, translated))
            print()
            print('Ingresa una D si estas conforme..')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                print(translated)
           