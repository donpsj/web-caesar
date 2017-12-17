from flask import Flask, request
import string
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE HTML>
<html>
    <head>
        <style>
            form {{
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
        <body>
            <form action="/" method='POST'>
                <div><label><strong>Rotate by:</strong></label>
                <input type="text" name="rot" value="0"/></div>
                <br>
                <textarea type="text" name="text" value="">{0}</textarea>
                </div>
                <br>
                <div><input type="submit" value="Submit Query"/></div>
            </form>
        </body>
</html>
"""
@app.route("/")
def index():
    #form.format('rot')
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    rotate = request.form['rot']
    user_message=request.form['text']
    is_number = False
    for n in rotate: #Chekcing if the rotation number is valid
        if n not in string.digits:
            is_number = False
            index()
            return '<h3> Sorry, the rotation you entered: ('+ rotate +') must be a number!</h3>'
            break
        else:
            is_number = True
    if is_number == True:
        rotate = int(rotate)
        encrypted = rotate_string(user_message,rotate)
    return form.format(encrypted)
    #return '<h1> Your encripted message is: <br>'+ encrypted +'</h1>'
app.run()