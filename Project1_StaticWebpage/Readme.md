# Project 1 - Static Website Deployment on AWS

🔗 <a href="http://project1-static-webpage.s3-website.us-east-2.amazonaws.com/">Live Demo</a>

<p>S3 Website Endpoint:<br/><a href="http://project1-static-webpage.s3-website.us-east-2.amazonaws.com">http://project1-static-webpage.s3-website.us-east-2.amazonaws.com</a></p>

### Overview
This Projectis my first cloud deployment. I used simple static HTML page and hosted it using Amazon S3, added CloudFront for better performance, and then transfer my domain through Route53, and use ACM to make it able to accept HTTPS traffic. The goal is to understand how AWS handles storage, CDN distribution, DNS, and certificates.

### Tools
| Services | The Use |
|---| --- |
| S3 | Buckets to store and host static website files. |
| CloudWatch | The CDN, speed up delivery and serve cached versions across different region. |
| Route53 | Connect custom domain to CloudFront distribution. Example: *google.com* or *www.linkedin.com*.
| ACM | Generate SSL/TLS certitication for HTTPS traffic. |

### Process
1. I build a simple static HTML page.
2. Created S3 bucket, disabled "Block all public access", and turned on static website hosting.
3. Added JSON bucket policy -*can be based on user permission, HTTPS or HTTP, global keys or enterprise keys, which part of the bucket is allowed, requiring MFA or not*- to control how the site can be accessed.
4. Upload files to the bucket and tested the S3 website endpoint to ensure the corerct filei is accessible.
5. Set up CloudFront -*Free up to 1TB if using Free Tier*-, chose my S3 website endpoint as the origin. Website-endpoint is recommend this time because it is a static webpage.
6. Waited for the CloudFront distribution to finish deploying, then tested the CloudFront URL.
7. Started the Route 53 setup to connect my own domain (I transferred the domain I already owned).
8. After transferring, follow the procedure and you should be getting auth code. It then take up to 10 days for your current domain name registrar to process the request.
9. At this moment of waiting, I used AWS Certificate Manager to request a public certificate for HTTPS. Choose the domain and wwiat for the process.

### Current To-Do
- [ ] Wait for Route 53 DNS transfer to finish
- [ ] Confirm that the CloudFront URL works with HTTPS
- [ ] Update my A-record to point to the distribution


### Notes
- CloudFront caches old files — if I update my HTML, I need to invalidate the cache.
- The S3 “website endpoint” is good for testing before adding CloudFront.
- Route 53 is not free, even if you’re using Free Tier — something to keep in mind.
- In production, S3 buckets should be private and accessed through CloudFront (using OAC), but for learning, public access is fine. I also won't use WAF (Web Application Firewall), but in real life, it is very recommended.
- To check the static webpage through S3 webpage, go to the project's bucket, then go to **Properties tab**. Scroll all the way to the bottom and you will see **Bucket Website Endpoint**. Copy it and paste it to webpage.

### Bucket Policy I Used
*For now, I allowed HTTP only ebecause JTTPS requires the certificate.*
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RestrictToHTTPSReqOnly",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::project1-static-webpage",
                "arn:aws:s3:::project1-static-webpage/*"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```
