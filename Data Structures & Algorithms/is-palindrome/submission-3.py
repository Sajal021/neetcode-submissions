class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split()
        s = "".join(s)
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 = s1 + i
        s1 = s1.lower()
        s2 = s1[::-1] 
        return (s2==s1)
            
       

        
        