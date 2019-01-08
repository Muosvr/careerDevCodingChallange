def compareString(word1, word2):
    changeLog = []
    changeScore = 0
    for i in range(len(word1)):
        change = ord(word2[i]) - ord(word1[i])
        changeLog.append(change)
        changeScore += abs(change)
    return changeLog, changeScore

if __name__=="__main__":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    if len(word1) != len(word2):
        print("Words need to have same length")
    else:
        log, score = compareString(word1, word2)
        print("Change log:", log, "Change score:", score)