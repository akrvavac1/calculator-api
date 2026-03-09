from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"operation": "add",
        "a": a,
        "b": b,"result": a + b}

#subtraction endpoint
@app.get("/subtract/{a}/{b}",status_code=200)
def subtract(a: float, b: float):
    """
    Subtracts two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": a - b
    }

#multiplication endpoint
@app.get("/multiply/{a}/{b}",status_code=200)
def multiply(a: float, b: float):
    """ 
     Multiplies two given numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"operation": "multiply",
     "a": a,
     "b": b,
     "result": a * b}    

#Divide Endpoint
@app.get("/divide/{a}/{b}",status_code=200)
def divide(a: float, b: float):
    """
    Divides two given numbers.

    Parameters:
    - a: First number
    - b: Second number

    Returns:
    - JSON object with the result
    """
    if b == 0:
        raise HTTPException(
            status_code=422,
            detail="Division by zero is not allowed. Please use a non-zero value for b."
        )

    return{"operation": "divide",
     "a": a,
     "b": b,
     "result": a / b}


#Additional Endpoint(1):
@app.get("/rectanglearea-endpoint1/{length}/{width}",status_code=200)
def rectanglearea(length: float, width: float):
    """
    Calculates the area of a rectangle by multiplying its length and width.

    Parameters:
    - Length: The length of the rectangle
    - Width: The width of the rectangle

    Returns:
    - JSON object containing the rectangle area
    """

    if length <= 0 or width <= 0:
        raise HTTPException(
            status_code=422,
            detail="Length and width must be positive numbers."
        )

    area = length * width

    return {
        "operation": "rectanglearea",
        "Length": length,
        "Width": width,
        "Result": area
    }    

#Additional Endpoint(2):
@app.get("/celsius-to-fahrenheit-endpoint-2/{celsius}",status_code=200)
def celsius_to_fahrenheit(celsius: float):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    - Celsius: Temperature in Celsius

    Returns:
    - JSON object containing the converted Fahrenheit value
    """

    fahrenheit = (celsius * 9/5) + 32

    return {
        "Operation": "celsius_to_fahrenheit",
        "Celsius": celsius,
        "Result": fahrenheit
    }

#Additional Endpoint(3):
@app.get("/compound-interest-endpoint-3/{principal}/{rate}/{time}",status_code=200)
def compound_interest(principal: float, rate: float, time: float):
    """
    Calculates compound interest over time given the principal, interest rate, and time.

    Parameters:
    - Principal: Initial amount of money
    - Rate: Interest rate (enter as a decimal, for example, 0.08 for 8%)
    - Time: Number of years

    Returns:
    - JSON object containing the final amount after compound interest
    """

    if principal <= 0:
        raise HTTPException(
            status_code=422,
            detail="Principal must be greater than zero."
        )

    if rate < 0:
        raise HTTPException(
            status_code=422,
            detail="Interest rate cannot be negative."
        )

    if time <= 0:
        raise HTTPException(
            status_code=422,
            detail="Time must be greater than zero."
        )

    amount = principal * (1 + rate) ** time

    return {
        "operation": "compound_interest",
        "Principal": principal,
        "Rate": rate,
        "Time": time,
        "Result": amount
    }   