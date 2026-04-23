'''Given an array of strings strs, group the anagrams together. You can return the answer
in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''

def groupAnagrams(strs):
    anagram_map = {}

    for word in strs:
        key = ''.join(sorted(word))  # sorted string as key
        
        if key not in anagram_map:
            anagram_map[key] = []
        
        anagram_map[key].append(word)

    return list(anagram_map.values())


# 👇 Run example
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Output:", groupAnagrams(strs))