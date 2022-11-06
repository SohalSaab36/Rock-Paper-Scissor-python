import random as rd
possible = ["rock","paper","scissor"]
def main():
  player = input("rock paper scissor exit = ")
  cpu = rd.choice(possible)
  print(f"cpu = {cpu}")
  if player == cpu:
    print("draw")
    main()
  elif player == "exit":
    exit()
  elif player != cpu:
    if player == possible[0]:
      if cpu == possible[1]:
        print("cpu won")
      elif cpu == possible[2]:
        print("player won")
      else:
        print("Something went wrong")
      main()
    elif player == possible[1]:
      if cpu ==  possible[0]:
        print("player won")
      elif cpu == possible[2]:
        print("cpu won")
      else:
        print("Something went wrong")
      main()
    elif player == possible[2]:
      if cpu == possible[0]:
        print("cpu won")
      elif cpu == possible[1]:
        print("player won")
      else:
        print("something went wrong")
      main()
    else:
      print("err")
      main()
main()
