values = range(1,11)+'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck=['%s of %s '%(v,s) for v in values for s in suits ]
from pprint import pprint
from random import shuffle
shuffle(deck)

while deck: raw_input(deck.pop())
