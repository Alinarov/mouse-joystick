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
sensitivity = 30


# Control de estado de botones para evitar múltiples clics por segundo
prev_buttons = [0] * joystick.get_numbuttons()


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

        # Botón X (izquierdo) - botón 0
        if joystick.get_button(0) and not prev_buttons[0]:
            pyautogui.click(button='left')

        # Botón Círculo (derecho) - botón 1
        if joystick.get_button(1) and not prev_buttons[1]:
            pyautogui.click(button='right')

        # Guardar el estado de los botones
        for i in range(joystick.get_numbuttons()):
            prev_buttons[i] = joystick.get_button(i)

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Programa detenido por el usuario.")
finally:
    pygame.quit()
