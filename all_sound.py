
import pygame
from pathlib import Path

dir_path = Path.cwd()

pygame.mixer.init()

click = pygame.mixer.Sound(Path(dir_path, "sound", "Клик.wav"))
click.set_volume(0.09)

shoot_sound = pygame.mixer.Sound(Path(dir_path, "sound", "Выстрел.wav"))
shoot_sound.set_volume(0.5)

hit_sound = pygame.mixer.Sound(Path(dir_path, "sound", "Враг попал.wav"))
hit_sound.set_volume(0.1)

hit_enemy_sound = pygame.mixer.Sound(Path(dir_path, "sound", "Враг умер.wav"))
hit_enemy_sound.set_volume(0.1)

victory_sound = pygame.mixer.Sound(Path(dir_path, "sound", "Победа.wav"))
victory_sound.set_volume(0.2)

end_menu_sound = pygame.mixer.Sound(Path(dir_path, "sound", "Смерть.wav"))
end_menu_sound.set_volume(0.2)