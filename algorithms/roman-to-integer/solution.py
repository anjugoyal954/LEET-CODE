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
        ans = 0
        for i in range(len(s)-1):
            curr = s[i]
            nexxt = s[i+1]
            if dictt[curr] >= dictt[nexxt] :
                ans += dictt[curr]
            else:
                ans -= dictt[curr]
        ans += dictt[s[-1]]
        return ans




        