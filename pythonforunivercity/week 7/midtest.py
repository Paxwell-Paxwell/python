score = []
with open('midTermScore_grp01.csv', 'r') as fp:
    i = 0
    for line in fp:
        if i != 0:
            score.append(int(line.strip().split(',')[7]))
        i += 1
    score.sort()
    print(score)
    totalstd = i
    maxscore = score[-1]
    minscore = score[0]
    total = 0
    for j in score:
        total += j
    av = total / len(score)
    x = 0
    for i in score:
        x += (i - av) ** 2
    std = (x / len(score)) ** 0.5
print(totalstd)
print(f'{maxscore} {av:.2f} {std:.2f} {minscore}')