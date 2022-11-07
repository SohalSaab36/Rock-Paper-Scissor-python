import random as rd
possible = ["rock","paper","scissor"]
while True:
  cscore = 0
  pscore = 0
  player = input("rock paper scissor ; type exit to end = ").lower()
  cpu = rd.choice(possible)
  print(f"cpu = {cpu}")
  print(f"{cscore}cpu {cscore}player")
  if player == cpu:
    print("Tie! ; 0 points added")
  elif player == "exit":
    break
  elif player != cpu:
    if player == possible[0]:
      if cpu == possible[1]:
        print("cpu won")
        cscore = cscore + 1
        print(f"{cscore}cpu {cscore}player")
      elif cpu == possible[2]:
        print("player won")
        pscore = pscore +1
        print(f"{cscore}cpu {pscore}player")
      else:
        print("Something went wrong")

    elif player == possible[1]:
      if cpu ==  possible[0]:
        print("player won")
        pscore = pscore + 1
        print(f"{cscore}cpu {cscore}player")
      elif cpu == possible[2]:
        print("cpu won")
        cscore = cscore +1
        print(f"{cscore}cpu {pscore}player")
      else:
        print("Something went wrong")

    elif player == possible[2]:
      if cpu == possible[0]:
        print("cpu won")
        cscore = cscore +1
        print(f"{cscore}cpu {pscore}player")
      elif cpu == possible[1]:
        print("player won")
        pscore = pscore +1
        print(f"{cscore}cpu {pscore}player")
      else:
        print("something went wrong")

    else:
      print("error : try again ")
