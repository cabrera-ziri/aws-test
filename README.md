# aws-test


1. Set up an AWS account:

Go to aws.amazon.com and sign up for a free account.


2. Launch an EC2 instance:

- Log in to the AWS Management Console.
- Navigate to EC2 service.
- Click "Launch Instance".
- Choose an Amazon Machine Image (AMI) - e.g., Amazon Linux 2.
- Select an instance type (t2.micro is free tier eligible).
- Configure instance details, add storage, and configure security group.
- Create or select an existing key pair for SSH access.


3. Connect to your instance:

Use SSH to connect:
ssh -i /path/to/your-key.pem ec2-user@your-instance-public-ip


4. Set up your environment:

Update the system: sudo yum update -y
Install necessary software: e.g., sudo yum install -y python3


5. Transfer your code:

Use SCP to copy files:
scp -i /path/to/your-key.pem /path/to/your-code.py ec2-user@your-instance-public-ip:~


6. Run your code:

Execute your script: python3 your-code.py


7. Monitor and manage:

Use AWS CloudWatch for monitoring.
Remember to stop or terminate your instance when not in use to avoid charges.
