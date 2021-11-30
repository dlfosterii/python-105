#write a function that prints out "good morning" three times

def start(times, phrase):
    while times >= 0:
        print(phrase)
        times -= 1

start(3, 'good morning')