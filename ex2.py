def my_data(*args):
    return (input('Как вас зовут? '),
            input('Ваша Фамилия - '),
            input('Год рождения - '),
            input('Город проживания - '),
            input('Ваш email - '),
            input('Ваш телефон - '))


result = ' '.join(my_data())
print(result)
print(type(result))



