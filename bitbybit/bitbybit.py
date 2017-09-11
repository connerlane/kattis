while True:
    inp = eval(input())
    if (inp != 0):
        register = ['?' for i in range(32)]
        for i in range(inp):
            instruction = input().split()
            if (instruction[0] == "SET"):
                register[len(register) - 1 - int(instruction[1])] = 1
            elif (instruction[0] == "CLEAR"):
                register[len(register) - 1 - int(instruction[1])] = 0
            elif (instruction[0] == "AND"):
                a = register[len(register) - 1 - int(instruction[1])]
                b = register[len(register) - 1 - int(instruction[2])]
                if (a != '?' and b != '?'):
                    if (a == 1 and b == 1):
                        register[len(register) - 1 - int(instruction[1])] = 1
                    else:
                        register[len(register) - 1 - int(instruction[1])] = 0
                else:
                    if (a == 0 or b == 0):
                        register[len(register) - 1 - int(instruction[1])] = 0
                    else:
                        register[len(register) - 1 - int(instruction[1])] = '?'

            elif (instruction[0] == "OR"):
                a = register[len(register) - 1 - int(instruction[1])]
                b = register[len(register) - 1 - int(instruction[2])]
                if (a == 1 or b == 1):
                    register[len(register) - 1 - int(instruction[1])] = 1
                else:
                    if (a == 0 and b == 0):
                        register[len(register) - 1 - int(instruction[1])] = 0
                    else:
                        register[len(register) - 1 - int(instruction[1])] = '?'
        register = [str(i) for i in register]
        print("".join(register))
    else:
        break
