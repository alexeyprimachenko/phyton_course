# Напишите программу которая выполнит следующее:



# Попросить ввести свой возраст (можно исползовать константу или input()).

# - если пользователю меньше 7 - вывести “Где твои мама и папа?”

# - если пользователю меньше 18 - вывести “Мы не продаем сигареты несовершеннолетним!”

# - если пользователю больше 65 - вывести “Пенсионерам сегодня скидка!”

# - если у пользователя юбилей (10, 20, 40 и тд лет, любое число, кратное 10) - вывести “Где Ваш сертификат о вакцинации?”

# - в любом другом случае - вывести “Оденьте маску! ”

age = int(input('Сколько тебе лет? '))

if age < 7:
     print('Где твои мама и папа?')
elif age < 18 and age % 10:
     print('Мы не продаем сигареты несовершеннолетним!')
elif age > 65 and age % 10:
     print('Пенсионерам сегодня скидка!')
elif age % 10 == 0:
        print('Где Ваш сертификат о вакцинации?')
else:
     print('Оденьте маску!')