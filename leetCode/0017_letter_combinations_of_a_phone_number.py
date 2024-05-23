# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        output = []
        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(idx, digits, slate):
            if len(slate) == len(digits):
                output.append("".join(slate))
                return
            for i in dictionary[digits[idx]]:
                slate.append(i)
                dfs(idx + 1, digits, slate)
                slate.pop()
        
        dfs(0, digits, [])
        return output
            

        

