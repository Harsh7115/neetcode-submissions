class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_lst = []
        seen = []

        for i in range(len(strs)):
            if sorted(strs[i]) not in seen:
                sub_list = []
                sub_list.append(strs[i])
                seen.append(sorted(strs[i]))
                for j in range(i+1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        sub_list.append(strs[j])
                final_lst.append(sub_list)
            else:
                continue
        return final_lst
        