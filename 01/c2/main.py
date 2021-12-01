infile = open('01\c2\infile.txt', 'r')
infile = [int(i) for i in infile.read().splitlines()]

depths = []
new_depths = []
larger = 0

for line in infile:
    depths.append(line)

window_depths = [sum(depths[i:i+3]) for i in range( len(depths))]

for index in range(1, len(window_depths)):
    if (window_depths[index] > window_depths[index - 1]):
        larger += 1

print(larger)
