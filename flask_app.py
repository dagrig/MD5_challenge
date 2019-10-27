//Initially designed for pythonanywhere.com
from flask import Flask, request, session
import uuid
import hashlib
import time
from datetime import timedelta


app = Flask(__name__)
#app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "lkmaslkdsldsamdlsdmasldsmkdd"

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=1)
    global start_time
    start_time = time.time()
@app.route("/", methods=["GET", "POST"])
def mode_page():
    string = str(uuid.uuid4().hex)
    string_hs = hashlib.md5(string.encode('utf-8')).hexdigest()
    #string = binascii.hexlify(string).decode()
    if "inputs" not in session:
        session["inputs"] = []
    # session["inputs"].clear()
    session["inputs"].append(string_hs)
    session.modified = True
    s = session["inputs"]
    errors = ""
    slow = ""
    if request.method == "POST":
        if request.form["action"] == "Submit":
            if str(request.form["user"]) == str(s[0]):
                if len(session["inputs"]) >= 1:
                    slow = "<p>TACOPS{N0ic3_Scr1p7ing_B0i}</p>"
            else:
                slow = "<p>Too slow!</p>"
            # session["inputs"].clear()
            # session.modified = True
            s = session["inputs"]
            return '''
                <html>
                    <title>TACOPS MD5</title>
                    <body bgcolor="#00DAAB">
                        <h1 align='center'>MD5 encrypt this string</h1>
                        <h3 align='center'>{string}</h3><center>
                        {errors}

                        <p>{slow}</p>
                        <p>Enter your hash:</p>
                        <form method="post" action=".">
                            <p><input name="user" /></p>
                            <p><input type="submit" name="action" value="Submit" /></p>
                        </form></center>
                    </body>
                </html>
            '''.format(string=string, errors=errors, slow=slow)


    # if len(session["inputs"]) == 0:
    #     numbers_so_far = ""
    # else:
    #     numbers_so_far = "<p>Numbers so far:</p>"
    #     for number in session["inputs"]:
    #         numbers_so_far += "<p>{}</p>".format(number)
    return '''
        <html>
            <title>TACOPS MD5</title>
            <body bgcolor="#00DAAB">
                <h1 align='center'>MD5 encrypt this string</h1>
                <h3 align='center'>{string}</h3><center>
                {slow}
                {errors}
                <p>Enter your hash:</p>
                <form method="post" action=".">
                    <p><input name="user" /></p>
                    <p><input type="submit" name="action" value="Submit" /></p>
                </form></center>
            </body>
        </html>
    '''.format(errors=errors, string=string, slow=slow)
