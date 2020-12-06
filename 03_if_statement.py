# What should I wear?

temp = int(input('Please enter temperature in Celsius: '))

if temp > 30:
    print('Wear shorts and sun cream!')
elif temp <=30 and temp > 20:
    print('It\'s warm but not shorts weather!')
elif temp <= 20 and temp >10:
    print('You\'ll probably need a vest today!')
else:
    print('Too cold! Don\'t go out!')