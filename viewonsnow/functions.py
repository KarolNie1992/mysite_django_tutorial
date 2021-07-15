def viewOnSnow(data):
    dataNew = data.copy()

    for i in range(len(dataNew)):
        #zakładam że pierwszy i ostatni nie zmienia sie
        if i == 0 or i == len(dataNew)-1:
            continue
        else:
            maxDic = {
                'maxL':dataNew[i],
                'maxR':dataNew[i]
            }
            endIdx = len(dataNew) - 1
            #sprawdz najwyższą w lewo 
            for l in range(i + 1):
                if dataNew[l] > maxDic['maxL']:
                    maxDic['maxL'] = dataNew[l]
            
            #Sprawdz najwyższą w prawo
            r = i
            for _ in range(endIdx-r+1):
                if dataNew[r] > maxDic['maxR']:
                    maxDic['maxR'] = dataNew[r]
                r+=1
            
            #przypisanie do newValue mniejszej wartości ze słownika maxDic
            newValue = maxDic[min(maxDic, key = maxDic.get)]
            if dataNew[i] != newValue or dataNew[i] < newValue:
                dataNew[i] = newValue
    return dataNew