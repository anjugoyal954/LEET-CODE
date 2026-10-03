class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        output = 0

        for index, i in enumerate(columnTitle):
             output += (ord(i) - ord("A") + 1) * 26 ** index

        return output
        