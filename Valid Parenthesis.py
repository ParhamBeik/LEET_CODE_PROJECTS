# s = "()[]{}"
# def test():
#     for num in range(len(s)):
#         if len(s)==2:
#             if (s[num]=="(" and s[num+1]==")") or (s[num]=="[" and s[num+1]=="]") :
#                 return True
#             else:
#                 return False
#         if len(s)==4:
#             if ((s[num]=="(" and s[num+1]==")") or (s[num]=="[" and s[num+1]=="]") or (s[num]=="{" and s[num+1]=="}")) and ((s[num+2]=="(" and s[num+3]==")") or (s[num+2]=="[" and s[num+3]=="]") or (s[num+2]=="{" and s[num+3]=="}")):
#                 return True
#             else:
#                 return False
#         if len(s)==6:
#             if ((s[num]=="(" and s[num+1]==")") or (s[num]=="[" and s[num+1]=="]") or (s[num]=="{" and s[num+1]=="}")) and ((s[num+2]=="(" and s[num+3]==")") or (s[num+2]=="[" and s[num+3]=="]") or (s[num+2]=="{" and s[num+3]=="}")) and ((s[num+4]=="(" and s[num+5]==")") or (s[num+4]=="[" and s[num+5]=="]") or (s[num+4]=="{" and s[num+5]=="}")):
#                 return True
#             else:
#                 return False

# print(test())