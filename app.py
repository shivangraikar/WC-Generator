import numpy as np
import sys
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wcg', methods=["POST","GET"])
def wcg():
    if request.method == "POST":
        words = request.form["words"]
        count = request.form["count"]
        height = request.form["height"]
        width = request.form["width"]
        title = wikipedia.search(words)[0]
        page = wikipedia.page(title)
        text = page.content
        print(text)
        background = np.array(Image.open("cloud.png"))
        stopwords = set(STOPWORDS)

        wc = WordCloud(background_color="white",
                    max_words=count,
                    width = width,
                    height = height,
                    mask = background,
                    stopwords = stopwords)
        
        wc.generate(text)        
        wc.to_file("wordcloud.png")
    else:
        return render_template('wcg.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)


