import pygame
from all_graphics import explosion_anim, background, background_rect, start_menu_rect, start_menu, victory_rect, victory
from all_graphics import score_text, score_text_rect, hog_logo, hog_logo_rect, hp_rect, hp, end_menu_rect, end_menu, \
    Explosion
from all_sound import hit_sound, hit_enemy_sound, click, victory_sound, end_menu_sound, shoot_sound
from enemys import Dementor, Sova, Pojirateli, Clans
from player import Player, Bullet
from pathlib import Path

dir_path = Path.cwd()

pygame.mixer.music.load(Path(dir_path, "sound", "Главное меню.wav"))
pygame.mixer.music.set_volume(0.2)

WIDTH = 1200
HEIGHT = 600
FPS = 60

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гарри Поттер")
clock = pygame.time.Clock()


def new_enemy():
    d = Dementor()
    s = Sova()
    c = Clans()
    dd = Pojirateli()
    all_sprites.add(d)
    all_sprites.add(s)
    all_sprites.add(c)
    all_sprites.add(dd)
    dem.add(d)
    sov.add(s)
    cl.add(c)
    death.add(dd)

# универсальная функция для вывода любого текста на экран
def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('VCROSDMonoRUSbyD')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, "yellow")
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# функция вывода стартового меню
def show_go_screen():
    screen.blit(start_menu, start_menu_rect) # загрузка картинки
    pygame.display.flip()
    waiting = True
    pygame.mixer.music.play(loops=-1)
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                pygame.quit()
            if event.type == pygame.KEYDOWN: # если нажалась любая клавиша - игра началась
                click.play()
                waiting = False
                pygame.mixer.music.stop() # музыка в меню остановилась, пошла музыка геймплея
                pygame.mixer.music.load(Path(dir_path, "sound", "Уровень.wav"))
                pygame.mixer.music.play(loops=-1)
                pygame.mixer.music.set_volume(0.2)


def show_out_screen():
    if score >= 1000: # если набрано необходимое количество очков, вывод победного экрана
        screen.blit(victory, victory_rect) #
        draw_text(screen, str(score), 60, WIDTH / 1.4, HEIGHT / 1.75)
        pygame.mixer.music.stop() # остановка всего звука
        hit_sound.stop()
        hit_enemy_sound.stop()
        shoot_sound.stop()
        victory_sound.play() # проигрыш звука победы
    else:
        screen.blit(end_menu, end_menu_rect) # если гарри умер, то вывод проигрышного экрана
        draw_text(screen, str(score), 60, WIDTH / 2, HEIGHT / 1.75)
        pygame.mixer.music.stop() # аналогично
        hit_sound.stop()
        hit_enemy_sound.stop()
        shoot_sound.stop()
        end_menu_sound.play()

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход из игры
                pygame.quit()


# Цикл игры
game_over = True
running = True
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(bullets)
enemy = pygame.sprite.Group()
death = pygame.sprite.Group()
dem = pygame.sprite.Group()
sov = pygame.sprite.Group()
cl = pygame.sprite.Group()
score = 0
for i in range(6):
    new_enemy()

while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        all_sprites.add(bullets)
        enemy = pygame.sprite.Group()
        death = pygame.sprite.Group()
        dem = pygame.sprite.Group()
        sov = pygame.sprite.Group()
        cl = pygame.sprite.Group()
        score = 0
        for i in range(6):
            new_enemy()

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    # Обновление
    all_sprites.update()

    hits_dem = pygame.sprite.spritecollide(player, dem, True)
    for hit in hits_dem:
        player.hp -= 20
        hit_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if player.hp <= 0:
            running = False
            game_over = True
            show_out_screen()

    hits_sov = pygame.sprite.spritecollide(player, sov, True)
    for hit in hits_sov:
        player.hp -= 10
        hit_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if player.hp <= 0:
            running = False
            game_over = True
            show_out_screen()

    hits_clans = pygame.sprite.spritecollide(player, cl, True)
    for hit in hits_clans:
        player.hp -= 10
        hit_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if player.hp <= 0:
            running = False
            game_over = True
            show_out_screen()

    hits_death = pygame.sprite.spritecollide(player, death, True)
    for hit in hits_death:
        player.hp -= 40
        hit_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if player.hp <= 0:
            running = False
            game_over = True
            show_out_screen()

    hits1 = pygame.sprite.groupcollide(dem, bullets, True, True)
    for hit in hits1:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        score += 20
        d = Dementor()
        all_sprites.add(d)
        dem.add(d)

    hits2 = pygame.sprite.groupcollide(cl, bullets, True, True)
    for hit in hits2:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        score -= 10
        c = Clans()
        all_sprites.add(c)
        cl.add(c)

    hits3 = pygame.sprite.groupcollide(sov, bullets, True, True)
    for hit in hits3:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        score -= 20
        s = Sova()
        all_sprites.add(s)
        sov.add(s)

    hits4 = pygame.sprite.groupcollide(death, bullets, True, True)
    for hit in hits4:
        hit_enemy_sound.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        score += 30
        dd = Pojirateli()
        all_sprites.add(dd)
        death.add(dd)

    if score >= 1000:
        show_out_screen()
        victory_sound.play()
        running = False
        game_over = True

    # Рендеринг
    screen.blit(background, background_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(hog_logo, hog_logo_rect)
    screen.blit(hp, hp_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 48, WIDTH - 550, 27)
    draw_text(screen, str(player.hp), 48, WIDTH - 80, 27)
    draw_text(screen, "ЦЕЛЬ:1000", 48, 180, HEIGHT - 75)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
