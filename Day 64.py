class Solution:
    def anagrams(self, A):
        anagram_groups = {}
        for i in range(len(A)):
            sorted_str = ''.join(sorted(A[i]))
            if sorted_str in anagram_groups:
                anagram_groups[sorted_str].append(i + 1)
            else:
                anagram_groups[sorted_str] = [i + 1]
        return list(anagram_groups.values())
