import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is live!"}

@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        # Convert input to integer
        num = int(number)
    except ValueError:
        # Return 400 status with `error: true`
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
            media_type="application/json"
        )

    # Determine if the number is odd or even
    properties = ["even" if num % 2 == 0 else "odd"]

    # Check if the number is an Armstrong number
    digit_powers_sum = sum(int(digit) ** len(str(abs(num))) for digit in str(abs(num)))
    is_armstrong = num == digit_powers_sum
    if is_armstrong:
        properties.insert(0, "armstrong")

    # Check if the number is prime
    if num > 1:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    else:
        is_prime = False

    # Check if the number is a perfect number
    is_perfect = num > 1 and sum(i for i in range(1, num) if num % i == 0) == num

    # Construct the response with newline formatting
    response = {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "is_armstrong": is_armstrong,
        "properties": properties,  # List will be formatted correctly in JSON
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": f"{num} is just an interesting number!"
    }

    # Return JSON with indentation for proper formatting
    return JSONResponse(content=response, media_type="application/json", headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)