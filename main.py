from fastapi import FastAPI, HTTPException

app = FastAPI()

def prettify_number(number: int | float) -> str:
    """
    Prettifies a numeric value according to specified rules.

    Args:
        number (int | float): The numeric value to be prettified.

    Returns:
        str: The prettified string version of the number.

    Raises:
        ValueError:
            - If the input is not a valid numeric type.
            - If input larger then 10^15.
    """

    # Handlinge non-numeric values
    if not isinstance(number, (int, float)):
        raise ValueError("Invalid input type/format")
    
    # Handling negative numbers
    sign = ""
    if number < 0:
        sign = "-"
        number = abs(number)

    # Handling large numbers
    if number >= 10**15:
        raise ValueError("Invalid input. Input number length is too large")
    
    if number >= 10**12:
        return f"{sign}{number / 10**12:.1f}T"
    elif number >= 10**9:
        return f"{sign}{number / 10**9:.1f}B"
    elif number >= 10**6:
        return f"{sign}{number / 10**6:.1f}M"
    elif number >= 10**3:
        return f"{sign}{number / 10**3:.1f}K"
    elif number != int(number):
        return f"{sign}{number:.1f}"
    else:
        return f"{sign}{int(number)}"


@app.get("/prettify/{number}")
def get_prettified_number(number: str):
    """
    REST API endpoint to prettify a numeric value.

    Args:
        number (str): The numeric value to be prettified.

    Returns:
        dict: A JSON response containing the prettified number.

    Raises:
        HTTPException:
            - If the input cannot be parsed as a float.
            - If there is an issue with the prettification process.
    """
    try:
        parsed_number = float(number.replace(",","."))
        prettified_number = prettify_number(parsed_number)
        return {"prettified_number": prettified_number}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
