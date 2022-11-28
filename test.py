x = 12
y = 12.2

if isinstance(y, (int, float)):
    print('is int or float')
elif isinstance(y, (int)):
    print('is int')
elif isinstance(y, float):
    print('is float')