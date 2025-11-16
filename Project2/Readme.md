# Project 2 - AWS Two-Tier Infrastructure Build


## Instruction received from ChatGPT

This project builds a basic two-tier architecture, which is the foundation of most cloud applications:
- Tier 1 — Web Server - Runs on EC2 (your frontend or backend service).
- Tier 2 — Database - Runs on Amazon RDS (PostgreSQL or MySQL).

Cnnect the EC2 instance → to the RDS database → inside a properly designed VPC.

This is the most important beginner–intermediate cloud project because it teaches:
- VPC
- Public vs private subnets
- Security Groups
- Routing tables
- Internet Gateways
- NAT Gateways
- EC2 configuration
- RDS access control
- Basic automation (optional with Terraform)

It’s the closest beginner-friendly project to what companies actually deploy.

### ✔️ Why This Project Matters

Project 2 teaches you real infrastructure design, including:
- private networks
- secure DB access
- port management
- AMIs, key pairs
- SSH
- connecting apps to databases
- troubleshooting connectivity

When you apply to cloud roles, interviewers always check if you can build a basic two-tier setup. This project absolutely deserves its own page/repo folder.

### Details
Static = No backend logic, just files (example: your S3 static website)

Dynamic = Application processes requests, interacts with a database (example: a Flask/Node.js app reading/writing data)

Your Two-Tier Project sits in the middle:

✔ Dynamic in terms of architecture
- EC2 is running a server
- RDS is storing data
- There’s backend communication
- There's networking, security groups, database connections

✖ Not dynamic in terms of user-facing interactions (unless you add an app)

If you install only a placeholder page, it’s not truly dynamic

If you build a small backend app that reads/writes from the DB → yes, fully dynamic