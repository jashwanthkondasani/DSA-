
class Solution:
  def longestCommonPrefix(self, strs):
    if not strs:
      return ""
    # prefix = strs[0]
    # for s in strs[1:]:
    #   while not s.startswith(prefix):
    #     prefix = prefix[:-1]
    #     if not prefix:
    #       return ""
    # return prefix
    for i in range(len(strs[0])):
        for s in str:
           if i== len(s) or s[i] != strs[0][i]:
              # return strs[0][:i]
                return res
        res += strs[0][i]
    return res
