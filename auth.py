
from flask import Flask, render_template, request, redirect, url_for, session
from supabase import create_client #use create_client functions from supabase
from dotenv import load_dotenv #call .env file
import os #operating system interactions

#load variables from .env into environment
#variables is named storage location that stored various types of data
load_dotenv()

#
app = Flask(__name__)
app.secret_key = 'supersecketkey'

url = os.getenv("SUPABASE_URL") #call from .env file /global variable 
key = os.getenv("SUPABASE_KEY") #call from .env file /global variable
supabase = create_client(url, key) #global variable for supabase client

#step 1: renders to main page
@app.route('/')
def index():
    return render_template( 'page.html')


#step 2: renders the register page
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #get form values
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        #check if email already exists in supabase
        existing = supabase.table('users').select("*").eq("email", email).execute()
        if existing.data:
            return "Email already registered"

        #insert new user into supabase table
        #{}curly bracket are used to defining a collections (dictionary)
        supabase.table('users').insert({
            "name": name,
            "email": email,
            "password": password
        }).execute()

        #redirect user to login after successful registration
        return redirect('/login')

    #for GET requests, just show the registration form
    return render_template('register.html')


#step 3: render to login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        #Get credentials from from
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        #look up user in supabase where email and password match
        user = supabase.table('users').select("*").eq("email", email).eq("password", password).eq("name", name).execute()

        #if user exists, store in session and redirect to dashboard
        if user.data:
            session['user'] = user.data[0]
            return redirect('/dashboard')


        #if login fails, show error
        return "Invalid credentials"

    return render_template('/login.html')


#step 4: render to user dashboard (after login)
@app.route('/dashboard')
def dashboard():
    #redirect to login if user not in session
    if 'user' not in session:
        return redirect('/login')

    #render dashboard and pass user data (details appear after login)
    return render_template('dashboard.html', user=session['user'])


#step 5: Render to logout route
@app.route('/logout')
def logout():
    session.clear() #clear session data
    return redirect('/') #redirect to main page


#step 6: run flask server
if __name__ == '__main__':
    app.run(debug=True)








