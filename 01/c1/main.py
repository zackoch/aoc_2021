infile = open('01\c1\infile.txt', 'r')
infile = [int(i) for i in infile.read().splitlines()]

depths = []
larger = 0

for line in infile:
    depths.append(line)

for index in range(1, len(depths)):
    if (depths[index] > depths[index - 1]):
        larger += 1

print(larger)


