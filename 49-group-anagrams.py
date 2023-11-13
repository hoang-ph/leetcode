import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity m * n where m is the length of string strs, n is the average length of each word

        result = collections.defaultdict(list) # mapping charCount to list of Anagrams
        for string in strs:
            # compute the count
            count = [0] * 26 # a...z
            for char in string:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(string)
        return result.values()

    def groupAnagramsSortedVersion(self, strs: List[str]) -> List[List[str]]:
        # time complexity m * nlogn
        result = collections.defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            result[sortedWord].append(word)
        return result.values()