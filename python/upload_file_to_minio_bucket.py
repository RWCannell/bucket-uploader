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

source_file = "./hogwarts_express.jpg"
destination_file = "hogwarts_express.jpg"
    
# Make the bucket if it doesn't exist.
found = client.bucket_exists(minio_bucket_name)
if not found:
    client.make_bucket(minio_bucket_name)
    print("Created bucket", minio_bucket_name)
else:
    print("Bucket", minio_bucket_name, "already exists")

# Upload the file, renaming it in the process
client.fput_object(
    minio_bucket_name, destination_file, source_file,
)
print(
    source_file, "successfully uploaded as object",
    destination_file, "to bucket", minio_bucket_name,
)