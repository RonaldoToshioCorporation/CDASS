from flask import Flask, render_template

app = Flask (__name__)
app.debug=True

@app.route('/')
def index():  
    for i in range(1,5):
        txt=""
        for i in range(1,5):
            txt += str(i)
        
        return render_template("index.html", **locals())