def logger(data):
    with open('log.csv', 'a') as file:
        file.write(f'\n{data}')
