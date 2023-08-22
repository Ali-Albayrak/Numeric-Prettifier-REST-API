# Numeric Prettifier REST API
This is a Python project that implements a REST API using the FastAPI framework.
The API accepts numeric input and returns a prettified string version of the number according to specified rules.


## Project Structure

The project consists of the following files:

- `main.py`: This is the main file that defines the FastAPI application and the endpoint for prettifying numbers.
- `app_tests.py`: This file contains unit tests to verify the functionality of the `prettify_number` function and the API endpoint.
- `requirements.txt`: This file lists the required Python packages and their versions for the project.
- `README.md`: This is the README file you're currently reading, providing an overview of the project and its files.


## How to Run

1. Install the required packages listed in `requirements.txt` using the following command:
```pip install -r requirements.txt```

2. Run the FastAPI server using Uvicorn with the following command:
```uvicorn main:app --reload```


## How to Test

1. Run the unit tests defined in `tests.py` using the following command:
```python -m unittest tests.py```
