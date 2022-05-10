from re import S


def smallestStringWithSwaps(s, pairs):
        res = []
        for x, y in sorted(pairs):
            new = list(s)
            new[x],new[y] = new[y],new[x]
            s = ''.join(new)
            res.append(s)
            
        print(res)    
        res.sort()
        
        
        print(res[0])

smallestStringWithSwaps('dcab', [[0,3],[1,2],[0,2]])