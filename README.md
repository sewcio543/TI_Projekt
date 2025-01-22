# GrudgeHub

GrudgeHub is a place where you can let it all out!
This social media does not accept positive content, only grudges and complaints.

If you are too polite, app will turn itself into a [teapot](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418).

## Getting started

### 1. Run Docker

Run the following commands to build and start all services:

```bash
docker-compose build
docker-compose up
```

Wait for all services to initialize.

### 2. Access the application

The React frontend will be available at:
<http://localhost:3000>

You can directly access API through Swagger UI at:

- **Identity API**: <http://localhost:8000>
- **Content API**: <http://localhost:8001>
- **People API**: <http://localhost:8002>

## Architecture Overview

### Multi-Service Architecture

GrudgeHub follows a microservice architecture. The platform consists of several loosely coupled services that communicate with each other through REST APIs.

### Technology Stack

1. **Backend APIs**:
   - **FastAPI** and **SQLModel**
   - Each API is focused on a specific domain:
     - **Identity API**: Handles user authentication and token management.
     - **Content API**: Manages posts and grudges (comments, but only negative)
     - **People API**: Manages user profiles.

2. **Database**: **PostgreSQL**
3. **Frontend**: **React**

**Give your worst!** 🤬
