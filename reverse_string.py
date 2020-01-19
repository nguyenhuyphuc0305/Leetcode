def reverseString(s):
    if s == "":
        return s
    else:
        return reverseString(s[1:]) + s[0]

############### TEST ###############
# test = "phuc"
# print(reverseString(test))
