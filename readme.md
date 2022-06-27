# Welcome to BiteFinder! 

The answer to the most difficult question we face...What do you want to eat?

BiteFinder lets you search through hundreds of local eateries in your area and choose one by random. No more decision paralysis!

Don't like your choice? Search again to find a a place more suitable to you. 

_____

# Full-Stack Application Details 
## API Used:
- Yelp -- https://fusion.yelp.com/

## Frontend Technologies:
- Primary Language: Javascript
- Methodologies/Frameworks: AJAX, JQuery, WTForms (Form Validation and CSRF Protection)

## Backend Technologies:
- Primary Language: Python
- Methodologies/Frameworks: Flask, SQLalchemy,PostgreSQL, Jinja (templating), Password Hashing/Salt (BCrypt)

_____

# App Run Instructions

## Visit on Heroku
To access, please visit https://bitefinder75.herokuapp.com/

application can be used without signing up or you can create an account via the sign up link
create account via sign up button

## Run locally
To get this application running, make sure you do the following in the Terminal:

- Fork Repo and Clone to local repository 
- While in application directory enter the following commands in your terminal: 
  - `python3 -m venv venv`
  - `source venv/bin/activate` (activates virtual environment)
  - `pip install -r requirements.txt`
    - If you are using Python 3.8 instead of 3.7, then you will have issues with installing some of the packages in the requirements.txt file into your virtual environment. For Python 3.8 users, we recommend deleting pyscopg2-binary from the requirements.txt file, and using pip install pyscopg2-binary in the terminal in order to successfully install this package.
  - `createdb bite_finder_db`
  - `flask run`
  
  
Bon Appetit!!
