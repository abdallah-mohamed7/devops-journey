output "server_public_ip"{
 description = "The public IP address of the hadith API server"
 value = aws_instance.hadith_server.public_ip

}



output "bucket_arn" {
 description = "The ARN of the S3 bucket"
 value = aws_s3_bucket.my_bucket.arn

}
