def cleanup(strs):
    cleanUpU = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz@'
    for letters in strs.lower():
        if letters in alphabet:
            cleanUpU += letters
        else:
            cleanUpU += ' '
    return cleanUpU
    
numTweets = 0
tMax = ''
tMax2 = 0

with open('elon-musk.txt') as tweets:
    for lines in tweets:
        if tMax2 < len(lines.split()):
            tMax2 = len(lines.split())
            tMax = lines
        numTweets += 1

print('Number of tweets: ', numTweets)
print('tweet with max number of words: ', tMax)
findingT = {}
with open('elon-musk.txt') as tweets1:
    for lines in tweets1:
        for tWords in cleanup(lines).split():
            if '@' in tWords:
                x = cleanup(tWords)
                if x in findingT:
                    findingT[x] += 1
                else:
                    findingT[x] = 1
while True:
    usernames = input('enter usernames Twitter: ')
    if usernames in findingT:
        print('Mentoned',findingT[usernames] ,' times')
    else:
        print('not Mentoned')
