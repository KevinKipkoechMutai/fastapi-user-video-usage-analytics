# FastAPI Analytics Application

This FastAPI application provides an endpoint to retrieve analytics data related to user activities. The `/analytics` endpoint allows users to query the total watched hours of user activities grouped by user groups over a specified period (either by year or by month).

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Endpoint Documentation](#endpoint-documentation)
- [License](#license)

## Installation

To set up the FastAPI application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KevinKipkoechMutai/fastapi-user-video-usage-analytics
   cd fastapi-user-video-usage-analytics
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your database:**
   Ensure you have a database set up and configured in your application. Update the database connection settings in your `dependencies.py` file.

## Running the Application

To run the FastAPI application, use the following command:
```bash
   uvicorn main:app --reload
   ```

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.

## Endpoint Documentation

### `GET /analytics`

This endpoint retrieves analytics data for user activities.

#### Query Parameters

- `group_ids` (optional): A list of integers representing the IDs of user groups to filter the results. If not provided, results for all groups will be returned.
- `period`: A string indicating the time period for the analytics data. It can be either:
  - `year`: Returns data grouped by year.
  - `month`: Returns data grouped by month.

#### Response

The response will be a JSON object containing:

- `period`: The period used for the analytics (either "year" or "month").
- `data`: A list of objects, each containing:
  - `group_name`: The name of the user group.
  - `watched_hours`: The total hours watched by users in that group.
  - `period`: The corresponding year or month for the data.

#### Example Request
GET http://localhost:8000/analytics?group_ids=1,2&period=year


#### Example Response
{
"period": "year",
"data": [
{
"group_name": "Group A",
"watched_hours": 120.5,
"period": "2023"
},
{
"group_name": "Group B",
"watched_hours": 95.0,
"period": "2023"
}
]
}

## License

This project is licensed under the MIT License. 