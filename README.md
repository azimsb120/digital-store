# Digital Store

## About

A minimal digital product marketplace where creators can upload and sell digital content, and users can browse and purchase these products.

For the purposes of this proof of concept, _selling_ refers to distributing digital content, and _purchasing_ refers to downloading it.

## Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** JavaScript (Vue.js)
- **Database:** MySQL
- **Containerization:** Docker
- **Deployment:** AWS (EC2, S3, RDS)

## Run the App

### Environment Variables

Use `.env.example` as a template to create a `.env` file in the current working directory, and set the following variables:

- ENVIRONMENT
- MYSQL_ROOT_PASSWORD
- MYSQL_DATABASE
- MYSQL_USER
- MYSQL_PASSWORD
- DATABASE_URI=`mysql+mysqlconnector://${MYSQL_USER}:${MYSQL_PASSWORD}@{ENVIRONMENT}/${MYSQL_DATABASE}`

Note: For `ENVIRONMENT`, set to `db` for Docker and `localhost` for local development.

### Run using Docker

If available, using Docker (and `docker-compose`) is the easiest way to run the database, backend, and frontend.

From the current working directory, run:

```bash
docker-compose up --build
```

## High-level roadmap

- [x] Version control: Initialize Git repository
- [x] Setup environment: Virtual environment and dependencies for `api`
- [x] Makefile: For setup, dev, clean
- [x] Docker config: Create `docker-compose.yml` and `Dockerfile` for `db` and `api`
- [x] Database integration: MySQL with SQLAlchemy
- [x] Pydantic Models for creators, products, and data validation
- [ ] User management: User registration and login with JWT
- [ ] Creator functionality: APIs for product upload and management
- [ ] File storage: Remote storage with AWS S3
- [ ] Marketplace functionality: APIs for product listing and searching
- [ ] Order processing APIs
- [ ] Frontend setup: Initialize Vue.js with Nuxt.js project
- [ ] Statement management and Routing
- [ ] UI: User registration and login
- [ ] UI: Product management
- [ ] UI: Product listing and details
- [ ] Testing: Unit tests
- [ ] CI/CD: GitHub actions
- [ ] Deploy to AWS
- [ ] Documentation: Details on features, development, and demo

## Acknowledgements

I acknowledge the use of official documentation (Flask, Vue.js), search engines (Google), and LLMs (ChatGPT 4o and Claude 3.5) for assistance in completing this project.
