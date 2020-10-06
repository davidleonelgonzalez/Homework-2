# David Gonzalez
# 1630338

if __name__ == '__main__':
    word = input()
    phr = ''
    rev = ''
    for ch in word.lower():
        if ch != '':
            phr += ch
            rev = ch + rev
    if phr == rev:
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')

