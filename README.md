# FastAPI




## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:kasyap04/machinetest-sms-campaigner-backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd machinetest-sms-campaigner-backend
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirement.txt
    ```

## Configuration
1.  create `.env` file from `.env.example` and fill the constants
2.  (Optional) Might need to be change frontend url in main.py to avoid CORS issue

## Running the App

Once the dependencies are installed, you can start the FastAPI application:

```bash
uvicorn main:app --host localhost --port 8000
```

### API Endpoints

###### `/create-admin`

This endpoint accepts a POST request with the following JSON body:

- `username`: The username for the new admin account (string).
- `password`: The password for the new admin account (string).

**Example Request:**

```bash
curl -X POST "http://[HOST]:[PORT]/create-admin" -H "Content-Type: application/json" -d '{"username": "admin", "password": "securepassword"}'
```

Result:
```bash
{
  "status": True,
  "msg": "Admin created"
}
```


## Unit Test
```bash
pytest
```