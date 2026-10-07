# Práctica P1: Control y Parpadeo de un LED

 Introducción

En esta práctica se realizó el control de un LED conectado a una Raspberry Pi mediante el uso de Python y la librería `RPi.GPIO`.

El ejercicio consiste en generar una señal digital que permita encender y apagar un LED de manera repetitiva. Para comprender las diferentes formas de identificar los pines de la Raspberry Pi, se trabajó con dos sistemas de numeración: **BCM** y **BOARD**.

El desarrollo se realizó de manera remota. Para ello se utilizó una máquina virtual con Fedora instalada mediante VirtualBox, desde donde se estableció una conexión SSH con la Raspberry Pi.


## Objetivo de la práctica

El propósito de esta actividad es aprender a utilizar los puertos GPIO de una Raspberry Pi para controlar un componente electrónico básico.

Al finalizar la práctica se busca comprender:

* Cómo configurar un GPIO como salida.
* La diferencia entre numeración BCM y BOARD.
* Cómo generar un parpadeo utilizando retardos de tiempo.
* El funcionamiento de la librería `RPi.GPIO`.
* La conexión de una computadora con la Raspberry Pi mediante SSH.
* La importancia de liberar los GPIO al terminar un programa.

---

## Herramientas y software utilizados

Para realizar la actividad fueron necesarios los siguientes recursos:

* Raspberry Pi.
* LED.
* Resistencia.
* Protoboard.
* Cables de conexión.
* Computadora.
* Fedora Linux.
* VirtualBox.
* Python 3.
* Librería `RPi.GPIO`.
* Conexión de red mediante SSH.

---

## Conexión del LED

El LED fue conectado utilizando el **GPIO 18**, que corresponde al **pin físico número 12** de la Raspberry Pi.

| Programa      | Numeración | GPIO | Pin físico | Uso             |
| ------------- | ---------- | ---: | ---------: | --------------- |
| `blinkBCM.py` | BCM        |   18 |         12 | Control del LED |
| `blinkPIN.py` | BOARD      |    — |         12 | Control del LED |

En el primer programa se utiliza directamente el número GPIO, mientras que en el segundo se utiliza la numeración física de los pines.

Por lo tanto, ambas configuraciones terminan controlando la misma conexión física.

---

## Comunicación con la Raspberry Pi

Para acceder a la Raspberry Pi desde Fedora se utilizó una conexión SSH.

El comando empleado fue:

```bash
ssh mar@192.168.50.83
```

Después de ingresar correctamente, fue posible trabajar directamente con los archivos almacenados en la Raspberry Pi desde la terminal.

---

## Creación de los programas

Se realizaron dos archivos para comprobar las diferentes formas de numerar los pines.

Para crear o modificar el programa BCM:

```bash
sudo nano blinkBCM.py
```

Para trabajar con la numeración física:

```bash
sudo nano blinkPIN.py
```

Posteriormente, los programas fueron ejecutados con Python 3:

```bash
python3 blinkBCM.py
```

y:

```bash
python3 blinkPIN.py
```

---

## Programa utilizando BCM

El primer programa utiliza la numeración **BCM**, por lo que el LED se identifica mediante el GPIO 18.

La configuración principal es:

```python
GPIO.setmode(GPIO.BCM)
```

Después se establece el GPIO como salida:

```python
GPIO.setup(LED_PIN, GPIO.OUT)
```

El funcionamiento consiste en alternar el estado del pin.

Cuando se utiliza:

```python
GPIO.HIGH
```

el LED recibe una señal de salida y se enciende.

Posteriormente se utiliza:

```python
GPIO.LOW
```

para apagarlo.

Entre ambos estados se utiliza `time.sleep()` para establecer un intervalo de tiempo.

El resultado es un parpadeo continuo:

```text
ENCENDIDO → espera → APAGADO → espera
       ↑                         ↓
       └──────── repetir ────────┘
```

---

## Programa utilizando BOARD

El segundo método utiliza la numeración física de la Raspberry Pi.

En este caso se configura:

```python
GPIO.setmode(GPIO.BOARD)
```

El número utilizado para el LED es:

```python
LED_PIN = 12
```

Esto significa que el programa está haciendo referencia directamente al **pin físico 12**, en lugar de utilizar el número GPIO.

La secuencia del segundo programa realiza varios parpadeos consecutivos y posteriormente realiza una pausa antes de comenzar nuevamente el ciclo.

Esto permite observar de una manera diferente el comportamiento del mismo LED.

---

## Diferencia entre BCM y BOARD

Una de las partes principales de la práctica fue identificar la diferencia entre ambos métodos de numeración.

### BCM

La numeración BCM utiliza los números asignados a los GPIO del controlador de la Raspberry Pi.

En esta práctica:

```text
GPIO 18 → Pin físico 12
```

Se configura mediante:

```python
GPIO.setmode(GPIO.BCM)
```

### BOARD

La numeración BOARD utiliza directamente la posición física del pin en el conector de la Raspberry Pi.

En este caso:

```text
Pin físico 12 → GPIO 18
```

Se selecciona mediante:

```python
GPIO.setmode(GPIO.BOARD)
```

Aunque los números utilizados son diferentes, ambos métodos permiten controlar el mismo LED conectado al pin físico 12.

---

## Control del programa

Para evitar que el programa quede ejecutándose indefinidamente, se utilizó el manejo de la interrupción mediante:

```python
except KeyboardInterrupt:
```

De esta manera, al presionar:

```text
Ctrl + C
```

el programa puede detenerse de forma controlada.

Finalmente se utiliza:

```python
GPIO.cleanup()
```

para liberar los pines GPIO utilizados durante la ejecución.

---

## Resulta
