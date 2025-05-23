
variable "credentials" {
    description = "My Credentials"
    default = "C:/Projects/nyc_taxi/terraform/keys/fleet-point-453222-s4-1d1f18171a37.json"
}

variable "project" {
    description = "Project ID"
    default = "fleet-point-453222-s4"
}

variable "region" {
    description = "Region"
    default = "us-central1"
}

variable "location" {
    description = "Project Location"
    default = "US"
}

variable "bq_dataset_name" {
    description = "My BigQuery Dataset Name"
    default = "demo_dataset"
}

variable "gcs_bucket_name" {
    description = "My Storage Bucket Name"
    default = "demo-bucket-fleet-point-453222-s4"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}