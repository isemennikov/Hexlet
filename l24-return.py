def greeting() -> object:
    print('Я появлюсь в консоли')
    return 'Hello, Hexlet!'


# И напечатает текст на экран и вернет значение
message = greeting()


# LABS
# Task:  Implement a say_hurray_three_times() function that returns a string
def say_hurray_three_times():
    message = 'hurray! hurray! hurray!'
    return message


result = say_hurray_three_times()

print(result)

# correct version
def say_hurray_three_times():
    word = 'hurray!'
    return f'{word} {word} {word}'
result = say_hurray_three_times()

print(result)
