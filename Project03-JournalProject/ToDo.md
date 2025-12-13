Task List for Journaling

### 1. Project Conception and InitiationPsychological & Functional Design 
- [x] Conceptualize web design for "Journaling"
- [x] Read and take notes on core psychological concepts.

### 2. Frontend Skeleton
- [ ] Decide necessary pages and what each pages do
- [ ] Create folder structure (use HTML and CSS)
- [ ] Build the journal form and each pages
- [ ] Capture and validate form input (JavaScript)
- [ ] Store memories in localStorage (JavaScript)
- [ ] Render entries on the page (JavaScript)

### 3. BackEnd Creation
- [ ] Create Lambda or auto function
- [ ] Send frontend data via fetch()
- [ ] Handle success/failure visually
- [ ] Remove localStorage - still debating

### 4. Authentication
- [ ] Add login button
- [ ] Handle login redirect
- [ ] Received ID token
- [ ] Attach token to API requests

### 5. Add AI functionalilty
- [ ] Show AI response below journal entry
- [ ] Add "reflect more" button
- [ ] Display weekly reflection section
- [ ] Design the AI/Quote Logic Flowchart

### 6. Settings and Personlization
- [ ] Give theme selector
- [ ] Reminder preference (store only)
- [ ] Delete account button

##### What to search
- “DynamoDB simple schema example”
- “JSON request body REST API example”
- “DynamoDB simple schema example”
- “JSON request body REST API example”
- “display API response in HTML”
- “JavaScript DOM update”


# Other from Gemini 

### Core Serverless API (15 hrs)
- [ ] Create a DynamoDB table (WellnessJournalEntries).
- [ ] Create an IAM Role for the Lambda function.
- [ ] Write and deploy a Python/Node.js Lambda function (POST /entries).
- [ ] Create a REST API in API Gateway.
- [ ] Define the resource path /entries and integrate it with the Lambda function (2.3).
- [ ] Test the full flow: Send a sample JSON entry via Postman/Console.

### Functionality & User Interface
- [ ] Implement the Quote/Insight Logic (P1.5) inside Lambda.
- [ ] Create a simple HTML form for the journal entries.
- [ ] Write JavaScript to handle the form submission and call API Gateway.
- [ ] Deploy the HTML/CSS/JS files to an S3 Bucket configured for static website hosting.
- [ ] Set up CloudFront in front of the S3 bucket.

### CI/CD Pipeline (20 hrs)
- [ ] Create a GitHub repository for the project.
- [ ] Set up CodePipeline for the Serverless Backend.
- [ ] Configure the Deploy Stage of the backend pipeline to update the Lambda function.
- [ ] Set up a second CodePipeline for the Static Frontend.