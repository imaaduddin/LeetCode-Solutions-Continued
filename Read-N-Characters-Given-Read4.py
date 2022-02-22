# Question difficulty: Easy
# Question number: 157
# Question url: https://leetcode.com/problems/read-n-characters-given-read4/

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
        buf4 = [''] * 4
        num_read = 0
        EOF = False
        while num_read < n and not EOF:
            curr_read = read4(buf4)
            delta = min(curr_read, n - num_read)
            buf[num_read:num_read + delta] = buf4[:delta]
            num_read += delta
            if curr_read < 4:
                EOF = True 
        return num_read