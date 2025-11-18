***In Progress***

# Project 2 - AWS Two-Tier Infrastructure Build

## Instruction received from ChatGPT

### This project builds a basic two-tier architecture, which is the foundation of most cloud applications:
- Tier 1 — Web Server (EC2 in Public Subnets)
  - A web server runs in public subnets so users on the internet can reach it.
  - It connects outward to the database tier but the database cannot connect back.
- Tier 2 — Database Tier (RDS in Private Subnets)
  - A managed database runs inside private subnets with no internet access.
  - Only the web server is allowed to talk to it through Security Groups.

Cnnect the EC2 instance → to the RDS database → inside a properly designed VPC.

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
- [] SSH into EC2 (public subnet)
- [] From EC2, connect to your database using:
mysql -h <RDS-endpoint> -u admin -p
- [] Test web server returns your HTML/app
- [] Confirm RDS cannot be reached from the internet
- [] Confirm traffic only flows the right way

### 📊 Optional Add-Ons (For “Wow” factor)
- Load Balancer (ALB)
- Auto Scaling Group
- Bastion Host (for private access)
- Terraform version of the entire build
- CloudWatch dashboardss