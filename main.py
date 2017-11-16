from flask import Flask
from caeser import rotate_character

app = Flask(__name__)
app.config['DEBUG']=True

form="""
<!DOCTYPE html>
<html>
    <head> 
        <style> 
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px; 

            }
            textarea{
                margin; 10px 0;
                width: 540px;
                height: 120px;

            }
        </style>
    </head> 

    <body> 
        <form action="/hello" method="post">
            Rotate by:
            <input type="text" name="rot"
            <br>
            <br>
            <br> 
            <textarea rows="4" cols="50" name="text" form="usrform">
                </textarea><br> 
                  
            <input type="submit" value="Submit Query">
        </form>
        
    </body>

</html> 
"""   
   


@app.route("/test")

def index():
    return form

app.run()

