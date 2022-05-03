import boto3
import boto3.session
import threading


def create_client(service):
    client = boto3.resource(service)
    return client


def upload_file(s3, file_name, bucket_name):
    s3.Bucket(bucket_name).upload_file(file_name, file_name)


# Montar Jsons en S3
# s3 = create_client("s3")
# upload_file(s3, "", "storage-web-files")
