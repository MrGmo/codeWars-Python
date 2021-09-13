def rake_garden(garden):
    g = garden.split()
    for i in range(len(g)):
        if g[i] == 'rock' or g[i] == 'gravel':
            pass
        else:
            g.remove(g[i])
            g.insert(i,'gravel')
    return ' '.join(g)