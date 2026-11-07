class Solution:
    def isHappy(self, n: int) -> bool:
        num_string = str(n)
        square_list = [int(x)*int(x) for x in num_string]
        sum_value = sum(square_list)
        sum_list = [sum_value]
        while sum_value != 1:
            num_string = str(sum_value)
            square_list = [int(x)*int(x) for x in num_string]
            sum_value = sum(square_list)
            if sum_value in sum_list:
                return False
            else:
                sum_list += [sum_value]
        return True


        


        