from time import asctime


def get_date_time():
    return asctime()


print('Today:')
print(get_date_time())
