class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for strings in strs:
            word = strings + "||"
            encoded_string += word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        final_list = s.strip().split("||")

        final_list.pop()

        return final_list

