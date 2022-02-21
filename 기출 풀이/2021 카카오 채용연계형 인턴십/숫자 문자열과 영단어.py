# 10분

def solution(s):
    num = ""
    answer = ""
    for word in s:
        if word == "0" or word == "1" or word == "2" or word == "3" or word == "4" or word == "5" or word == "6" or word == "7" or word == "8" or word == "9":
            answer += word
            continue
        num += word
        if num == "zero":
            num = ""
            answer += "0"
        elif num == "one":
            num = ""
            answer += "1"
        elif num == "two":
            num = ""
            answer += "2"
        elif num == "three":
            num = ""
            answer += "3"
        elif num == "four":
            num = ""
            answer += "4"
        elif num == "five":
            num = ""
            answer += "5"
        elif num == "six":
            num = ""
            answer += "6"
        elif num == "seven":
            num = ""
            answer += "7"
        elif num == "eight":
            num = ""
            answer += "8"
        elif num == "nine":
            num = ""
            answer += "9"

    answer = int(answer)
    return answer