class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            remainder = columnNumber % 26
            quotient = columnNumber // 26

            if remainder == 0 :
                res += "Z"
                quotient -= 1
            else:
                res += chr(65 + remainder - 1)

            columnNumber = quotient
        return res[::-1]
        