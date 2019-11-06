from numpy import array, sin, cos
import pygame


def f(x, y1, y2):
    return array([y2, -g / l * sin(y1)])


g = 9.80666
l = 100
dt = 0.1
state = [0.0, 0]  # 0.2 - angle, 1 - angle'
t = 0

pygame.init()
clock = pygame.time.Clock()
srf = pygame.display.set_mode((300, 300))

while True:
    x = l * sin(state[0]) + 150
    y = l * cos(state[0]) + 150
    srf.fill((255, 255, 255))
    pygame.draw.line(srf, (100, 100, 100), (150, 150), (x, y), 2)
    pygame.draw.circle(srf, (100, 100, 100), (int(x), int(y)), 10, 0)

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        state[1] -= 0.01
    if keys[pygame.K_RIGHT]:
        state[1] += 0.01
    pygame.event.poll()
    clock.tick(60)
    print(state[1])
    k1 = f(t, state[0], state[1])
    k2 = f(t + dt / 2, state[0] + k1[0] * dt / 2, state[1] + k1[1] * dt / 2)
    k3 = f(t + dt / 2, state[0] + k2[0] * dt / 2, state[1] + k2[1] * dt / 2)
    k4 = f(t + dt, state[0] + k3[0] * dt, state[1] + k3[1] * dt)
    state += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    t += dt
