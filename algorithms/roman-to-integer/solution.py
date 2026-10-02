class Solution:
    def romanToInt(self, s: str) -> int:
        dictt = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        output = 0
        for i in range(len(s)-1) :
            curr = s[i]
            nextt = s[i+1]
            if dictt[curr] >= dictt[nextt] :
                output += dictt[curr]
            else:
                output -= dictt[curr]
        output += dictt[s[-1]]
        return output
 


            
            

            


        

        
        