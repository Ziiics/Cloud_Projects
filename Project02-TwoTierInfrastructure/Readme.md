***In Progress***

# Project 2 - AWS Two-Tier Infrastructure Build

### Overview
This project creates a real two-tier cloud architecture with a Web Tier (EC2 - Tier 1) in public subnets and a Database Tier (RDS - Tier 2) in private subnets inside a properly designed VPC. It mirrors what companies deploy in production and teached cloud networking, routing, database security, and infrasturcture design.

### Tools
| Category | AWS Service/Tool | Purpose |
| --- | --- | --- |
| Compute | EC2 | Runs web server in public subnets |
| Database | RDS (MySQL) | Stores apps data in private subnet |
| Network | VPC  | Isolate entire environment |
|  | Subnets | Separate internet-facing from internal ones |
|  | Internet Gateway (IGW) | Allows EC2 intances in public subnets to access internet |
|  | NAT Gateway | Asllows private subnet to∂ reach internet |
|  | Route Tables |  Controls traffic routing with VPC |
| Security | Secuirty Groups | Firewall rules for EC2 and RDS | 
|  | NACLs (optional) |  Additional subnet-level traffic filtering |
| Access & Management | IAM | Roles and permissions for EC2 and RDS 
| Monitoring | CloudWatch (optional) | Logs, metrics, alarms, dashboards |
| Automation (optional) | Terraform/CloudFormation | IaC verrsion of the build | 

### Notes
- I tend to name every container, subnets, vpc, everything as it make it less confusing
- EC2 Instance (Linux) as the web tier
- RDS Database (MySQL or PostgreSQL) as the DB tier
- Security Groups controlling all ports between the two tiers

### Steps
1. Making VPC to section the subnet. Ensure to name it because if you have couple different VPC, it can be confusing.
*<a href="Asset/Step1.png">(View Screenshot for Step 1)</a>*

2. Once its done, create subnet (the option is on the left bar on the VPC). Choose the correct VPC and created 4 subnet with at least two different region. Choosing all four different region will not allow the database to be made.
*<a href="Asset/Step2.png">(View Screenshot for Step 2)</a>*

3. Create 2 route table, public and private.
*<a href="Asset/Step3.png">(View Screenshot for Step 3)</a>*

4. Create security groups that ia also located in VPC. Securiy group is like the friewall. Make one for EC2 and one for the RDS.
*<a href="Asset/Step4.png">(View Screenshot for Step 4)</a>*

5. Go to EC2, then make key pairs and then create an instance. The key pairs will be used for the instance to ensure secure access. When making the insatnce, ensure to choose the right VPC to be able to choose the seucirty group.
*<a href="Asset/Step5.png">(View Screenshot for Step 5)</a>*

6. Made a database with the project2_vpc that is made. Ensure to click on the *Additional Configuration* to choose name for the database. Not making a name will not create the database. It will be located around the bottom part and will be minimize. 
*<a href="Asset/Step6.png">(View Screenshot for Step 6)</a>*

7. Create IAM user as admin and ensure that they have full SSM and RDS access
*<a href="Asset/Step7.png">(View Screenshot for Step 7)</a>*

8. Utilize SSM System Manager and securely store password. I used SecureString for this.
*<a href="Asset/Step8.png">(View Screenshot for Step 8)</a>*

9. 



### 🔐 Security Design 
- EC2 Security Group
  - Inbound: HTTP/HTTPS (optional), SSH from your IP
  - Outbound: Allow to the DB Security Group
- RDS Security Group
  - Inbound: ONLY from EC2's SG, on port 3306 (MySQL) or 5432 (Postgres)
  - No public access, no direct internet


### 🧪 What You Will Test
- [ ] SSH into EC2 (public subnet)
- [ ] From EC2, connect to your database using:
mysql -h <RDS-endpoint> -u admin -p
- [ ] Test web server returns your HTML/app
- [ ] Confirm RDS cannot be reached from the internet
- [ ] Confirm traffic only flows the right way

### 📊 Optional Add-Ons (For “Wow” factor)
- Load Balancer (ALB)
- Auto Scaling Group
- Bastion Host (for private access)
- Terraform version of the entire build
- CloudWatch dashboards

