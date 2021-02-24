



genres = ['pop', 'classic', 'classic', 'classic', 'jazz','ex','jazz']
plays = [500, 600, 150, 800, 2500,700, 2500]

dic = {}

answer = []
for genre, play in zip(genres, enumerate(plays)):
    if genre not in dic.keys():
        dic[genre] = [play]
    else:
        dic[genre].append(play)

print(dic)
print(sorted(dic))
genreSort = sorted(dic, key = lambda x: sum(map(lambda y: y[1], dic[x])), reverse=True)

print(genreSort)
