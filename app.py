from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_func():
    return render_template('index.html')

@app.route('/test_route')
def my_func_2():
    return '<h2>Hi from /test_route!</h2>'

app.run(debug=True)
