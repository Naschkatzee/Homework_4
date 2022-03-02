def concat (*kwargs):
    word = ' '.join(characters)
    return word 
characters = ['hello', 'filthy', 'dogs']
print (concat(characters))


def concat (*kwargs, reversed = True):
    word = ' '.join(characters)
    return word 
    
characters = ['hello', 'filthy', 'dogs']
print(concat(characters.reverse()))