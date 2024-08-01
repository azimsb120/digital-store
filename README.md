# Digital Store

## About

A minimal digital product marketplace where creators can upload and sell digital content, and users can browse and purchase these products.

## Tech stack

- **Backend:** Python (Flask)

- **Frontend:** JavaScript (Vue.js)

- **Database:** MySQL

- **Containerization:** Docker

- **Deployment:** AWS (EC2, S3, RDS)

## Run the app

### Using docker

If available, using docker (and `docker-compose`) is the easiest way to run the db, backend, and frontend.

From the current working directory, run:

```bash
docker-compose up --build
```

## High-level roadmap

- [ ] Version control: Initialize Git repository
- [ ] Setup environment: Virtual environment and dependencies for `api`
- [ ] Makefile: For setup, dev, clean
- [ ] Docker config: Create `docker-compose.yml` and `Dockerfile` for `db` and `api`
- [ ] Database integration: MySQL with SQLAlchemy
- [ ] Pydantic Models for creators, products, and data validation
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

I acknowledge the use of official the documentations (Flask, Vue.js), search engine (Google), and LLMs (ChatGPT 4o and Claude 3.5) for assistance in completing this project.
