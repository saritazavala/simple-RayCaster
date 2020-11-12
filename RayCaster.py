import pygame
from math import *
import sys
#References
#https://pythonprogramming.net/pygame-start-menu-tutorial/

colors = {
  '1': (146,60,63),
  '2': (233,70,63),
  '3': (0,130,168),
  '4': (0,0,0),
  "\n": (0,0,0)
}

back = pygame.image.load('./images/main_menu.png')
instrucciones = pygame.image.load('./images/instrucciones.jpg')
wall1 = pygame.image.load('./images/wallU1.jpg')
wall2 = pygame.image.load('./images/wallU2.jpg')
wall3 = pygame.image.load('./images/wallU3.png')
wall4 = pygame.image.load('./images/wall4.png')
wall5 = pygame.image.load('./images/wall5.png')
end = pygame.image.load('./images/ptm.png')
win = pygame.image.load('./images/win.gif')
lose = pygame.image.load('./images/lose.jpg')
#Enemies
enemy1 = pygame.image.load('./images/sprite1.png')
enemy2 = pygame.image.load('./images/sprite2.png')
enemy3 = pygame.image.load('./images/sprite3.png')
enemy4 = pygame.image.load('./images/sprite4.png')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_hand = pygame.image.load('./images/player.png')
textures = {
  "1":wall1,
  "2":wall2,
  "3":wall3,
  "4":wall4,
  "5":wall5,
  "6": end
}
#Music


enemies = [
  {
    "x": 100,
    "y": 200,
    "texture": enemy1
  }
]

class Raycaster:
  def __init__(self, screen):
    _, _, self.width, self.height = screen.get_rect()
    self.zbuffer = [-float('inf') for z in range(0, 500)]
    self.screen = screen
    self.blocksize = 50
    self.map = []

    self.player = {
      "x": self.blocksize +25,
      "y": self.blocksize +25,
      "a": 0,
      "fov":pi/3
    }

  def start_game(self):
    # render loop
    while True:
      screen.fill((0, 0, 0))
      d = 10
      for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
          exit(0)
        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_a:
            r.player["a"] -= pi / 20

          if e.key == pygame.K_d:
            r.player["a"] += pi / 20

          if e.key == pygame.K_w:
            r.player["x"] += int(d * cos(r.player["a"]))
            r.player["y"] += int(d * sin(r.player["a"]))
            print(r.player["x"], r.player["y"])

          if e.key == pygame.K_s:
            r.player["x"] -= int(d * cos(r.player["a"]))
            r.player["y"] -= int(d * sin(r.player["a"]))

          if (r.player["x"] > 360) and (r.player["y"] > 70):
            self.win_action()

          #Lose option in process
          # if self

      #351 79
      #360, 80
      r.render()
      screen.blit(self.update_fps(), (10, 0))
      pygame.display.flip()

  def instructionsPage(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.K_3:
          exit(0)
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            self.main_menu()

      #Fonts --------------------
      instruction_tittle = pygame.font.SysFont('gabriola', 50, True)
      return_key = pygame.font.SysFont('gabriola', 25, True)
      message = pygame.font.SysFont('inkfree',25, False, True)
      description = pygame.font.SysFont('couriernew',20, False,False)
      option = pygame.font.SysFont('lucidasanstypewriter',15, False,False)

      TextSurf, TextRect = self.text_objects("Instrucciones", instruction_tittle)
      TextRect.center = (int(self.width / 2), int(self.height / 4))
      screen.blit(TextSurf,TextRect)

      TextSurf, TextRect = self.text_objects("Bienvenido! El objetivo del juego es llegar al tesoro de Drake.", description)
      TextRect.center = (int(self.width / 2), int(self.height / 3))
      screen.blit(TextSurf,TextRect)


      TextSurf, TextRect = self.text_objects("Trata de no toparte con paredes o enemigos, de lo contrario",description)
      TextRect.center = (int(self.width / 2), int(self.height / 2.5))
      screen.blit(TextSurf,TextRect)

      TextSurf, TextRect = self.text_objects("Drake morirá y perderá su progreso",description)
      TextRect.center = (int(self.width / 2), int(self.height / 2.10))
      screen.blit(TextSurf,TextRect)

      TextSurf, TextRect = self.text_objects("Sic Parvis Magna", message)
      TextRect.center = (int(self.width / 1.5), int(self.height / 1.5))
      screen.blit(TextSurf,TextRect)

      TextSurf, TextRect = self.text_objects("Presiona R para regresar", return_key)
      TextRect.center = (int(self.width / 4), int(self.height / 1.5))
      screen.blit(TextSurf,TextRect)

      pygame.display.update()
      clock.tick(15)
      screen.blit(instrucciones, (0, 0))


  def text_objects(self, text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

  def main_menu_sound(self):
    pygame.mixer.music.load('./music/A Thiefs End.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(0)


  def main_menu(self):
    self.main_menu_sound()
    print(pygame.font.get_fonts())
    intro = True
    while intro:
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.K_3:
          exit(0)
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
            self.start_game()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
              self.instructionsPage()
            if event.type == pygame.K_3:
              exit(0)

      #Fonts -----------------
      tittle_font = pygame.font.SysFont('gabriola', 50, True)
      instructions_font = pygame.font.SysFont('couriernew',25, False,False)
      instruccions = pygame.font.SysFont('lucidasanstypewriter',15, False,False)
      # -----------------------------
      TextSurf, TextRect = self.text_objects("Unchart3d", tittle_font)
      TextRect.center = (int(self.width / 5), int(self.height / 3))
      screen.blit(TextSurf,TextRect)
      # -----------------------------
      TextSurf, TextRect = self.text_objects("Elige tu opcion", instructions_font)
      TextRect.center = (int(self.width / 5), int(self.height / 2.4))
      screen.blit(TextSurf,TextRect)
      # -----------------------------
      TextSurf, TextRect = self.text_objects("1. Empezar Juego", instruccions)
      TextRect.center = (int(self.width / 5), int(self.height / 2))
      screen.blit(TextSurf,TextRect)
      # -----------------------------
      TextSurf, TextRect = self.text_objects("2. Instrucciones", instruccions)
      TextRect.center = (int(self.width / 5), int(self.height / 1.75))
      screen.blit(TextSurf,TextRect)
      # -----------------------------
      TextSurf, TextRect = self.text_objects("3. Salir", instruccions)
      TextRect.center = (int(self.width / 5), int(self.height / 1.58))
      screen.blit(TextSurf,TextRect)
      # -----------------------------
      pygame.display.update()
      clock.tick(15)
      screen.blit(back, (0,0))
      #print(pygame.font.get_fonts())


  def point(self, x, y, c):
    screen.set_at((x, y), c)

  def draw_rectangle(self, x, y, texture):
    for cx in range(x, x + 50):
      for cy in range(y, y + 50):
        tx = int((cx - x)*128 / 50)
        ty = int((cy - y)*128 / 50)
        c = texture.get_at((tx, ty))
        self.point(cx, cy, c)


  def load_map(self, filename):
    with open(filename) as f:
      for line in f.readlines():
        self.map.append(list(line))

  def draw_player(self, xi, yi, w=256, h=256):
    for x in range(xi, xi + w):
      for y in range(yi, yi + h):
        tx = int((x - xi) * 32 / w)
        ty = int((y - yi) * 32 / h)
        c = player_hand.get_at((tx, ty))
        if c != (152, 0, 136, 255):
          self.point(x, y, c)

  def cast_ray(self, a):
    d = 0
    while True:
      x = self.player["x"] + d*cos(a)
      y = self.player["y"] + d*sin(a)

      i = int(x / self.blocksize)
      j = int(y / self.blocksize)

      if self.map[j][i] != ' ':
        hitx = x - i*50
        hity = y - j*50

        if 1 < hitx < 49:
          maxhit = hitx
        else:
          maxhit = hity

        tx = int(maxhit * 128 / 50)

        return d, self.map[j][i], tx

      self.point(int(x), int(y), (255, 255, 255))
      d += 1


  def win_action(self):
    while True:
      for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
          exit(0)
        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_0:
            intro = False
            self.main_menu()

      congrats_message = pygame.font.SysFont('erasitc', 50, False)
      TextSurf, TextRect = self.text_objects("Hemos ganado!", congrats_message)
      TextRect.center = (int(self.width / 1.25), int(self.height /3))
      screen.blit(TextSurf,TextRect)

      pygame.display.update()
      clock.tick(15)
      screen.blit(win, (0, 0))

  def lose_action(self):
    while True:
      for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
          exit(0)

      pygame.display.update()
      clock.tick(15)
      screen.blit(lose, (0, 0))



  def draw_stake(self, x, h, tx, texture):
    start = int(250 - h / 2)
    end = int(250 + h / 2)
    for y in range(start, end):
      ty = int((y - start) * (128 / (end - start)))
      c = texture.get_at((tx, ty))
      self.point(x, y, c)

  def draw_sprite(self, sprite):
    sprite_a = atan2((sprite["y"] - self.player["y"]), (sprite["x"] - self.player["x"]))
    sprite_d = ((self.player["x"] - sprite["x"]) ** 2 + \
                (self.player["y"] - sprite["y"]) ** 2) ** 0.5
    sprite_size = int(500 / sprite_d * 70)
    sprite_x = int(500 + (sprite_a - self.player["a"]) * 500 / self.player["fov"] + \
                   250 - sprite_size / 2)
    sprite_y = int(250 - sprite_size / 2)

    for x in range(sprite_x, sprite_x + sprite_size):
      for y in range(sprite_y, sprite_y + sprite_size):
        if 500 < x < 1000 and self.zbuffer[x - 500] <= sprite_d:
          tx = int((x - sprite_x) * 128 / sprite_size)
          ty = int((y - sprite_y) * 128 / sprite_size)
          c = sprite["texture"].get_at((tx, ty))
          if c != (152, 0, 136, 255):
            self.point(x, y, c)
            self.zbuffer[x - 500] = sprite_d

  def render(self):
    # dibuja la vista desde arriba
    for x in range(0, int(self.width / 2), self.blocksize):
      for y in range(0, self.height, self.blocksize):
        i = int(x / self.blocksize)
        j = int(y / self.blocksize)

        if self.map[j][i] != ' ':
          self.draw_rectangle(x, y, textures[self.map[j][i]])

    self.point(self.player["x"], self.player["y"], WHITE)

    # dibuja la vista de primera persona
    for i in range(0, 500):
      a = self.player["a"] - self.player["fov"] / 2 + (i * self.player["fov"] / 500)
      d, m, tx = self.cast_ray(a)
      x = 500 + i
      h = int(500 / (d * cos(a - self.player["a"]))) * 50
      self.draw_stake(x, h, tx, textures[m])

    for i in range(0, 500):
      self.point(499, i, (0, 0, 0))
      self.point(500, i, (0, 0, 0))
      self.point(501, i, (0, 0, 0))

    for enemy in enemies:
      self.point(enemy["x"], enemy["y"], BLACK)
      self.draw_sprite(enemy)

    self.draw_player(1000 - 256 - 128, 500 - 256)

  def update_fps(self):
    font = pygame.font.SysFont("erasitc", 25, True)
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("white"))
    return fps_text

# ------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Zaravala')
r = Raycaster(screen)
back = pygame.transform.scale(back, (r.width, r.height))
win = pygame.transform.scale(win, (r.width, r.height))
lose = pygame.transform.scale(lose, (r.width, r.height))
instrucciones = pygame.transform.scale(instrucciones, (r.width, r.height))
r.load_map('./level1.txt')
clock = pygame.time.Clock()
r.main_menu()


