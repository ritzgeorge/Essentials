def connect(field,doct):
    for i in range(14):
        c=int(i/2)
        if i%2==0:
            for b in range(14):
                a=int(b/2)
                if b!=13:
                    if b%2==0:
                        print(field[a][c],end='')
                    else:
                        print('|',end='')
                        
                else:
                    print('')      
        else:
            print('--------------')

    for i in range(7):
        if doct[i][0]==doct[i][1]==doct[i][2]==doct[i][3]=='X'or doct[i][4]==doct[i][1]==doct[i][2]==doct[i][3]=='X' or doct[i][5]==doct[i][4]==doct[i][2]==doct[i][3]=='X'or doct[i][5]==doct[i][4]==doct[i][6]==doct[i][3]=='X':
            print('player 1 winner')
        elif doct[i][0]==doct[i][1]==doct[i][2]==doct[i][3]=='O'or doct[i][4]==doct[i][1]==doct[i][2]==doct[i][3]=='O' or doct[i][5]==doct[i][4]==doct[i][2]==doct[i][3]=='O'or doct[i][5]==doct[i][4]==doct[i][6]==doct[i][3]=='O':
            print('player 2 winner')
    for i in range(7):
        if doct[0][i]==doct[i][1]==doct[2][i]==doct[3][i]=='X'or doct[4][i]==doct[1][i]==doct[2][i]==doct[3][i]=='X' or doct[5][i]==doct[4][i]==doct[2][i]==doct[3][i]=='X'or doct[5][i]==doct[4][i]==doct[6][i]==doct[3][i]=='X':
            print('player 1 winner')
        elif doct[0][i]==doct[i][1]==doct[2][i]==doct[3][i]=='O'or doct[4][i]==doct[1][i]==doct[2][i]==doct[3][i]=='O' or doct[5][i]==doct[4][i]==doct[2][i]==doct[3][i]=='O'or doct[5][i]==doct[4][i]==doct[2][i]==doct[3][i]=='O':
            print('player 2 winner')




player=1
standardvalues=[[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
print(standardvalues)
dictionary={}
dictionary=standardvalues
print(dictionary)
print(dictionary[2][1])
while(True):
    print('player turn is ',player)
    column=int(input('enter column= '))
    p=column
    if player==1:
        if standardvalues[column][0]==' ':
            x=6
            for y in range(7):
                if standardvalues[column][x]==' ':
                    standardvalues[column][x]='X'
                    dictionary[column][x]='X'
                    break
                else:
                    x-=1    
            player=2
    else:
        if standardvalues[column][0]==' ':
            x=6
            for y in range(7):
                if standardvalues[column][x]==' ':
                    standardvalues[column][x]='O'
                    dictionary[column][x]='O'
                    break
                else:
                    x-=1
            player=1

    connect(standardvalues,dictionary)
    


    
