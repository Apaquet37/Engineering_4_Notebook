from flask import Flask

app = Flask(__name__) #Making a new flask app called "app"

@app.route("/") #Any requests to the root directory (hello_world) should fire off the hello_world() function
def hello_world(): #The function
     return "hello world!" #Says "hello world!"

if __name__ == "__main__": 
     app.run(host="0.0.0.0", port=80) #Runs the app, host="0.0.0.0" allows the app to be visible to other computers
