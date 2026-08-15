class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        best = 0
        for right in range(len(s)):
            # expand: add s[right] to count, update max_freq
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # if window is invalid, shrink from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1           # decrement count[s[left]]
                left += 1

            # update best
            best = max(best, right - left + 1)
        return best