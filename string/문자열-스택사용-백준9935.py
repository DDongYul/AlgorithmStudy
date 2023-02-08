string = input()
bomb_string = input()
end_bomb = bomb_string[-1]
stack = []
length = len(bomb_string)
for i in string:
    stack.append(i)
    if i == end_bomb:
        if ''.join(stack[-length:]) == bomb_string:
            del stack[-length:]

rst = ''.join(stack)
if rst == '':
    print("FRULA")
else:
    print(rst)