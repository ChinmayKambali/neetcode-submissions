class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '[]' in s or '{}' in s:
        #     s=s.replace('()','')
        #     s=s.replace('{}','')
        #     s=s.replace('[]','')
        # return s==''


        last_opened=[]
        open_close={"(":")","{":"}","[":"]"}
        for c in s:
            if c in ["(","{","["]:
                last_opened.append(c)
            if c in [")","}","]"]:
                if len(last_opened)==0: return False
                if not c==open_close[last_opened.pop()]: return False
        
        return (len(last_opened)==0)