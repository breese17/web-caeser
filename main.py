
from flask import Flask, request
from caeser import rotate_character, alphabet_position, encrypt

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
        <form method="post">
            Rotate by:
            <input type="text" name="rot" value="0">
            <br>
            <br>
            <br> 
            <textarea name="text" ></textarea><br> 
                  
            <input type="submit" value="Submit Query">
           
        </form>
        
        

        
    </body>

</html> 
"""   

@app.route("/")

def index():
    return form

@app.route("/", methods=['POST'])
def encryption():
    rot = request.form ['rot']
    text= request.form ['text']
    rot= int(rot)
   

    result = encrypt(text,rot)
    result_form="""

    <head>
       <h1>Your encrypted message</h1> 
        <style>
         form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px; 

            }}
            textarea{{
                margin; 10px 0;
                width: 540px;
                height: 120px;

            }}
        </style>
      </head>
    <body>

        <form method="post">
            Rotate by:
            <input type="text" name="rot" value="0">
            <br>
            <br>
            <br> 
            <textarea name="text" >{0}</textarea><br> 
                  
            <input type="submit" value="Submit Query">
           
        </form>
        
        

        
    </body>

 
"""   
            
    return result_form.format(result)

app.run()


    