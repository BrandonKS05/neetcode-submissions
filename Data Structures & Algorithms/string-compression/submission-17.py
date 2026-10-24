class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        left = 0 
        right = 0
        while right < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            window = right - left

            if window == 1:
                chars[idx] = chars[left]
                idx += 1

            else:
                chars[idx] = chars[left]
                idx += 1

                digit = str(window)
                print(digit)
                for ch in digit:
                    chars[idx] = ch
                    idx += 1
            left = right
        return idx 
