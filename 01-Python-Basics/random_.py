from random import choice,randint,shuffle


'''
coin=choice(["heads", "tails"])
print(coin)

random_number=randint(1,10)
print(random_number)
'''
cards=["jack","queen","king","ace","2","3","4","5","6","7","8","9","10"]
shuffle(cards)
#print(cards)

for card in cards:
    print(card)