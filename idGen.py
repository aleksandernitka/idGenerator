import string
import random
import datetime

# Code used to fully anon participants:
# Outputs a 6-symbol random id

def id_generator(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

thisId = id_generator()
time = datetime.datetime.now()

print(time, thisId)

id = open('idKeys.txt', 'a')
id.write('{} {}\n'.format(time, thisId))
id.close()