class Solution:
    def romanToInt(self, s: str) -> int:
        # value - [intValue, index]
        lookupDict = {
            'I': 1,'V': 5,'X': 10,'L': 50 ,'C':100,'D':500 ,'M':1000
        }
        # s - IX
        # s - III
        return_value = 0
        idx=0
        while(idx < (len(s)-1)):
            curr = s[idx] # I - 1
            next = s[idx+1] # X - 10
            if(lookupDict[next] > lookupDict[curr]):
                return_value += (lookupDict[next] - lookupDict[curr])
                idx += 2
            elif(lookupDict[next] < lookupDict[curr]):
                return_value += lookupDict[curr]
                idx += 1
            else:
                tmp = lookupDict[next] + lookupDict[curr]
                return_value += tmp
                idx+=2
            # print("return_value: ", return_value)
        
        # print("idx::", idx)
        if(idx != len(s)):
            last_one = s[-1]
            return_value += lookupDict[last_one]
        
        return return_value
