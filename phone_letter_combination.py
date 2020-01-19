teleDict = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def letterCombRecursive(result, letter):
    if letter == '':
        return result
    else:
        if result == []:
            result = teleDict[letter[0]]
        else:
            temp = result
            for i in teleDict[letter[0]]:
                result = result + list(map(lambda x: x + i, temp))
            result = result[len(temp):]
        if len(letter) == 1:
            letter = ''
        else:
            letter = letter[1:]
        return letterCombRecursive(result, letter)


############### TEST ###############
print(letterCombRecursive([], "234"))
