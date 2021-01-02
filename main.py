from pygame         import MOUSEBUTTONDOWN as M
from pygame.display import set_mode        as S
from pygame.display import flip            as F
from pygame.mouse   import get_pos         as G
from pygame.image   import load            as L
from pygame.event   import get             as E
from pygame         import init            as I

exec('I();s,a,p,q,w,W=S((800, 575)),[0]*9,1,lambda x:200+150*(x%3),lambda x:6'\
'7+x//3*150,enumerate;c=lambda b:max(a[c//5]&a[c//5+c%5]&a[c//5+c%5*2]for c i'\
'n[1,3,4,8,12,13,16,31])\nwhile not c(a):\n for v in E():\n  if 600>G()[0]>20'\
'0and 508>G()[1]>67and v.type==M:\n   a[(G()[0]-200)//133+(G()[1]-67)//133*3]'\
'=p;p^=3\n [s.blit(L("ox"[-i]+".png"),(q(e),w(e)))for e,i in W(a)if i];F()')