from __future__ import annotations

def remove_odds(nums: set[int]) -> set[int]:
    result = set()
    for i in nums:
        if i % 2 == 0:
            result.add(i)
    return result

def vowel_captilization(string: str) -> str:
    vowels = set("aeiouAEIOU")
    result = []
    for i in string:
        if i in vowels:
            result.append(i.upper())
        elif i.isalpha():
            result.append(i.lower())
        else:
            result.append(i)
    #TODO: implement this function
    return "".join(result)

