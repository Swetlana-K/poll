# Django Polling Application

## Introduction
In this Django project, will be created a polling application that allows users to create and participate in polls. This application is built using the Django framework, providing a seamless and user-friendly tool for both poll creators and voters.

## Features

1. **Poll Creation:**
   - Poll creation and participation will be not restricted to authenticated users.
   - Users can create polls with multiple choices.
   - They can set one or more datees and specify the time.

2. **Poll Voting:**
   - Users can cast their votes in active polls.
   - Users can choose from the available options and submit their votes.

3. **Results Display:**
   - The application will display real-time results for each poll.
   - Users can view the distribution of votes.

4. **Admin Panel:**
   - Django's built-in admin panel will allow administrators to manage polls, users, and monitor voting activity.

5. **Poll Expiry:**
   - Admins can close or archive polls manually.

## Quick Installation Guide for the Project
### Step 1: Clone Repository

    git clone <repository-url>
    cd <repository-name>

### Step 2: Create and Activate Virtual Environment

    python -m venv venv
    source venv/bin/activate

### Step 3: Install Dependencies

    make dev-install

### Step 4: Create .env File

Create a file named .env in the project's main directory and add the following contents:

    DB_USER: User
    DB_PWD: Password
    DB_HOST: Host, Server
    DB_NAME: Database Name
    DB_PORT: Connection Port
    SECRET_KEY: Secret Key
    DB_ENGINE: Database Engine

### Step 5: Set Up Database

Ensure that the PostgreSQL database is running. Create the database with the information from the .env file:

    psql -U postgres
    CREATE DATABASE DatabaseName;

### Step 6: Perform Database Migrations

    make dev-migrate

### Step 7: Start Development Server

    make dev-start

Open your web browser at http://127.0.0.1:8000/.

