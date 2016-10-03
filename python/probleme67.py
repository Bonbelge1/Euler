with open('probleme67.txt', 'r') as f:
    data = f.read().splitlines()

#new_data = [[int(string) for string in line.split(' ')] for line in data]
M = []
for line in data:
    string_list = line.split(' ')
    int_list = []
    for string in string_list:
        int_list.append(int(string))

    M.append(int_list)

for row in range((len(M) - 1), 0, -1):
    for col in range(0, row):
        M[row - 1][col] = M[row - 1][col] + max(M[row][col], M[row][col + 1])

print(M[0][0])