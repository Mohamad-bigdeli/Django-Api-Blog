<h1>Introduction</h1>
This project is a dynamic and functional blog designed to provide a suitable platform for publishing and managing content. In the account section, the Juser package is used for user management, and JWT is employed for secure authentication. This ensures the security and efficiency of the system in managing users.
The blog section of the project allows for the publication of posts in various categories. Users can easily categorize and share their posts based on different topics. This feature helps to better organize content and facilitates easier access for users to their desired materials.

<h1>Technologies</h1>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Flake8](https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white)
![Black](https://img.shields.io/badge/Black-000000?style=for-the-badge&logo=black&logoColor=white)
![Locust](https://img.shields.io/badge/Locust-000000?style=for-the-badge&logo=locust&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-000000?style=for-the-badge&logo=faker&logoColor=white)

<h1>Project Overview</h1>
This project leverages a robust stack of technologies to ensure efficient development, testing, deployment, and monitoring. Below is a breakdown of the key technologies used:

- Python : The primary programming language for backend development.

- Django : A high-level web framework for building secure and maintainable web applications.

- GitHub Actions : Used for CI/CD automation, enabling seamless testing and deployment workflows.

- Docker : Containerization tool to create consistent development and deployment environments.

- Pytest : A powerful testing framework to ensure code reliability and quality.

- Faker : A library for generating fake data, useful for testing and populating databases.

- Redis : Serves as both a caching layer and message broker for Celery.

- Celery : Handles background task processing and asynchronous job execution.

- Swagger : Provides interactive API documentation for easy testing and integration.

- JWT : JSON Web Tokens for secure user authentication and authorization.

- Nginx : Acts as a web server and reverse proxy to manage incoming traffic.

- Flake8 & Black : Tools for code linting and automatic code formatting to maintain code quality.

- Locust : A load testing tool to evaluate the application's performance under stress.

## 🚀 Project Setup

To set up the project, follow the steps below:

### Prerequisites
- **Docker**: If you don't have Docker and Docker Compose installed, follow the [Docker installation guide](https://docs.docker.com/get-docker/) and the [Docker Compose installation guide](https://docs.docker.com/compose/install/).

---

### Setup Steps

1. **Clone the Repository**
  
   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/Mohamad-bigdeli/Django-Api-Blog.git

2. **Navigate to the Project Folder**

    Move into the project directory using the cd command:

    ```bash
    cd Django-Api-Blog
    

3. **Start Docker Compose** 

    Use Docker Compose to start the project services by running the command:

    ```bash
    docker-compose up --build 

4. **Create and Apply Migrations**

    After the services are up, create and apply the database migrations using the following commands:
    ```bash 
    docker-compose exec backend sh -c "python manage.py makemigrations"

    docker-compose exec backend sh -c "python manage.py migrate"

5. **Create a Superuser**

    Create a superuser to access the Django admin panel by running the command:

    ```bash
    docker-compose exec backend sh -c "python manage.py createsuperuser"

6. **Collect Static Files**

    Collect static files for the project using the command:

    ```bash
    docker-compose exec backend sh -c "python manage.py collectstatic --noinput"
    
7. **View the Project**

    Your project is now running on port 8000. Open your browser and navigate to:

   ```bash
    http://localhost:8000.

8. **Access the Admin Panel**

    To access the Django admin panel, go to the following URL and log in with your superuser credentials:

    ```bash
    http://localhost:8000/admin

**Additional Notes**

    If you make changes to the code and need to restart the services, use the docker-compose restart command.
    To stop the services, use the docker-compose down command.

<h3>By following these steps, your project will be fully set up and ready to use. 🎉</h3>

