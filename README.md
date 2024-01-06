# Pinterest-Data-Pipeline

## Table of Contents
1. [Description](#description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)

## Description <a name="description"></a>
This project aims to set up a development environment mimicking the infrastructure of a Pinterest-like system using AWS services and integrating with Kafka. The primary goal is to familiarize users with AWS setup, EC2 instances, and working with MSK clusters for Kafka.

### Project Overview
- **GitHub Repository Setup:** Guides users through creating a new repository to track code changes on GitHub.
- **AWS Account Setup:** Instructions for creating an AWS account, accessing an EC2 instance, and configuring IAM roles for MSK cluster authentication.
- **Kafka Client Configuration:** Details on installing Kafka and setting up IAM authentication to communicate with the MSK cluster.

## Installation Instructions <a name="installation-instructions"></a>
### Step-by-Step Setup Guide
#### Step 1: GitHub Repository Setup
1. Click the button on the right to create a new GitHub repository.

#### Step 2: AWS Account and EC2 Instance Setup
1. Go to [AWS Console](https://aws.amazon.com/) and sign in using the provided credentials.
2. Change the password as prompted and note your UserId.

#### Step 3: Key Pair Configuration for EC2 Instance
1. Access Parameter Store in your AWS account and retrieve the specific key pair associated with your EC2 instance.
2. Save the key pair content in a `.pem` file.

#### Step 4: Connecting to EC2 Instance
1. Follow the instructions in the EC2 console under "Connect" (SSH client) to connect to your EC2 instance.

#### Step 5: Configuring Kafka Client for MSK Cluster
1. Install Kafka (version 2.12-2.8.1) and the IAM MSK authentication package on your client EC2 machine.
2. Access IAM console, edit the trust policy, and configure `client.properties` for AWS IAM authentication.

#### Step 6: Creating Kafka Topics on MSK Cluster
1. Retrieve Bootstrap servers and Zookeeper connection strings from the MSK Management Console.
2. Create three topics as specified for Pinterest-like data.

## Usage Instructions <a name="usage-instructions"></a>
### File Structure
- `kafka_folder/`
  - `bin/`
    - `client.properties`

   
## Setting up S3 Bucket and MSK Connect

### Step 7: S3 Bucket Configuration
1. Go to the S3 console and locate the bucket containing your UserId in the format: `user-<your_UserId>-bucket`.
2. Note the bucket name for use in subsequent steps.

### Step 8: Confluent.io Amazon S3 Connector Setup
1. On your EC2 client, download the Confluent.io Amazon S3 Connector.
2. Copy the downloaded connector to the previously identified S3 bucket.

### Step 9: Creating Custom Plugin and Connector in MSK Connect Console
1. Access the MSK Connect console.
2. Create a custom plugin with the name: `<your_UserId>-plugin`.
3. Create a connector with the name: `<your_UserId>-connector`.
4. Configure the connector using the following settings:
   - **Bucket Name:** `user-<your_UserId>-bucket`
   - **topics.regex Field:** `<your_UserId>.*`
   - **Access Permissions:** Choose the IAM role used for MSK cluster authentication (`<your_UserId>-ec2-access-role`).
5. Ensure that the connector is associated with the appropriate plugin.

### Step 10: Data Storage in S3 Bucket
By building the plugin-connector pair, any data passing through the IAM-authenticated MSK cluster will be automatically stored in the designated S3 bucket (`user-<your_UserId>-bucket`).


test



