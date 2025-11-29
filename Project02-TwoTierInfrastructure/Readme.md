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

4. Create security groups that ia also located in VPC. Securiy group is like the friewall. Make one for EC2 and one for the RDS. I choose Ubuntu as it is the most in demand.
*<a href="Asset/Step4.png">(View Screenshot for Step 4)</a>*

5. Go to EC2, then make key pairs and then create an instance. The key pairs will be used for the instance to ensure secure access. When making the insatnce, ensure to choose the right VPC to be able to choose the seucirty group.
*<a href="Asset/Step5.png">(View Screenshot for Step 5)</a>*

6. Go to RDS and create a subnet group that consist only of the private subnet.
*<a href="Asset/Step6.png">(View Screenshot for Step 6)</a>*

7. Made a database with the project2_vpc that is made. For the subnet group, choose the previously made in the previous step. Ensure to click on the *Additional Configuration* to choose name for the database. Not making a name will not create the database. It will be located around the bottom part and will be minimize. 
*<a href="Asset/Step7.png">(View Screenshot for Step 7)</a>*

8. Create IAM user as admin and ensure that they have full SSM and RDS access
*<a href="Asset/Step8.png">(View Screenshot for Step 8)</a>*

9. Utilize SSM System Manager and securely store password. I used SecureString for this.
*<a href="Asset/Step9.png">(View Screenshot for Step 9)</a>*

10. Connect to EC2. For this project, i am using SSH Client. The steps can be found by clicking **Connect** on the selected instance.
*<a href="Asset/Step10.png">(View Screenshot for Step 10)</a>*

11. Run these command on the SSH client
```
sudo apt-get update      #update the instance
sudo apt-get install mysql-server     #install MySql to support database
sudo apt-get install nginx    #used as reverse proxy, load balancer, mail proxy, and HTTP cache
sudo apt-get install docker.io    #Platform as a service (PaaS) that use virtualization to deliver software as container

  # host = RDS endpoint (to find, go to database -> connectivity & secuirty)
  # user = Master username (to find, database -> Configuration)
mysql -h host -u user -p       #to access mysql command platform to create database
```

12. Create database in MySql. I am creating a database where people who visit can write the purpose of their visit.
```
CREATE DATABASE mysql_database_name   # mysql_database_name can be change according to preference
USE mysql_database_name     # choose the database we will be creating the table in

#create the table inside the database. Mine is about purpose of their visit
CREATE TABLE table_name (
  Name VARCHAR(50);
  Purpose VARCHAR(255);
)
```

13. To check if the table exist. **Ensure to always add ';' at the end**ß
```
SHOW DATABASES            # show different database
USE mysql_database_name;  # a must, describe which database we are looking at
SHOW TABLE table_name;    # only show the table
DESCRIBE table_name;      # show what is inside the table. like the type, etc
```

14. Add your database. I built MySQL database using Python. Utilize boto3 to get the SecureString password from Parameter store, and using Flask as microservice to get obejct from the database.
  *Add my code here once it is done*

15. Create S3 bucket. The permission is Block public access, and everything else is as default
*<a href="Asset/Step15.png">(View Screenshot for Step 15)</a>*

16. To be safe, I want to do some testing before continuing to the next step
    - Checking EC2 -> RDS connection
      ``` python
      mysql -h <RDS_ENDPOINT> -u <MASTER_USER> -p
      show databases;
      USE mysql_database_name;
      SHOW TABLES;
      INSERT INTO table_name (name, purpose) VALUES ('Test', 'Testing connection')
      SELECT * FROM table_name
      ```
    - Test if Backend (Flask) can talk to RDS 
      1. Copy code to EC2 using ssh client.
          On EC2 SSH client,
            ```bash
            scp -i <pem_location_path> <local_file_to_app.py> ubuntu@<ip>:<remote_path>
            ```

      


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

