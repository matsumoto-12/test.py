with open("test.txt", encoding="utf-8") as test:
    word=[]
    word.append(test.readline())
    while ':' in word[-1]:
        word.append(test.readline())
    else:
        last=int(word[-1])
        word.pop()

    for i in range(len(word)):
        word[i]=word[i][:-1]
    #文字列としてwordに格納したのを数字と単語にわけてwordsに格納
    words={}
    for i in range(len(word)):
        number,w=word[i].split(':')
        number=int(number)
        words[number]=w

    #iの順にタプルのリストに格納
    #約数が1つも無かった時の状態をnothingとする
    nothing=True
    words=sorted(words.items())
    for i,j in words:   #最後の数字の約数である場合、単語を表示し、nothingをfalseにする
        if last%i==0:
            print(j,end='')
            nothing=False
    #全て約数で無かったとき最後の数字を表示する
    if nothing==True:
        print(last)
