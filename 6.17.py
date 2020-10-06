# David Gonzalez
# 1630338

user_password = input()

mod_password = ''

i = 0
while i < len(user_password):
    ch = user_password[i]
    if ch == 'i':
        mod_password += '!'
    elif ch == 'a':
        mod_password += '@'
    elif ch == 'm':
        mod_password += 'M'
    elif ch == 'B':
        mod_password += '8'
    elif ch == 'o':
        mod_password += '.'
    else:
        mod_password += ch
    i += 1
mod_password += 'q*s'
print(mod_password)


