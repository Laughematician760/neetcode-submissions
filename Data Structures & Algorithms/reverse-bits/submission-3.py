class Solution:
    def reverseBits(self, n: int) -> int:
        x = ""
        i = 32
        while i > 0:
            last_bit = n & 1
            string_bit = str(last_bit)
            x += string_bit
            n = n >> 1
            i -= 1

        return int(x, 2)

        





        