#Qchat chat-screen.

import os
from Qchat import Qchat

def main():
    os.system('clear')

    chat = Qchat(
        access_key='access_key',
        secret_key='secret_key',
        end_point='end_point_url')

    pre_client = ''
    pre_server = ''

    while 1:
        new_server = chat.read_message(bucket='my_bucket', file_name='server.txt')

        if pre_server != new_server and new_server != 'default message': 
            print(f'\033[91mServer: {new_server}')


        new_client = chat.read_message(bucket='my_bucket', file_name='client.txt')

        if pre_client != new_client and new_client != 'default message':
            print(f'\033[93mClient: {new_client}')
        
        
        pre_client, pre_server = new_client, new_server


if __name__ == "__main__":
    main()