# Bookstore Django Project Deployment

This guide will help you set up and run the Django project using Docker Compose on both Linux (Ubuntu) and Windows.

## Prerequisites

Ensure that the following software is installed on your system:

- **Docker**: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### On Windows
- **WSL2**: If you are using Windows, it's recommended to use WSL2 (Windows Subsystem for Linux) to run Docker.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/Bookstore.git
cd Bookstore
2. Configure Environment Variables
Create a .env file in the root directory of the project and add the necessary environment variables:

bash
Copy code
cp .env.example .env
Edit the .env file according to your environment setup.

3. Build and Run the Containers
On Linux (Ubuntu)
bash
Copy code
sudo docker-compose up --build
On Windows
Ensure that your Docker Desktop is running and configured with WSL2 integration. Then run:

bash
Copy code
docker-compose up --build
4. Access the Application
Once the containers are up and running, you can access the Django application at:

Linux (Ubuntu): http://localhost
Windows: http://localhost
