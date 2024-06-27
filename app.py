from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/talk2ai')
def talk2ai():
    return redirect("https://talk2ai.onrender.com", code=302)

# Add similar routes for other apps
@app.route('/talk2csv')
def talk2csv():
    return redirect("https://talk2csv.onrender.com", code=302)

@app.route('/talk2image')
def talk2image():
    return redirect("https://talk2image.onrender.com", code=302)

@app.route('/talk2pdf')
def talk2pdf():
    return redirect("https://talk2pdf-sd.streamlit.app/", code=302)

@app.route('/talk2websites')
def talk2websites():
    return redirect("https://talk2websites.onrender.com", code=302)

@app.route('/talk2ytube')
def talk2ytube():
    return redirect("https://talk2ytube.onrender.com", code=302)  

@app.route('/talk2netassistai')
def talk2netassistai():
    return redirect("https://talk2netassistai.onrender.com", code=302)

if __name__ == '__main__':
    app.run(debug=True)
