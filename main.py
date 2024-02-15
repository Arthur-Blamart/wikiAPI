from include import *

Linus = getPage('Linus Torvalds')
toFind = getPage('Lybie')

print(getLinked(getLinked(Linus)[0])[0])

prof = howLongFromAToB(Linus, toFind, 5)

print(prof)