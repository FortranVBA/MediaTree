
# Fruit Shop application

Fruit Shop is an application for products and sells management, developped for MediaTree as part of technical test assessment.
This application has been developed with the Django framework, using SQlite database (with precreated data).

The application features are the followings:
- Product registration by name, description and date of last modification.
- Sell registration by associated product sold, quantity (that must be an integer number) and date of last modification.
- The total quantity sold by product are listed on the sells main page.

## Warning

This application is intented for local execution and shall not be used as such in production (for example, sensitive variables need to be set as environment variables before production).

## Installation and first launch

This locally-executable application can be installed and executed from [http://localhost:8000/](http://localhost:8000/) using the following steps.

1. Clone this repository using $ git clone `https://github.com/FortranVBA/MediaTree.git` (you can also download the code using [as a zip file](https://github.com/FortranVBA/MediaTree/archive/refs/heads/master.zip))
2. Move to the application root folder.
3. Create a virtual environment for the project with `$ py -m venv .venv` on windows or `$ python3 -m venv .venv` on macos or linux.
4. Activate the virtual environment with `$ .venv\Scripts\activate` on windows or `$ source .venv/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Run the server with `$ python manage.py runserver`

When the server is running after step 6 of the procedure, the Fruit Shop application can be used with the following base URL: http://localhost:8000/.


## Usage with user profiles

For subsequent launches of the application, you only have to execute the following steps from the root folder of the project:
1. Activate the virtual environment with `$ .venv\Scripts\activate` on windows or `$ source .venv/bin/activate` on macos or linux.
2. Run the server with `$ python manage.py runserver`

Once you have launched the server, the main application entry point can be reached by visiting [http://localhost:8000/](http://localhost:8000/).

You can use one of the already created user:
-	Username: admin ; Password: admin

Or register a new user to the database, between previous steps 1 and 2, with the command `$ python manage.py createsuperuser` (follow the instructions for user input).

## Usage and detailed endpoint documentation

The application includes an API that can be called from the application web interface.
The list of allowed endpoints is the following:

| Description | Method |Endpoint |
| ----------- | ----------- | ----------- |
| List all products | LIST | /products/ |
| Create new product. Expected fields in body in json format : {name: "Product name", description: "Product description"}| CREATE | /products/ |
| Partial update product. Expected fields in body in json format (blank fields are not updated) : {name: "Product name", description: "Product description"} | PATCH | /products/{id}/ |
| Delete product | DELETE | /products/{id}/ |
| List all sells | LIST | /sells/ |
| Create new sell. Expected fields in body in json format : {product: "Id of product sold", quantity: "Number (positive integer) of product sold"} | CREATE | /sells/ |
| Partial update sell. Expected fields in body in json format (blank fields are not updated) : {product: "Id of product sold", quantity: "Number (positive integer) of product sold"}| PATCH | /sells/{id}/ |
| Delete sell | DELETE | /sells/{id}/ |

## Testing commands

After virtual environment activation, the tests can be launched with the command `$ python manage.py test`.
