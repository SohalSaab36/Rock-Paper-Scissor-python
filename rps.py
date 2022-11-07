import random as rd
possible = ["rock","paper","scissor"]
def main():
  cscore = 0 
  pscore = 0
  player = input("rock paper scissor ; type exit to end = ")
  cpu = rd.choice(possible)
  print(f"cpu = {cpu}")
  print(f"{Cscore}cpu {Pscore}player")
  if player == cpu:
    print("Tie! ; 0 points added")
    main()
  elif player == "exit":
    exit()
  elif player != cpu:
    if player == possible[0]:
      if cpu == possible[1]:
        print("cpu won")
        cscore = cscore + 1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[2]:
        print("player won")
        pscore = pscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("Something went wrong")
      main()
    elif player == possible[1]:
      if cpu ==  possible[0]:
        print("player won")
        pscore = pscore + 1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[2]:
        print("cpu won")
        cscore = cscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("Something went wrong")
      main()
    elif player == possible[2]:
      if cpu == possible[0]:
        print("cpu won")
        cscore = cscore +1
        print(f"{Cscore}cpu {Pscore}player")
      elif cpu == possible[1]:
        print("player won")
        pscore = pscore +1
        print(f"{Cscore}cpu {Pscore}player")
      else:
        print("something went wrong")
      main()
    else:
      print("err")
      main()
main()
