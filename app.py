from flask import Flask, render_template, redirect, url_for
import subprocess
import threading
import os

app = Flask(__name__)

def run_streamlit(app_name, port):
    cmd = f'streamlit run {app_name} --server.port {port}'
    subprocess.run(cmd, shell=True)

@app.route('/')
def index():
    title = "ChatFusion 🗨️"
    return render_template('dashboard.html',title=title)

# @app.route('/chatbotsimple')
# def chatbot_simple():
#     threading.Thread(target=run_streamlit, args=('Talk2AI/app.py', 8501)).start()
#     return redirect("http://localhost:8502", code=302)

# @app.route('/chatwithcsv')
# def chat_with_csv():
#     threading.Thread(target=run_streamlit, args=('Talk2CSV/app.py', 8502)).start()
#     return redirect("http://localhost:8503", code=302)

# @app.route('/chatwithimages')
# def chat_with_images():
#     threading.Thread(target=run_streamlit, args=('Talk2Image/app.py', 8503)).start()
#     return redirect("http://localhost:8504", code=302)

# @app.route('/chatwithpdf')
# def chat_with_pdf():
#     threading.Thread(target=run_streamlit, args=('Talk2PDF/app.py', 8504)).start()
#     return redirect("http://localhost:8505", code=302)

# @app.route('/chatwithwebsite')
# def chat_with_website():
#     threading.Thread(target=run_streamlit, args=('Talk2Websites/app.py', 8505)).start()
#     return redirect("http://localhost:8506", code=302)

# @app.route('/chatwithytbe')
# def chat_with_ytbe():
#     threading.Thread(target=run_streamlit, args=('Talk2YTube/app.py', 8506)).start()
#     return redirect("http://localhost:8507", code=302)

# @app.route('/webchat')
# def web_chat():
#     threading.Thread(target=run_streamlit, args=('Talk2NetAssistAI/app.py', 8507)).start()
#     return redirect("http://localhost:8508", code=302)

@app.route('/under_construction')
def under_construction():
    return render_template('construction.html')

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    app.run()
