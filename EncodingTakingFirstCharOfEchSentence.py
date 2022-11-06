def encode(data) :
    for text in data.split('\n') :
        ch = ''
        for i in range(len(text)) :
            if text[i] == ' ' :
               ch += text[i+1]
            elif i == 0 :
                 ch += text[i]
        print(ch)
        
dat = "hey yo\n whats app\nGames of Throne"
encode(dat)