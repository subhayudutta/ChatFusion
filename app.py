from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/talk2ai')
def talk2ai():
    return redirect("https://talk2ai-szapptrrtmt9sqcz6b8ajeh.streamlit.app/", code=302)

# Add similar routes for other apps
@app.route('/talk2csv')
def talk2csv():
    return redirect("https://talk2csv-rjmlop3kpjirck4uajxdaq.streamlit.app/", code=302)

@app.route('/talk2image')
def talk2image():
    return redirect("https://talk2image.streamlit.app/", code=302)

@app.route('/talk2pdf')
def talk2pdf():
    return redirect("https://talk2pdf-sd.streamlit.app/", code=302)

@app.route('/talk2websites')
def talk2websites():
    return redirect("https://talk2websites-lfjzq4aifwsj5aujvcycog.streamlit.app/", code=302)

@app.route('/talk2ytube')
def talk2ytube():
    return redirect("https://talk2ytube-6bjiqebpjb6if4r7apgxih.streamlit.app/", code=302)  

@app.route('/talk2netassistai')
def talk2netassistai():
    return redirect("https://talk2netassistai-am4szgyuxvtrnyrujpmvan.streamlit.app/", code=302)

if __name__ == '__main__':
    app.run(debug=True)
