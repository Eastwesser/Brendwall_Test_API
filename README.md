# Brendwall Test API

This project is a simple Django application that provides an API for managing products and a frontend interface for interacting with this API. 

## Features

- **API Endpoints:**
  - `POST /api/products/` - Create a new product.
  - `GET /api/products/` - Retrieve a list of all products.

- **Frontend:**
  - A basic HTML page with a form for adding new products and a table to display the list of products.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Eastwesser/Brendwall_Test_API.git
   cd brendwall_tz
   ```
   
2. **Create a Virtual Environment**

  ```bash
  python -m venv .venv
  ```

3. **Activate the Virtual Environment**

On Windows:

  ```bash
  .venv\Scripts\activate
  ```
On macOS/Linux:

  ```bash
  source .venv/bin/activate
  ```

4. Install Dependencies

  ```bash
  pip install -r requirements.txt
  ```

If you don't have a requirements.txt file, you can create one with:

  ```bash
  pip freeze > requirements.txt
  ```

Then, install Django and Django REST Framework:

  ```bash
  pip install django djangorestframework
  ```

5. Apply Migrations

  ```bash
  python manage.py migrate
  ```

6. Create a Superuser (Optional)

To access the Django admin interface, you may want to create a superuser:

  ```bash
  python manage.py createsuperuser
  ```

## Running the Server
To start the Django development server, run:

  ```bash
  python manage.py runserver
  ```
The server will be available at http://127.0.0.1:8000/.

## Using the API
- Create a Product:

  - URL: /api/products/
  - Method: POST
  - Request Body:
    ```json
    {
      "name": "Tablet",
      "description": "The best tablet for work!",
      "price": 11.99
    }
    ```
  - Response: JSON object of the created product.
  
- Retrieve Products:

    - URL: /api/products/
    - Method: GET
    - Response: JSON array of all products.

## Frontend Usage
1. Open your browser and go to http://127.0.0.1:8000/.
2. Use the form to add new products.
3. The list of products will be displayed in the table below the form.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.
