import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for x in list(string.ascii_lowercase):
            if x not in sentence:
                return False
        return True
