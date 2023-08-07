class Solution:
    def reverseBits(self, source: int) -> int:                                            # Reverse the bits from a given integer using bit-wise operations
      target = 0
      mask   = 1
      for i in range(32):                                                                 # Loop through each bit of the source
        target <<=  1                                                                     # Shift target to the left by 1 iff source is not == 0
        b = source & mask                                                                 # Extract right-most bit from source
        if(b == 1):   
          target |=  mask                                                                 # Put the right-most bit into the target
        source >>= 1                                                                      # Shift source to the right by 1
      print("{:032b}".format(target))
      return target

sol = Solution()
sol.reverseBits(0b1101)
sol.reverseBits(0b00000010100101000001111010011100)
    
      
# step 1: extract right-most bit from source
# step 2: put the right-most bit into the target
# step 3: shift source to the right by 1
# step 4: shift target to the left  by 1 iff source is not == 0
