
n = 13

def solve(players):
    in_binary = '{0:08b}'.format(players)
    index = in_binary.find('1')
    binary_list = list(in_binary)
    del binary_list[index]
    binary_list.append('1')
    str_binary = ''.join(binary_list)
    winning_seat = int(str_binary, 2)
    return winning_seat

print(solve(n))

