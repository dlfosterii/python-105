def repeat(num, bark):
    while num >=0:
        print(bark)
        num -= 1



#goal output is: woofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoof
a_dog_says = repeat(3, repeat(5, 'woof'))



def repeat(how_many_times, the_string):
    result = ''
    while how_many_times > 0:
        #do something
        print(the_string)
        result += the_string
        how_many_times -= 1
    return result

num = 5
a_dog_says = repeat(5, 'woof')
another_dog_says = repeat(3, a_dog_says)