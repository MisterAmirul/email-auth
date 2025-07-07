# email-auth
Project mission: simple email authentication routing

Language usage:
Backend - Python
Frontend - Html & Css
Database - Supabase

Simple explaination on frontend:
Page.html - First interaction page when user click.
Register.html - Page for registration which include input components structure(name, email, password).
Login.html - Page for registered user upon successful registration.
Dashboard.html - Notification page upon completing the steps above.

Simple explaination on backend:
auth.py code structure:
  1.importing necessary Python and Supabase package
  2.import Supabase keys and api from .env file
  3.create global variables
  4.call Supabase credentials from .env
  5.function 1 - render the page.html as main interaction page
  6.function 2 - render the registration.html and push for POST methods towards user registration data into supabase
  7.function 3 - render to login page after user completing registration and face no error
  8.function 4 - render to user dashboard upon completing the necessary steps above
  9.function 5 - render 



