import pygame
import pyautogui
import time

# Inicializar pygame y joystick
pygame.init()
pygame.joystick.init()

# Verifica si hay al menos un joystick conectado
if pygame.joystick.get_count() == 0:
    print("No hay mandos conectados.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Usando mando: {joystick.get_name()}")

# Sensibilidad del movimiento del ratón
sensitivity = 20

try:
    while True:
        pygame.event.pump()  # Actualiza eventos de pygame

        # Leer ejes del joystick (0 = izquierda/derecha, 1 = arriba/abajo)
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        # Multiplicar por sensibilidad
        dx = int(x_axis * sensitivity)
        dy = int(y_axis * sensitivity)

        # Mover el ratón
        if dx != 0 or dy != 0:
            pyautogui.moveRel(dx, dy)

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Programa detenido por el usuario.")
finally:
    pygame.quit()
