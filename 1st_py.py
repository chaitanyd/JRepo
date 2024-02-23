def eggs(l1):
    for i in range(len(l1)):
        print(l1[i] + ', ', end="")
        if l1[i] == l1[-2]:
            print('and ' + l1[-1], end="")
            break


spam = ['apples', 'bananas', 'tofu', 'cats']
eggs(spam)
