#!/usr/bin/env python
import random
stay = 0
switch = 0
stay_success = 0
switch_success = 0
doors = ['goat', 'goat', 'car']

for x in range(1,100000):
  guess = random.randrange(3)
  
  # unnecessary step
  # shown_goats doesn't really matter, but see below
  for index, door in enumerate(doors):
    if (door == 'goat' and index != guess):
      shown_goat = index
  # we randomize whether we stay or switch
  coin_flip = random.randint(0,1)
  if (coin_flip == 0):
    #stay
    stay = stay+1
    if (doors[guess] == 'car'):
      stay_success = stay_success+1
  else:
    #switch 
    switch = switch+1
    # technically, there is no reason to derive switched_guess
    # but it makes the following if() more intuitive
    for index, door in enumerate(doors):
      if (index != guess and index != shown_goat):
        switched_guess = index

    # we could instead do doors[guess] != 'car'
    # see: http://stackoverflow.com/questions/1247863/monty-hall-problem/1247888#1247888
    if (doors[switched_guess] == 'car'):
      switch_success = switch_success+1

print "stay: " + str(stay_success) + " for " + str(stay) + " " +  str(stay_success/float(stay)*100) + "%"
print "switch: " + str(switch_success) + " for " + str(switch)  + " " +  str(switch_success/float(switch)*100) + "%"
      

