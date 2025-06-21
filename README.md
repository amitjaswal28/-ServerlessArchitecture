# AWS Lambda & Boto3 Automation Assignments

This repository contains the solutions for 4 selected AWS Lambda automation tasks using Python and Boto3.

---

## ✅ Assignment 1: Automated EC2 Instance Management

### 📄 Objective:
Automatically start or stop EC2 instances based on specific tags using a Lambda function.

### 🛠 Setup Instructions:
1. **Create two EC2 instances** in AWS Console.
2. Tag one as:
   - Key: `Action` | Value: `Auto-Start`
   - Key: `Action` | Value: `Auto-Stop`
3. Create an IAM role with **`AmazonEC2FullAccess`**.
4. Create a Lambda function using Python 3.x and attach the role.
5. Paste the script from `assignment-1-ec2-management/lambda_function.py`.
6. Manually invoke the function.

### 📸 Screenshot:
- [ ] EC2 instance state before and after Lambda run.
- [ ] Lambda logs showing stopped/started instance IDs.

---

## ✅ Assignment 2: Automated S3 Bucket Cleanup

### 📄 Objective:
Delete files older than 30 days from a specified S3 bucket using Lambda.

### 🛠 Setup Instructions:
1. Create an S3 bucket and upload files (simulate older dates if needed).
2. Create an IAM role with **`AmazonS3FullAccess`**.
3. Create a Lambda function using Python 3.x.
4. Replace `'your-bucket-name'` in the script in `assignment-2-s3-cleanup/lambda_function.py`.
5. Manually trigger the function.

### 📸 Screenshot:
- [ ] Bucket file list before and after.
- [ ] Lambda logs showing deleted files.

---

## ✅ Assignment 3: Monitor Unencrypted S3 Buckets

### 📄 Objective:
Scan all S3 buckets and log names of those without server-side encryption.

### 🛠 Setup Instructions:
1. Create a few S3 buckets (some with encryption, some without).
2. Create an IAM role with **`AmazonS3ReadOnlyAccess`**.
3. Create a Lambda function using Python 3.x.
4. Use script from `assignment-3-unencrypted-buckets/lambda_function.py`.
5. Invoke the function manually.

### 📸 Screenshot:
- [ ] Lambda logs showing unencrypted buckets.

---

## ✅ Assignment 6: Monitor and Alert High AWS Billing

### 📄 Objective:
Monitor AWS estimated billing daily and send an SNS alert if it exceeds $50.

### 🛠 Setup Instructions:
1. Create an SNS topic and subscribe your email.
2. Create IAM role with permissions:
   - `cloudwatch:GetMetricStatistics`
   - `sns:Publish`
3. Create a Lambda function using Python 3.x.
4. Replace SNS topic ARN in `assignment-6-billing-alert/lambda_function.py`.
5. Invoke manually or schedule with CloudWatch.

### 📸 Screenshot:
- [ ] SNS email alert.
- [ ] Lambda logs showing current billing.

---

## 🧾 Notes
- Ensure all Lambda functions are deployed in regions where services/resources exist.
- Modify IAM roles for principle of least privilege in real-world scenarios.

---

## 📁 Folder Structure
```
├── assignment-1-ec2-management
│   └── lambda_function.py
├── assignment-2-s3-cleanup
│   └── lambda_function.py
├── assignment-3-unencrypted-buckets
│   └── lambda_function.py
├── assignment-6-billing-alert
│   └── lambda_function.py
└── README.md
```

---

## 🔗 Author
**Amit Jaswal**  
DevOps Batch 10 – AWS Automation Practice
