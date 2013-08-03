import pygame
import random
import math
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--life-cycle", dest="wlen", default=0,
                  help="set custom life cycle", metavar="NUMBER")
parser.add_option("-x", dest="resx", default=500,
                  help="set resolution X", metavar="NUMBER")
parser.add_option("-y", dest="resy", default=500,
                  help="set resolution Y", metavar="NUMBER")

(options, args) = parser.parse_args()

sx=int(options.resx)
sy=int(options.resy)
p=sx*sy	
q=int(p/50000)	# pixel size
phase=0
wlen=int(options.wlen)
levels=100
cx=sx/2
cy=sy/2
i=0
morph_rate=100

pygame.init()

screen=pygame.display.set_mode((sx,sy))
pygame.display.set_caption("ZIVOT NEMA")

running=True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    phase=0.02
    for x in range(sx/q):
	if i > morph_rate :
	    wlen-=0.01
            i=0
	i+=1
        for y in range(sy/q):
            rad=math.sqrt((float(x)-cx/q)**2+(float(y)-cy/q)**2)
            c=int(((math.sin(rad*wlen+phase)*128)+128)/(255/levels))*int(255/levels)
            pygame.draw.rect(screen,(0,c/2,c),(x*q,y*q,q-1,q-1))
	    

    pygame.display.flip()

pygame.quit()

