# Secure RDS Simulation

A local simulation of a secure AWS RDS deployment using Docker, MySQL, and Flask. This project demonstrates database connectivity, secret rotation, backup and restore workflows, and secure application integration.

## Features

* Dockerized MySQL Database
* Flask Application Integration
* Environment-Based Configuration
* Secret Rotation Simulation
* Automated Backup and Restore
* Persistent Data Storage using Docker Volumes

## Architecture

Flask Application → MySQL Database (Docker)

## Tech Stack

* Python
* Flask
* MySQL
* Docker
* Docker Compose

## Project Structure

secure-rds-simulation/
├── app/
├── scripts/
├── backups/
├── ssl/
├── docker-compose.yml
├── .env
└── README.md

## Getting Started

### Start Database

docker compose up -d

### Install Dependencies

pip install -r app/requirements.txt

### Run Application

python app/app.py

### Test Secret Rotation

python scripts/rotate_secret.py

### Create Backup

python scripts/backup.py

### Restore Backup

python scripts/restore.py

## Learning Outcomes

* Database Containerization
* Application-to-Database Connectivity
* Configuration Management
* Backup and Recovery Concepts
* Secure Credential Handling
