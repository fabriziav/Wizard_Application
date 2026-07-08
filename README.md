# Wizard Application 🧙‍♂️

**⚠️ WARNING: DELIBERATELY VULNERABLE APPLICATION ⚠️** *Do not deploy this application to any production environment or public cloud. This repository contains intentional security flaws, hardcoded (dummy) secrets, and severely outdated dependencies. It is designed strictly for local testing, educational purposes, and security tool demonstrations.*

## Overview

Wizard Application is a "vulnerable-by-design" sandbox project. It was created to demonstrate and test the capabilities of modern security tools like **Wiz**, **GitHub Advanced Security**, and AI-powered remediation assistants like **GitHub Copilot** integrated with the **Wiz MCP Server**.

The repository contains a multi-layered security disaster, including Infrastructure as Code (IaC) misconfigurations, Software Composition Analysis (SCA) risks, Static Application Security Testing (SAST) flaws, and leaked secrets.

## Features & Included Vulnerabilities

This project encompasses several files, each demonstrating different categories of security risks:

* **`app.py` (Application Logic - SAST & Secrets)**
    * **SQL Injection (CWE-89):** Blindly trusts user input using string formatting instead of parameterized queries.
    * **Command Injection (CWE-78):** Passes unsanitized user input directly to the OS shell.
    * **Exposed Secrets:** Contains a hardcoded, plaintext Stripe API key.
* **`main.tf` (Infrastructure - IaC Misconfigurations)**
    * **Hardcoded Credentials:** Contains plaintext AWS access and secret keys.
    * **Public Exposure:** Provisions an S3 bucket with a `public-read` ACL.
    * **Wide-Open Firewall:** Opens SSH (port 22) to the entire internet (`0.0.0.0/0`).
* **`Dockerfile` (Container Security)**
    * **Outdated Base Image:** Uses `python:3.6-slim`, which contains numerous unpatched OS-level CVEs.
    * **Root Privilege:** Runs the application as the `root` user (missing the `USER` directive).
* **`requirements.txt` (Dependencies - SCA Risks)**
    * Pins application dependencies to ancient versions (e.g., `Flask==0.12.2`) with known Critical and High severity CVEs.
* **`dev_notes.txt` (Data Exposure)**
    * Simulates careless developer documentation containing plaintext admin passwords and internal IP addresses.

## Technologies Used

* **Python / Flask** (Backend application)
* **Terraform / HCL** (Infrastructure provisioning)
* **Docker** (Containerization)
* **SQLite** (Database)

## Usage & Demo Guide

This repository is perfect for demonstrating how security tools identify and remediate risks across the Software Development Life Cycle (SDLC).

### 1. Local IDE Scanning
Open this project in your IDE (e.g., IntelliJ IDEA or VS Code) with your security linter/extension enabled to demonstrate how the tools highlight vulnerable code, exposed secrets, and bad IaC practices in real-time.

### 2. AI-Assisted Remediation (Copilot + Wiz MCP)
You can use this repository to showcase AI remediation:
1. Open `app.py` in your IDE.
2. Open GitHub Copilot Chat (ensure it is in Agent mode).
3. Ask the assistant to review the file using the Wiz MCP Server:  
   *"Use the Wiz MCP server to find SAST issues in `app.py` and provide the secure remediation snippet for the SQL injection."*

### 3. Pipeline / PR Scanning
Integrate this repository with a CI/CD pipeline (e.g., GitHub Actions) to demonstrate how security scanners block pull requests containing critical vulnerabilities or exposed secrets from being merged.
