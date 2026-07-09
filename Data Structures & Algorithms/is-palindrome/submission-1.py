class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9 ]', '', s)
        clean_text = clean_text.lower().replace(" ","")
    
        l, r = 0, len(clean_text) - 1
        while l <= r:
            if clean_text[l] != clean_text[r]:
                return False
            l += 1
            r -= 1
        return True
