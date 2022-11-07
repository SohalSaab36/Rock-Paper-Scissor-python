import random as rd
Pscore = 0 #player
Cscore = 0 #cpu
possible = ["rock","paper","scissor"]
def main():
  player = input("rock paper scissor exit = ")
  cpu = rd.choice(possible)
  print(f"cpu = {cpu}")
  print(f"{Cscore}cpu {Pscore}player")
  if player == cpu:
    print("draw 0 points added")
    main()
  elif player == "exit":
    exit()
  elif player != cpu:
    if player == possible[0]:
      if cpu == possible[1]:
        print("cpu won")
        Cscore = Cscore + 1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[2]:
        print("player won")
        Pscore = Pscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("Something went wrong")
      main()
    elif player == possible[1]:
      if cpu ==  possible[0]:
        print("player won")
        Pscore = Pscore + 1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[2]:
        print("cpu won")
        Cscore = Cscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("Something went wrong")
      main()
    elif player == possible[2]:
      if cpu == possible[0]:
        print("cpu won")
        Cscore = Cscore +1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[1]:
        print("player won")
        Pscore = Pscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("something went wrong")
      main()
    else:
      print("err")
      main()
main()
