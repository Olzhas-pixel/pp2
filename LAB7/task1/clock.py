import datetime
import pygame as pg # type: ignore

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Часики Микки")
clock = pg.time.Clock()

done = False
chasiki = pg.image.load("mickey.png")
chasiki = pg.transform.scale(chasiki, (600, 600))

minute_hand = pg.image.load("righthand.png")
minute_hand = pg.transform.scale(minute_hand, (800, 700))
second_hand = pg.image.load("lefthand.png")
second_hand = pg.transform.scale(second_hand, (40, 500))

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    my_time = datetime.datetime.now()
    minuteRN = int(my_time.strftime("%M"))
    secondRN = int(my_time.strftime("%S"))

    angleMin = minuteRN * 7 * -1 - 10
    angleSec = secondRN * 6 * -1 - 5

    minute = pg.transform.rotate(minute_hand, angleMin)
    second = pg.transform.rotate(second_hand, angleSec)

    screen.fill((255, 255, 255))
    screen.blit(chasiki, (100, 100))
    screen.blit(minute, ((399 - int(minute.get_width() / 2)), 400 - int(minute.get_height() / 2)))
    screen.blit(second, ((399 - int(second.get_width() / 2)), 400 - int(second.get_height() / 2)))
    pg.display.flip()
    clock.tick(50)

pg.quit()