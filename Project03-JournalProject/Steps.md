# Project Plan: Cloud-Based Wellness Journal

This document outlines the tasks for building a Serverless (API Gateway, Lambda, DynamoDB) and CI/CD powered journal application.

## 1. Project Conception and Initiation (P1)
**Goal:** Define the scope, data structure, and psychological foundation.

- [x] P1.1 Conceptualize web design for "Journaling": Define the overall UX/UI flow (Home -> Entry Form -> Entries List -> Settings).
- [ ] P1.2 Read and take notes on core psychological concepts: Focus on Vulnerability, Shame vs. Guilt, Courage.
- [x] P1.3 Define structured Morning/Evening Check-in data: Finalize the structured data fields (e.g., MorningMood (1-5), TalkedToSomeone (boolean)).
- [ ] P1.4 Curate initial action-oriented quotes and themes: Create a list of 10-15 quotes grouped by theme (Courage, Boundaries, etc.).
- [ ] D4.1 Initialize Project Repository: Create a GitHub repository structured with folders: /frontend, /lambda_code, and buildspec.yml.

---

## 2. Frontend Skeleton & Core Logic (P3)
**Goal:** Build the user interface and prepare to send data to the API.

- [ ] F2.1 Decide necessary pages and folder structure: Pages: index.html (Entry Form), entries.html (List), settings.html. Structure: /frontend/css, /frontend/js.
- [ ] F2.2 Build the journal form and pages (HTML/CSS): Create the static HTML for the form, list view, and settings view based on P1.3 fields.
- [ ] F2.3 Capture and validate form input (JavaScript): Use JavaScript to read form data and package it into a single JSON object.
- [ ] F2.4 Store memories in localStorage: (Optional/Temporary data store until authentication is live).
- [ ] F2.5 Render entries on the page (JavaScript functions for list view).
- [ ] F3.4 Deploy Frontend to S3 (Static Hosting): Create an S3 bucket and configure for Static Website Hosting.
- [ ] F3.5 Set up CloudFront in front of S3: Create a CloudFront Distribution pointing to the S3 bucket for content acceleration.

---

## 3. BackEnd Creation (P2 - AWS Project 4)
**Goal:** Build the core serverless architecture. 

- [ ] A3.1 Create DynamoDB table (WellnessJournalEntries): PK: UserID, SK: EntryDateTimestamp.
- [ ] A3.2 Create IAM Role for Lambda: Policy grants only PutItem and GetItem on the DynamoDB table ARN (Least Privilege).
- [ ] A3.3 Create and deploy core Lambda function (handler): Write the code to handle JSON input and perform the PutItem operation to DynamoDB.
- [ ] A3.4 Set up API Gateway (REST API): Create the API and the /entries resource.
- [ ] A3.5 Integrate Lambda with API Gateway: Define the POST method on /entries and link it to the Lambda function. Enable CORS.
- [ ] F3.3 Connect Frontend to Backend (fetch()): Update frontend JavaScript to send the JSON data to the deployed API Gateway URL.
- [ ] A3.6 Test End-to-End Flow: Use Postman/Console to verify that a submission successfully saves an entry to DynamoDB.
- [ ] B3.7 Handle success/failure visually: Update the frontend JS to display API response status messages.
- [ ] B3.8 Remove localStorage (if used): Clean up temporary data storage if A3.6 is successful.

---

## 4. Authentication (Optional/Advanced - P4)
**Goal:** Secure the API and enable user personalization.

- [ ] B4.1 Set up Cognito User Pool (User Pool/App Client).
- [ ] B4.2 Add login button and handle redirect (Use Cognito Hosted UI).
- [ ] B4.3 Receive and manage ID token (Capture token upon successful login).
- [ ] B4.4 Attach token to API requests (Include ID Token in fetch() headers).
- [ ] B4.5 Configure API Gateway Authorizer: Secure the /entries resource using the Cognito Authorizer.

---

## 5. Add AI Functionalilty (P3/P5)
**Goal:** Implement the core psychological feedback logic.

- [ ] F5.1 Design the AI/Quote Logic Flowchart: Finalize the logic that maps entry data (P1.3) to quote themes (P1.4).
- [ ] F5.2 Implement Quote/Insight Logic in Lambda: Update the function (A3.3) to run the logic (F5.1) and select a quote.
- [ ] F5.3 Show AI response below journal entry: Update frontend JS (F3.3) to read and render the quote/prompt returned by the API.
- [ ] F5.4 Add "reflect more" button (Prompt generation).
- [ ] F5.5 Display weekly reflection section: Create a new Lambda function (GET /entries) to query DynamoDB for a user's recent entries.

---

## 6. Settings and Personlization (P3/P4)
**Goal:** Add user configuration and maintenance features.

- [ ] F6.1 Give theme selector (Frontend only CSS/JS logic).
- [ ] F6.2 Reminder preference (Store only): Add Lambda/DynamoDB logic to store user preferences.
- [ ] F6.3 Delete account/data button: Create a secure Lambda/API endpoint (DELETE /user) to remove user data from DynamoDB and Cognito.

---

## 7. CI/CD and Project Monitoring (P4 - AWS Project 5)
**Goal:** Set up automated deployment and test system resilience. 

- [ ] D7.1 CI/CD Backend Setup: Configure CodePipeline to use CodeBuild to deploy Lambda (A3.3) changes pushed to GitHub.
- [ ] D7.2 CI/CD Frontend Setup: Configure a second CodePipeline to deploy Frontend changes (F2.1-F2.5) to the S3 bucket (F3.4).
- [ ] D7.3 Break/Fix & Documentation: Intentionally break the code, run the pipeline, fix the issue, and document the failure and the solution found in CloudWatch logs.