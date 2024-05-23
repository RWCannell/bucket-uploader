# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2020 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import timedelta

from minio import Minio
from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()
 
# Access environment variables
minio_bucket_name = os.getenv("MINIO_BUCKET_NAME")
minio_api_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")

client = Minio(
    minio_api_endpoint,
    access_key=minio_access_key,
    secret_key=minio_secret_key,
    cert_check=False,
)

file_path = "./hogwarts_express.jpg"

# # Get presigned URL string to delete 'my-object' in
# # 'my-bucket' with one day expiry.
# url = client.get_presigned_url(
#     "DELETE",
#     minio_bucket_name,
#     file_path,
#     expires=timedelta(days=1),
# )
# print(url)

# Get presigned URL string to upload 'my-object' in
# 'my-bucket' with response-content-type as application/json
# and one day expiry.
url = client.get_presigned_url(
    "PUT",
    minio_bucket_name,
    file_path,
    expires=timedelta(days=1),
    response_headers={"response-content-type": "application/json"},
)
print(url)

# # Get presigned URL string to download 'my-object' in
# # 'my-bucket' with two hours expiry.
# url = client.get_presigned_url(
#     "GET",
#     minio_bucket_name,
#     file_path,
#     expires=timedelta(hours=2),
# )
# print(url)