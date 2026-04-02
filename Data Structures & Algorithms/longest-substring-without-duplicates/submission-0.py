class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lpos = 0
        _max = 0
        curr = set()

        for i, c in enumerate(s):
            if c in curr:
                j = lpos
                while s[j] != c and j < i:
                    curr.remove(s[j])
                    j += 1

                if j < i:
                    lpos = j + 1

            curr.add(c)
            _max = max(_max, i - lpos + 1)

        return _max
