import re


message = ''
s = "aaRM@qqwe"
x = True
while x:
    if len(s) < 8:
        message = 'At least 8 digit'
        break
    elif re.findall("^1|0|2|3|4|5|6|7|8|9", s):
        message = "First digit can't be number"
        break
    elif not re.search('[A-Z]', s):
        message = 'At least one Uppercase'
        break
    elif not re.search('[a-z]', s):
        message = 'At least one lawer case'
        break
    elif not re.search('[@#$_]', s):
        message = 'Mist contain at least one sc'
        break

    else:
        message = 'Valid password'
        x = False
        break
if x:
    print('password not valid')
print(message)
