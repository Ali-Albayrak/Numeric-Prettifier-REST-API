from fastapi import FastAPI, HTTPException

app = FastAPI()

def prettify_number(number: int | float) -> str:
    if not isinstance(number, (int, float)):
        raise ValueError("Invalid input type/format")
    if number >= 10**15:
        raise ValueError("Invalid input. Input number length is too large")
    
    if number >= 10**12:
        return f"{number / 10**12:.1f}T"
    elif number >= 10**9:
        return f"{number / 10**9:.1f}B"
    elif number >= 10**6:
        return f"{number / 10**6:.1f}M"
    elif number >= 10**3:
        return f"{number / 10**3:.1f}K"
    elif number != int(number):
        return f"{number:.1f}"
    else:
        return str(int(number))
    
    # TODO handle negative numbers


@app.get("/prettify/{number}")
def get_prettified_number(number: str):
    try:
        parsed_number = float(number.replace(",","."))
        prettified_number = prettify_number(parsed_number)
        return {"prettified_number": prettified_number}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
