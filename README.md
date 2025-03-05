## Manufac Backend API Task

### Task Description
Create a FastAPI server supports 2 routes:


    a. GET /uuid: This route generates and responds with a unique version 4 UUID string each time it is requested.


    b. GET /async-uuid: This route generates and responds with a unique version 4 UUID string each time it is requested. However, the minimum time this request should take to complete is 3 seconds. This 3-sec delay should be added in a non-blocking way.


### Requirements:
- Python 3.10+
- Poetry (for dependency management)
- Docker (for containerization)

### Installation Steps
1. clone the repository: `git clone git@github.com:Ashcroft-lab/manufac_test.git`
2. Install poetry: `pip install poetry`
3. Install dependencies: `poetry install`
4. Run server: `poetry run uvicorn src.manufac_test.main:app --reload`
5. If Running in Docker: `docker build -t fastapi-uuid-server .`
6. Run Docker Container: `docker run -d -p 8000:8000 fastapi-uuid-server`


### API Documentation

- Swagger UI: http://localhost:8000/docs

api endpoints:
- GET /uuid
- GET /async-uuid