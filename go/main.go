package main

import (
	"bytes"
	"fmt"
	"io"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
)

var uploadFolder = "uploads"
var downloadFolder = "downloads"
var uploadFileName = "If_by_Rudyard_Kipling.pdf"
var downloadFileName = "Ozymandias_of_Egypt_by_Percy_Shelley.pdf"
var bucketName = "regan-test-bucket"
var region = "us-east-1"

func uploadFile() error {
	awsSession := session.Must(session.NewSession())

	uploader := s3manager.NewUploader(awsSession)

	// get path of current folder
	currentFolder, err := os.Getwd()
	if err != nil {
		return err
	}

	// concatenating the complete file path and filename
	uploadFile, err := os.Open(currentFolder + "/" + uploadFolder + "/" + uploadFileName)
	if err != nil {
		return err
	}

	// upload the file
	_, err = uploader.Upload(&s3manager.UploadInput{
		Bucket: aws.String(bucketName),
		Key:    aws.String(uploadFileName),
		Body:   uploadFile,
	})
	if err != nil {
		return err
	}

	return nil
}

func downloadFile() error {
	awsSession := session.Must(session.NewSession())
	downloader := s3manager.NewDownloader(awsSession)

	// create file that will where the data will be stored
	downloadFile, err := os.Create(downloadFileName)
	if err != nil {
		return err
	}

	// download the file
	_, err = downloader.Download(downloadFile, &s3.GetObjectInput{
		Bucket: &bucketName,
		Key:    &downloadFileName,
	})
	if err != nil {
		return err
	}

	return nil
}

func main() {
	region := "us-east-1"

	sess, err := session.NewSession(&aws.Config{
		Region: aws.String(region),
	})
	if err != nil {
		fmt.Println("Error creating session:", err)
		return
	}
	svc := s3.New(sess)

	bucketName := "regan-test-bucket"
	filePath := "public/assets/uploads/If_by_Rudyard_Kipling.pdf"

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error opening file:", err)
		return
	}
	defer file.Close()

	uploadFileName := "If_by_Rudyard_Kipling.pdf"

	// Read the contents of the file into a buffer
	var buf bytes.Buffer
	if _, err := io.Copy(&buf, file); err != nil {
		fmt.Fprintln(os.Stderr, "Error reading file:", err)
		return
	}

	// This uploads the contents of the buffer to S3
	_, err = svc.PutObject(&s3.PutObjectInput{
		Bucket: aws.String(bucketName),
		Key:    aws.String(uploadFileName),
		Body:   bytes.NewReader(buf.Bytes()),
	})
	if err != nil {
		fmt.Println("Error uploading file:", err)
		return
	}

	fmt.Println("File uploaded successfully!")
}
