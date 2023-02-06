from datetime import datetime
import turtle as t
from time import sleep

def linhas(t, posx, posy, raio):
    t.pu()
    t.goto(posx, posy)
    t.color ("green")
    
    for i in range(60):
        if i % 5 == 0:
            d = 0.2
            w = 5
        else:
            d= 0.1
            w = 2
            
        t.fd(raio*(1-d))
        t.pd()
        t.width(w)
        t.fd(raio*d)
        t.pu()
        t.bk(raio)
        t.rt(6)
        
def ponteiro(t, posx, posy, raio, ang, width, color):
    t.pu()
    t.goto(posx, posy)
    t.color (color)
    t.width(width)
    t.seth(90-ang)
    t.pd()
    t.fd(raio)
        
t.tracer(0)

x=0
y=0
r=300

while True:
    now = datetime.now()
    s_ang = now.second * 6 + now.microsecond / 1000000 * 6
    Min_ang = now.minute * 6 + now.second * 0.1
    H_ang = now.hour * 30 + now.minute * 0.5
    t.reset()
    
    #fundo
    
    linhas(t, x, y, r)
    #segundos
    ponteiro(t, x, y, r, s_ang, 2, 'red')
    ponteiro(t, x, y, r*0.8, Min_ang, 8, 'gray')
    ponteiro(t, x, y, r*0.5, H_ang, 10, 'gray')
    t.update()
    sleep(1/30)
