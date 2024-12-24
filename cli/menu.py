import config

def menu():

    print(f'=== Welcome to {config.APP_NAME} terminal software ===\nVERSION:{config.VERSION}\n \n')
    print(f'=== CHOOSE AN OPTION ===\n')
    print(f'Encode (text to morse) - Press 1')
    print(f'Decode (morse to text) - Press 2')
    print(f'Exit - Press anyother')
    response = str(input(': '))
    return response
