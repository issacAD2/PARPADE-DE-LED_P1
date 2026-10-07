import time
import RPi.GPIO as GPIO # type: ignore

PIN_LED = 18

def preparar_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_LED, GPIO.OUT)
    GPIO.output(PIN_LED, GPIO.LOW)


def cambiar_estado(estado):
    GPIO.output(PIN_LED, estado)

    if estado == GPIO.HIGH:
        print(">>> LED: ENCENDIDO")
    else:
        print(">>> LED: APAGADO")


try:
    preparar_gpio()

    print("==============================")
    print("   PRACTICA: LED CON GPIO")
    print("==============================")
    print("Numeracion utilizada: BCM")
    print("GPIO utilizado:", PIN_LED)
    print("Pin fisico: 12")
    print("Presiona Ctrl+C para terminar\n")

    while True:
        cambiar_estado(GPIO.HIGH)
        time.sleep(1)

        cambiar_estado(GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma detenido.")

finally:
    GPIO.cleanup()
    print("Configuracion GPIO liberada.")