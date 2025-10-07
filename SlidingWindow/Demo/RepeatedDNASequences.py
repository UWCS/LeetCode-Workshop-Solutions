class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaSeqSet = set()
        toReturn = set()

        for l in range(len(s) - 9):
            r = l + 10
            subStr = s[l:r]
            
            if subStr in dnaSeqSet:
                toReturn.add(subStr)
            else:
                dnaSeqSet.add(subStr)
        
        return list(toReturn)