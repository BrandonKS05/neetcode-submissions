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

            if window > 1:
                chars[idx] = chars[left]
                idx += 1

                digit = str(window)
                print(digit)
                for ch in digit:
                    chars[idx] = ch
                    idx += 1
            left = right
        return idx 
           


       

        
     
        for i in range(1, len(chars)):

            if chars[i] == pivot:
                freq += 1

            if chars[i] != pivot:
                chars[idx] = pivot
                pivot = chars[i]

                if freq == 1:
                    idx += 1
                    freq = 1
                    continue

                else:
                    compressed = compress_int(freq)
                    for i in range(len(compressed)):
                        chars[idx] = compressed[i]
                        idx += 1
                    freq = 1

                

            if freq == len(chars):
                compressed = compress_int(freq)
                for i in range(len(compressed)):
                    chars[idx] = compressed[i]
                    idx += 1

        return idx
            
        
        


         
            
            

        
            
            
            

            



        

            


        
        
