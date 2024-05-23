## Introduction
This repository contains coding examples of uploading files/objects to Amazon S3 buckets or MinIO buckets.

### Go
There exists an example using the `github.com/aws/aws-sdk-go/service/s3` package.

### Python
This is an example of what a pre-signed url looks like:
```bash
https://146.141.240.75:9000/regan-test-bucket/./hogwarts_express.jpg?response-content-type=application%2Fjson&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio_access_key%2F20240523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240523T180425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c944bf10d6c445a5166f0997288cec097899d43244158d2cb97a00e7d2a0f15
```