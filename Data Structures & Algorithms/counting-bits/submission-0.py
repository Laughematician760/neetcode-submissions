class Solution:
    def countBits(self, n: int) -> List[int]:
        initial_num_list = [0]
        for i in range(1, n+1):
            k = 0
            for j in range(len(format(i, 'b'))):
                string_binary_rep = format(i, 'b')
                if int(string_binary_rep[j]) == 1:
                     k += 1
                else:
                    continue
            initial_num_list += [k]
        return initial_num_list






        