#Qchat server-side.

import os
from Qchat import Qchat

def main():
    os.system('clear')

    chat = Qchat(
        access_key='access_key',
        secret_key='secret_key',
        end_point='end_point_url')

    if not chat.check_server_files('my_bucket', 'server.txt'):
        with open('server.txt', 'w+') as creator: 
            creator.write('default message')

        chat.submit_message(bucket='my_bucket', file='server.txt', file_name='server.txt')

    while 1:
        server_input = input('Server> ')

        with open('server.txt', 'w+') as server_file:
            server_file.write(server_input)

        chat.submit_message(bucket='my_bucket', file='server.txt', file_name='server.txt')


if __name__ == "__main__":
    main()