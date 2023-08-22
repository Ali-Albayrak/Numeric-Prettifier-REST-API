from fastapi import FastAPI

app = FastAPI()

def prettify_number(number: int | float) -> str:
    pass

@app.get("/prettify")
def get_prettified_number():
    return "Test"
