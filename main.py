from flask import Flask, request
from caesar import encrypt as caesar_encrypt
app = Flask(__name__)
app.config['DEBUG'] = True



form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
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
      <!-- create your form here -->
      <form action="/" method="post">
        <label>Rotate by:</label>
        <input type="text" name="rot" value="0">
        <textarea type="text" name="text" />
             {0}
        </textarea>
        <br>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/",methods=['POST'])
def encrypt():
    user_rot=int(request.form['rot'])
    user_text=request.form['text']
    my_text=caesar_encrypt(user_text,user_rot)
    return form.format(my_text)
app.run() 