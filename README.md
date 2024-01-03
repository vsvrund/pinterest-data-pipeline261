# Pinterest-Data-Pipeline

## Table of Contents
1. [Description](#description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License](#license)

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

### License Information <a name="license"></a>
This project is licensed under the [insert your chosen license] License.

