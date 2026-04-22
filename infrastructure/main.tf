terraform{
  required_providers {
   aws = {
    source = "hashicorp/aws"
    version = "~> 5.0"
  }
 }
}


provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "my_bucket"{
  bucket = var.bucket_name

  tags = {
   Name  = "My First terraform Bucket"
   Environment = "Dev"

 }
}
resource "aws_key_pair" "deployer" {
  key_name   = "hadith-deployer-key"
  public_key = file("~/.ssh/hadith_key.pub")
}

resource "aws_instance" "hadith_server" {
  ami                    = "ami-032bb177cf15a4813"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.hadith_sg.id]
  key_name               = aws_key_pair.deployer.key_name # Add this line
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo usermod -aG docker ubuntu
              
              sleep 10
              
              sudo docker run -d --name hadith-app -p 8082:8082 -e APP_MESSAGE="Hello from Automated EC2" abdallahmohamed7/hadith-api:latest

              EOF
  tags = {
    Name = "Hadith-API-Server"
  }
}




resource "aws_security_group" "hadith_sg" {
 name = "hadith-api-sg"
 description = "Allow shh and API traffic"

ingress {
 from_port = 22
 to_port =22
 protocol = "tcp"
 cidr_blocks =["0.0.0.0/0"]
}

ingress {
    from_port   = 8082
    to_port     = 8082
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}


