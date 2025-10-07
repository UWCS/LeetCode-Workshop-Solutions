def solution(aStr: str):
    uniqueStrings = set()

    for l in range(len(aStr) - 2):
        r = l + 3
        aSubstring = aStr[l:r]

        uniqueStrings.add(aSubstring)
    
    return len(uniqueStrings)

print(solution("ABBCDADCABBA"))