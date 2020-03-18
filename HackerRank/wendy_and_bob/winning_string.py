

def gameWinner(colors):
    player = "wendy"
    while colors != '':
        # print(colors, "turn=", player)
        colors = makeMove(colors, player)
        if colors != '':
            player = swapPlayers(player)
    return swapPlayers(player)

def swapPlayers(name):
    if name == 'wendy':
        return 'bob'
    else:
        return 'wendy'

def makeMove(colors, name):
    stringToFind = ''
    if name == 'bob':
        stringToFind = 'bbb'
    else:
        stringToFind = 'www'
    
    if stringToFind not in colors:
        return ''
    else:
        colors = colors.replace(stringToFind, stringToFind[0] + stringToFind[2], 1)
        return colors


colors = 'wwwbb'
print(gameWinner(colors))




