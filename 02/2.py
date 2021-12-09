# 02

commands = []
lines = open("input.txt", 'r').readlines()
num_commands = len(lines)
for l in lines:
    command, val = l.split(' ')
    commands.append([command, int(val)])

hor, ver = 0, 0
print(f"hor={hor}, ver={ver}")

for i in range(num_commands):
    c, v = commands[i]
    if c[0] == "f":
        hor += v
    elif c[0] == "u":
        ver -= v
    elif c[0] == "d":
        ver += v
    if i > num_commands - 5:
        print(i,":",c,v, "=>", end=" ")
        print(f"hor={hor}, ver={ver}")

print(f"Part 1: hor={hor}, ver={ver}, total={hor*ver}")

hor, ver, aim = 0, 0, 0 
print(f"hor={hor}, ver={ver}")

for i in range(num_commands):
    c, v = commands[i]
    if c[0] == "f":
        hor += v
        ver += aim * v
    elif c[0] == "u":
        aim -= v
    elif c[0] == "d":
        aim += v
    if i < 10 : #> num_commands - 5:
        print(i,":",c,v, "=>", end=" ")
        print(f"hor={hor}, ver={ver}")

print(f"Part 2: hor={hor}, ver={ver}, total={hor*ver}")
