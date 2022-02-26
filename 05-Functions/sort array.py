def sortString(anagramArray):        
    done = False
    while not done:
        i = 1
        done = True
        while i < len(anagramArray):            
            if anagramArray[i-1] > anagramArray[i]:
                done = False
                tempString = anagramArray[i]
                anagramArray[i] = anagramArray[i-1]
                anagramArray[i-1] = tempString            
               
            print(i,tempString,anagramArray)
            i = i + 1

        #end of while i < len
    #end of while not done

    print("anagramArray is ",anagramArray)
    return anagramArray