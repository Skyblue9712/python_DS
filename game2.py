import pgzrun
from random import randint
#screen height and width
WIDTH = 800
HEIGHT = 600
w,h=WIDTH,HEIGHT
# payer in the middle of hte screen
p= Rect((w//2,h//2),(20,30))# player
e= Rect((0,h//2), (20,30))# enemy
c= Rect((200,200), (10,10))# coin
score =0

def draw():
     screen.fill("BLACK")
     screen.draw.filled_rect(p,'white')
     screen.draw.filled_rect(e,'red')
     screen.draw.filled_rect(c,'yellow')
     screen.draw.text(f'score:{score}',topleft=(10,10),fontsize=30)


def update(dt):
    global score
    if keyboard.left: p.x += -1
    if keyboard.right: p.x += 1
    if keyboard.up: p.y += -1
    if keyboard.down: p.y += 1

    if p.x < 0: p.x =w
    if p.x > w: p.x =0
    if p.y < 0: p.y =h
    if p.y > h: p.y =0

    if e.x < p.x:e.x +=+1
    if e.x > p.x:e.x +=-1
    if e.y < p.y:e.y +=+1
    if e.y > p.y:e.y +=-1

    if p.colliderect(e):
       print('game over')
       quit()
    if p.colliderect(c):
       score +=1
       c.x =randint(0,w)
       c.y= randint(0,h)

pgzrun.go()