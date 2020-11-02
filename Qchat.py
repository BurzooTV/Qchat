#Qchat moudle.

import boto3

class Qchat():
    def __init__(self, access_key, secret_key, end_point):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__end_point = end_point
        self.__session = boto3.session.Session()
        self.__s3 = self.__session.client(
            service_name='s3',
            aws_access_key_id=self.__access_key,
            aws_secret_access_key=self.__secret_key,
            endpoint_url=self.__end_point)


    def submit_message(self, bucket, file, file_name):
        try:
            self.__s3.upload_file(file, bucket, file_name, 
                                       ExtraArgs={'ACL': 'public-read'})
        except:
            raise Exception("Something's wrongs! check bucket or file's path.")


    def read_message(self, bucket, file_name):
        try:
            file = self.__s3.get_object(Bucket=bucket, Key=file_name)
        except:
            raise Exception("Something's wrong! check bucket or key's name.")
        else:
            return file['Body'].read().decode('ascii')


    def check_server_files(self, bucket, server_file):
        try:
            buckets = self.__s3.list_objects_v2(Bucket=bucket)
        except:
            raise Exception("Something's wrong! this bucket does not exist.")
        else:
            if 'Contents' in buckets.keys():
                server = [obj['Key'] for obj in buckets['Contents']]
                return True if server_file in server else False
            else:
                return False    


    def check_client_files(self, bucket, client_file):
        try:
            buckets = self.__s3.list_objects_v2(Bucket=bucket)
        except:
            raise Exception("Something's wrong! this bucket does not exist.")
        else:
            if 'Contents' in buckets.keys():
                client = [obj['Key'] for obj in buckets['Contents']]
                return True if client_file in client else False
            else:
                return False
