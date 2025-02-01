# 11ms
class Solution(object):
  def isPalindrome(self, x):
      """
      :type x: int
      :rtype: bool
      """
      if(x < 0):
          return False

      last = x % 10
      rest = x // 10
      newX = last

      while(rest > 0):
        last = rest % 10
        rest = rest // 10
        newX = newX * 10 + last
      return newX == x

# 5ms

class Solution(object):
  def isPalindrome(self, x):
      """
      :type x: int
      :rtype: bool
      """
      if(x < 0):
          return False
      return int(str(x)[::-1]) == x