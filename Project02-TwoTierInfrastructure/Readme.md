***In Progress***

# Project 2 - AWS Two-Tier Infrastructure Build

### Overview
This project creates a real two-tier cloud architecture with a Web Tier (EC2) in public subnets and a Database Tier (RDS) in private subnets inside a properly designed VPC. It mirrors what companies deploy in production and teached cloud networking, routing, database security, and infrasturcture design.

### Tools
| Category | AWS Service/Tool | Purpose |
| --- | --- | --- |
| Compute | EC2 | Runs web server in public subnets |
| Database | RDS (MySQL) | Stores apps data in private subnet |
| Network | VPC  | Isolate entire environment |
|  | Subnets | Separate internet-facing from internal ones |
|  | Internet Gateway (IGW) | Allows EC2 intances in public subnets to access internet |
|  | NAT Gateway | Asllows private subnet to reach internet |
|  | Route Tables |  Controls traffic routing with VPC |
| Security | Secuirty Groups | Firewall rules for EC2 and RDS | 
|  | NACLs (optional) |  Additional subnet-level traffic filtering |
| Access & Management | IAM | Roles and permissions for EC2 and RDS 
| Monitoring | CloudWatch (optional) | Logs, metrics, alarms, dashboards |
| Automation (optional) | Terraform/CloudFormation | IaC verrsion of the build | 

### Details
- Tier 1 — Web Server (EC2 in Public Subnets)
- Tier 2 — Database Tier (RDS in Private Subnets)

---
---
---

### This is the most important beginner–intermediate cloud project because it teaches:
1. 1 VPC
2. Public Subnets (2 AZs) → Web server runs here
3. Private Subnets (2 AZs) → Database runs here
4. Internet Gateway → For public access to EC2
5. NAT Gateway → For RDS-related systems (if any) to reach internet for updates
6. Route Tables for public vs private traffic flow
7. EC2 Instance (Linux) as the web tier
8. RDS Database (MySQL or PostgreSQL) as the DB tier
9. Security Groups controlling all ports between the two tiers

### 🔐 Security Design (Very Important)
- EC2 Security Group
  - Inbound: HTTP/HTTPS (optional), SSH from your IP
  - Outbound: Allow to the DB Security Group
- RDS Security Group
  - Inbound: ONLY from EC2's SG, on port 3306 (MySQL) or 5432 (Postgres)
  - No public access, no direct internet


### 🧩 What You Will Learn
Networking concepts
- Subnet placement
- Routing
- Difference between IGW and NAT
- Why private subnets exist
- Why you never expose a database publicly

Compute concepts
- AMIs
- Key pairs
- SSH access
- Installing a web server

Database concepts
- RDS parameter groups
- DB endpoints
- Security boundaries
- Connecting EC2 → RDS using environment variables

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

### Steps done
1. Making VPC to section the subnet. Ensure to name it because if you have couple different VPC, it can be confusing.
2. Once its done, create subnet (the option is on the left bar on the VPC). Choose the correct VPC and created 4 subnet with at least two different region. Choosing all four different region will not allow the database to be made.
3. Made a database with the porject2_vpc that is made. Ensure to click on the *Additional Configuration* to choose name for the database. Not making a name will not create the database. It will be located around the bottom part and will be minimize. 
