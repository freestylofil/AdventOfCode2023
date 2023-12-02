with open('C:/Users/freyf/OneDrive/Pulpit/Filip/inne/programy/AdventOfCode2023/source/2.txt', 'r') as input_file:
    lines = input_file.readlines()

#red, green, blue = 12, 13, 14

sum_id = 0
sum_power = 0
for i, line in enumerate(lines):
    #possible = True
    games = line.strip().split(": ")[1]
    id_game = i+1
    games = games.split("; ")
    min_r, min_g, min_b = 0,0,0
    for game in games:
        tokens = game.split(", ")    
        for token in tokens:
            num_color = token.split(' ')
            #if (num_color[1] == "red" and int(num_color[0])>red) or (num_color[1] == "green" and int(num_color[0])>green) or (num_color[1] == "blue" and int(num_color[0])>blue):
            #    possible = False
            #    break
        #if not possible:
        #    break
            if num_color[1] == "red" and int(num_color[0]) > min_r:
                min_r = int(num_color[0])
            if num_color[1] == "green" and int(num_color[0]) > min_g:
                min_g = int(num_color[0])
            if num_color[1] == "blue" and int(num_color[0]) > min_b:
                min_b = int(num_color[0])
    sum_power += min_r*min_g*min_b

    #sum_id += id_game if possible else 0
#print(sum_id)
print(sum_power)