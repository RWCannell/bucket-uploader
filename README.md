## Introduction
This repository contains coding examples of uploading files/objects to Amazon S3 buckets or MinIO buckets.

### Go
There exists an example using the `github.com/aws/aws-sdk-go/service/s3` package.

### Python
It is better to run our Python scripts inside a virtual environment. To start up a virtual environment, we run the following command:
```bash
python3 -m venv myenv
```
Then to activate the virtual environment (with Mac or Linux), we run
```bash
source venv/bin/activate
```
For a Windows environment, we run
```bash
# in cmd.exe
venv\Scripts\activate.bat

# in PowerShell
venv\Scripts\Activate.ps1
```
To install the dependencies for `get_presigned_url.py`, use `pip`:
```bash
pip3 install minio
pip install python-dotenv
```
To deactivate the virtual environment and to delete it, run
```bash
deactivate

rm -r myenv
```
After running the `get_presigned_url.py`, the output that gets printed is an example of what a MinIO pre-signed url looks like:
```bash
https://146.141.240.75:9000/regan-test-bucket/./hogwarts_express.jpg?response-content-type=application%2Fjson&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio_access_key%2F20240523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240523T180425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c944bf10d6c445a5166f0997288cec097899d43244158d2cb97a00e7d2a0f15
```
or
```bash
https://cloud05.core.wits.ac.za/regan-test-bucket/./hogwarts_express.jpg?response-content-type=application%2Fjson&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minioAccessKey%211%2F20240611%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240611T104506Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=db03e5378dc2d3d96f0307926dfff56b727f42edcfb9edf25785571e99942c5b
```