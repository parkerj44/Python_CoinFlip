import random

def coinflip():

  var = random.random()
  
  if var < .5:
    result = 'Heads'
  else:
    result = "Tails"

  return result


def all_heads(count):

  attempts = 0 
  result = False

  while result == False:
    i = 0
    flip = 'Heads'
    while i < count and flip == 'Heads':
      flip = coinflip()
      i+=1
      if i == count - 1 and flip == 'Heads':
        result = True

    attempts += 1

  print("It took {} attempts to get {} Heads in a row.".format(attempts, count))


print("This game checks how many times it takes to get n amount of heads in a row.")
user_choice = int(input("Enter a number to test: "))

all_heads(user_choice)
