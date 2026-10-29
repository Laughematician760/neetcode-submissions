class Solution:
    def isValid(self, s: str) -> bool:
        while s != "":
            indices_list = [s.rfind("["), s.rfind("{"),  s.rfind("(")]
            max_index = max(indices_list)
            if max_index == len(s)-1:
                return False
            if s[max_index] == "[" and s[max_index + 1] == "]" or  s[max_index] == "(" and s[max_index + 1] == ")" or s[max_index] == "{" and s[max_index + 1] == "}":
                s = s[:max_index] + s[max_index + 2: ]
            else:
                return False
        return True




       
        


        