number = int(input('Введите время в секундах:'))
hours = number // 3600
hours_done = (hours) if hours > 10 else ('0' + str(hours))
minutes = (number % 3600) // 60
minutes_done = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (number % 3600) % 60
seconds_done = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Значение слишком большое')
else:
    print(f'{hours_done}:{minutes_done}:{seconds_done}')