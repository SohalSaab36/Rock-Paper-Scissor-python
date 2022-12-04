import random as rd
p =    ["rock","paper","scissor"]
TS = 0
cs =    0
ps =    0
RUN =    True
def conf():
  while True:
        pl = input("continue (y/n): ").lower()
        if pl == "y":
          break
        else:
           if pl == "n":
                if cs ==    ps:
                    if TS >    0:
                        print("tied")
                    else:
                        print("no scores :)")
                elif cs >    ps:
                    print("you lose")
                elif cs <    ps:
                    print("player won")
                else:
                    print("debug: conf()")
                exit()
           else:
                if pl == "y":
                    break
                else:
                    conf()
while RUN:
            TS =    cs + ps
            player =    input(f"{p}: ").lower()
            cpu =    rd.choice(p)
            print(f"cpu chose {cpu}")
            print(f"cpu score {cs}   ; player score {ps}")
            
            if player == cpu:
                print("as usual tied")
                conf()
            elif player !=    cpu and player in p:
                if player ==    p[0]:
                    if cpu ==    p[1]:
                        print("you lose")
                        cs =    cs + 1
                        print(f"cpu score {cs}   ; player score {ps}")
                        conf()
                    elif cpu==p[2]:
                        print("player won")
                        ps =    ps + 1
                        print(f"cpu score {cs}   ; player score {ps}")
                        conf()
                    else:
                       print("RESTART")
                       conf()
                elif player ==    p[1]:
                     if cpu ==    p[0]:
                         print("you won")
                         ps =    ps+1
                         print(f"cpu score {cs}   ; player score {ps}")
                         conf()
                     elif cpu ==    p[2]:
                         print("you lose")
                         cs =    cs+1
                         print(f"cpu score {cs}   ; player score {ps}")
                         conf()
                     else:
                         print("RESTART")
                         conf()
                elif player ==    p[2]:
                    if cpu ==    p[0]:
                        print("you lose")
                        cs =    cs+1
                        print(f"cpu score {cs}   ; player score {ps}")
                        conf()
                    elif cpu ==    p[1]:
                        print("you won")
                        ps =    ps+1
                        print(f"cpu score {cs}   ; player score {ps}")
                        conf()
                    else:
                        print("RESTART")
                        conf()                       
            else:
                   print("wrong input restart")
                   conf()
