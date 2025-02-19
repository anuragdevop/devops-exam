provider "aws" {
  region = "ap-south-1" 
}

terraform {
  backend "s3" {
    bucket = "467.devops.candidate.exam"
    key    = "Anurag.Dangi"
    region = "ap-south-1"
  }
}

