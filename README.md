# Number Classification API

## Overview
The Number Classification API is designed to analyze a given number and return its mathematical properties along with a fun fact. This API is useful for mathematical enthusiasts, educators, and developers who need number-based insights in their applications.

## Features
- **Classifies Numbers:** Determines if a number is prime, even, odd, or a perfect square.
- **Mathematical Properties:** Provides properties like factors, divisibility, and more.
- **Fun Facts:** Returns an interesting fact about the number.
- **Publicly Accessible:** Available for external applications via a RESTful endpoint.
- **CORS Handling:** Supports cross-origin resource sharing.
- **JSON Responses:** Returns well-structured JSON outputs.

## API Endpoints
### `GET /classify?number=<input>`
#### Request Parameters
- `number` (integer, required): The number to be classified.

#### Example Request
```
GET /classify?number=7
```

#### Example Response
```json
{
  "number": 7,
  "is_prime": true,
  "is_even": false,
  "is_odd": true,
  "is_perfect_square": false,
  "factors": [1, 7],
  "fun_fact": "7 is considered a lucky number in many cultures."
}
```

## Deployment & Hosting
The API is hosted on GitHub and deployed to a publicly accessible server. The deployment process includes:
- **Framework:** Built using FastAPI for high performance.
- **Cloud Hosting:** Deployed on Render at [Number Classification API](https://number-classification-api-430j.onrender.com).
- **Automated Testing:** Ensures reliability before updates.

## Installation & Running Locally
To run the API locally, follow these steps:

### Prerequisites
- Python 3.x
- FastAPI
- Uvicorn

### Steps
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd number-classification-api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the API:
   ```sh
   uvicorn app:app --reload
   ```
4. Access it at `http://127.0.0.1:8000/classify?number=10`

## Contributing
Contributions are welcome! If you want to improve this API, feel free to:
- Fork the repository
- Create a new branch
- Submit a pull request

## License
This project is licensed under the MIT License.

## Contact
For any questions or support, reach out via email or open an issue on GitHub.

