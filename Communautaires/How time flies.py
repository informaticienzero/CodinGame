from datetime import date, datetime, timedelta

d1 = datetime.strptime(input(), '%d.%m.%Y')
d2 = datetime.strptime(input(), '%d.%m.%Y')

days = (d2 - d1).days
diff = date(1, 1, 1) + (d2 - d1)

y = diff.year - 1
m = diff.month - 1

result = ''

if y != 0:
    result += f'{y} year' 
    if y == 1:
        result += ', '
    else:
        result += 's, '
        
if m != 0:
    result += f'{m} month'
    if m == 1:
        result += ', '
    else:
        result += 's, '
        
result += f'total {days} days'
print(result)
