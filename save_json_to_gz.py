from pprint import pprint
import json
import gzip
import requests
from awss import upload_file, create_client


def encode_json(json_object):
    return json.dumps(json_object, indent=4, ensure_ascii=True).encode("utf-8")


def decode_json(binary_object):
    return json.loads(binary_object)


def compress_data(data):
    return gzip.compress(data, compresslevel=9)


def save_compress_data(data, file_name):
    with open(file_name, mode="wb") as f:
        f.write(data)


def open_compress_data_file(file_name):
    with gzip.open(file_name, "rb") as f_in:
        data = f_in.read()
    return data


def save_json_gz(date, json, client):
    file_name = f"{date}.json.gz"
    print(file_name)
    json = encode_json(json)
    json = compress_data(json)
    save_compress_data(json, file_name)
    upload_file(client, file_name, "storage-web-files")


# data = encode_json(data)
# data = compress_data(data)
# save_compress_data(data, "file_name")  # cambiar
# data = open_compress_data_file("file_name")  # cambiar
# data = decode_json(data)
# print(data)
