text = 'Ha ha ha, I just finished one part of Python classes. \n'\
        'Need to be continue. \n'

with open('text2.txt', 'w') as f:
    f.write(text)

with open('text2.txt', 'r') as f:
    print(f.read())

