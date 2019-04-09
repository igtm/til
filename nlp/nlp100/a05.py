def n_gram(str, n):
    result = []
    for i in range(len(str) - n + 1):
       result.append(str[i:i+n])
    return result

if __name__ == '__main__':
    print(n_gram('I am an NLPer', 2))
