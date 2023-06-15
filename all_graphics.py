import pygame
from pathlib import Path

WIDTH = 1200
HEIGHT = 600

dir_path = Path.cwd()
# добавление всей основной графики в код
background = pygame.image.load(Path(dir_path, "graphics", "уровень.jpg"))
background_rect = background.get_rect()
garry = pygame.image.load(Path(dir_path, "graphics", "гарри.png"))  # гарри
start_menu = pygame.image.load(Path(dir_path, "graphics", "старт.png"))
start_menu_rect = start_menu.get_rect() # стартовое меню
end_menu = pygame.image.load(Path(dir_path, "graphics", "конец.png"))
end_menu = pygame.transform.scale(end_menu, (1200, 600))
end_menu_rect = end_menu.get_rect() # проигрыш
victory = pygame.image.load(Path(dir_path, "graphics", "выигрыш.png"))
victory = pygame.transform.scale(victory, (1200, 600))
victory_rect = victory.get_rect()   # выигрыш
score_text = pygame.image.load(Path(dir_path, "graphics", "счет.png")) # счет
score_text = pygame.transform.scale(score_text, (130, 50))
score_text_rect = score_text.get_rect(center=(WIDTH - 700, 50))
hog_logo = pygame.image.load(Path(dir_path, "graphics", "логотип хогвартса.png"))
hog_logo = pygame.transform.scale(hog_logo, (80, 80))
hog_logo_rect = hog_logo.get_rect(center=(WIDTH - 825, 50))
dementor = pygame.image.load(Path(dir_path, "graphics", "дементор.png"))
hp = pygame.image.load(Path(dir_path, "graphics", "хп.png"))
hp = pygame.transform.scale(hp, (100, 80))
hp_rect = hp.get_rect(center=(WIDTH - 180, 50))

# загрузка анимации взрыва противника

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(12):
    filename = Path(dir_path, "graphics", "пух{}.png".format(i))
    img = pygame.image.load(filename)
    img.set_colorkey("black")
    img_lg = pygame.transform.scale(img, (156, 156))
    explosion_anim['lg'].append(img_lg)

# загрузка всех видов врагов

pojirateli = []
pojirateli_list = [Path(dir_path, "graphics", "пожиратель .png"),
                   Path(dir_path, "graphics", "пожиратель1.png")]
sova = []
sova_list = [Path(dir_path, "graphics", "сова1.png"),
             Path(dir_path, "graphics", "сова2.png"),
             Path(dir_path, "graphics", "сова3.png")]

clans = []
clans_list = [Path(dir_path, "graphics", "когтевран.png"),
              Path(dir_path, "graphics", "пуффендуй.png"),
              Path(dir_path, "graphics", "слизерин.png")]
piu = []
piu_list = [Path(dir_path, "graphics", "пиу.png"),
            Path(dir_path, "graphics", "пиу1.png"),
            Path(dir_path, "graphics", "пиу2.png"),
            Path(dir_path, "graphics", "пиу3.png"),
            Path(dir_path, "graphics", "пиу4.png")]

for img in pojirateli_list:
    pojirateli.append(pygame.image.load(img))

for img in sova_list:
    sova.append(pygame.image.load(img))

for img in clans_list:
    clans.append(pygame.image.load(img))

for img in piu_list:
    piu.append(pygame.image.load(img))

# отдельный класс для анимации взрыва

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 35

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
