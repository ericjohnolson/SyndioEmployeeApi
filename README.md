# Syndio Employee Api
This Syndio Backend App is an API exposing employee diversity and equity indicators. The API leverages the following technologies:
* [FastAPI](https://fastapi.tiangolo.com/) - a modern, fast, web framework for building APIs
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and ORM
* [Uvicorn](https://www.uvicorn.org/) - an ASGI web server implementation for Python

## Getting Started
1. Using a terminal, install the project requirements from the base directory, `employeeApi`
   ```bash
   pip install -r requirements.txt
   ```
2. Create an environment variable defining the port the API will run on, for example:
   ```bash
   export PORT="7071" 
   ```
3. Start the Uvicorn webserver, run the app:
   ```bash
   uvicorn app.main:app --port $PORT  
   ```
4. To ensure the API is running and review the Swagger documentation, browse to `http://localhost:$PORT/docs` 
replacing $PORT with the port number you specified in the environment variable above. 
   1. For example, using 7071, you can view the [Syndio Employee Api Docs](http://localhost:7071/docs)


5. Finally you can test executing the API, by getting employees:
   ```bash
   curl localhost:$PORT/employees
   ```