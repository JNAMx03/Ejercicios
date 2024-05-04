def myFunc(e):
    return e['score']

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        # temp = []
        name = input()
        # temp.append(name)
        score = float(input())        
        # temp.append(score)
        # records.append(temp)
        records.append({'name':name, 'score':score})

    # for i in range(len(records)):
    #     if i != len(records)-1:
    #         j = i + 1
    #     else:
    #         j = len(records)-1
    #     for j in range(len(records)):
    #         if records[i][1] < records[j][1]:
    #             aux = records[i]
    #             records[i] = records[j]
    #             records[j] = aux

    records.sort(key=myFunc)

    for i in range(len(records)):
        if records[i]['score'] < records[i+1]['score']:
            gg = records[i+1]['score']
            break

    names = []
    for i in range(len(records)):
        if records[i]['score'] == gg:
            names.append(records[i]['name'])
        
    names.sort()

    for i in range(len(names)):
        print(names[i])

    
           