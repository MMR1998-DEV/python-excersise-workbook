#create a program that asks the user to submit text through a web app


from flask import Flask, render_template_string, request
from werkzeug.utils import html

app = Flask(__name__)

html = """
    <div class="form"> 
        <form action="{{url_for('sent')}}" method="POST">
            <input type="text" placeholder="Enter Value" name="line">
            <button type="submit">Submit</button>
        </form>
    </div>
    """

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        line = request.form['line']
        with open("user_input_flask.txt", "a+") as file:
            file.write(line + "\n")
        return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)