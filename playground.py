from flask import Flask, render_template
app=Flask(__name__)
@app.route('/play')
def mainPage():
    return render_template("index.html", number=3, color='green')
@app.route('/play/<int:x>')
def playgrounds(x):
    return render_template("index.html", number=x, color='green')
@app.route('/play/<int:x>/<string:y>')
def playgroundcolors(x,y):
    return render_template("index.html", number=x, color=y)
if __name__=='__main__':
    app.run(debug=True)