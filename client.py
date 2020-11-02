#Qchat client-side.

import os
from Qchat import Qchat

def main():
    os.system('clear')

    chat = Qchat(
        access_key='access_key',
        secret_key='secret_key',
        end_point='end_point_url')
    
    if not chat.check_client_files('my_bucket', 'client.txt'):
        with open('client.txt', 'w+') as creator:
            creator.write('default message') 

        chat.submit_message(bucket='my_bucket', file='client.txt', file_name='client.txt')

    while 1:
        client_input = input('Client> ')

        with open('client.txt', 'w+') as client_file:
            client_file.write(client_input)

        chat.submit_message(bucket='my_bucket', file='client.txt', file_name='client.txt')


if __name__ == "__main__":
    main()