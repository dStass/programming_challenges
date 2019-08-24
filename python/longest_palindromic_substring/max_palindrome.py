'''
From: Daily Interview Pro 19/08/2019
Problem: Longest Palindromic Substring

A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s):
      all_found = {}
      string_length = len(s)
      index = 0
      to_return = ""

      # for each char in string say index i, we check:
      # if palindrome of substring from index i to i+1, i+2, ... exist
      # in main str, done by adding a reverse clone of itself with both
      # versions of palindrome "odd" and "even"
      # e.g. cat as a palindrome = cattac (even) and catac (odd)
      # "- len(to_return)" optimisation:
      # we don't need to check if any further palindromes exist if its len
      # is less than max
      #
      # Small modificaiton to specs as unclear
      # When two or more palindromes of the same max length found, return
      # the first occurence
      # special characters (. , ? / ; etc) treated as standard digit and will
      # not be ignored
      while index < string_length - len(to_return):
        at_index = s[index]
        upto = index + 1
        while upto < string_length:
          if upto - index < len(to_return)/2:
            upto += 1
            continue
          if upto-index > string_length/2:
              break
          to_find = s[index : upto]
          palindromes = [to_find[:-1] + to_find[::-1], to_find + to_find[::-1]]
          for p in palindromes:
            if len(p) > (1 if len(to_return) == 0 else len(to_return)):
              if p in s:
                to_return = p
          upto += 1
        index += 1
      return to_return

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

s2 = "kyyatgsmzhjvltnzfrfalwuludmcimbzikybxxtqteyqybqvoqikwxuusokyftbevgkrjfmixfwttekxefyxoubrjqwgsjlblpzspbmafniphgpyqsyggadrgxwfsrjrfbhpoommsczupwweexywitxyjytihfmszykwsjmklqfrdhkysiwktqlcnrtcogddgsdsmxvckjasdvlmwrmctxtdtxyvsmlkxtvzbmnpqcemhpsfahztupfsksmfiniczuxxjdjyzlvibtuxnmqtzynalfmeybathheucfrnbvdacnvwjnlaxzbqecwifmrwgnzkriaecubkflcjdtfwvgmqgpmrgsggyzenevuamhhlwelrkdcstfdsbznnyupbdvefbchiwsigfhfxdqivxjyfnylnzlliqqvppozkciepiahcqhimxzdybuhhsuibvmytumljtvnwgmiorlhfnqtfuawalrcxwhhvgsmuoiwmfyhszbcibylbjkhhhkfsuztgnffqigddepefxfvseflrojpfsfgthvkgjggovcqgpdtpxkgktlmqxrnzifkgdvivzfadpsbhhffbmitytakghrxbsbcipekoxpuuyfwrndapduaffsmbremysrzyvfebuxbhxwoqufdokcnnfvksyoiklvlyykkvxjhnfhjfimebwamgjfilequcatbzkhlpmldibeelhuphgfaskbzvgnjahgbcaanmmzuseckxfixhqibbeamaetznalxbsapnisplijrgcqrqjlmhrdfqhxsoppihokgpmqyelcajfmniwdmymasadjyebbzipyisitkorsxjnzjhxvoakenrtrotafznpdsbfiuaavldfzkmlerhskafapxeopwmijusczqjvsoguytdnejewjwqcvotkuamudobbsosvwvraiidxandadpzdzyxurvhbpcffswaoncxckyxwfxrswlrbhsqlxeahklbpqctb"
print(str(Solution().longestPalindrome(s2)))
