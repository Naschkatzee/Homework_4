characters = ['hello', 'filthy', 'dogs']

def inspect (con: str) -> None:
    def the_wrapper_around_the_original_function():
        print (characters)
    con ()
    return the_wrapper_around_the_original_function

@inspect
def con():
    word = ' '.join(characters)
    print (word) 
