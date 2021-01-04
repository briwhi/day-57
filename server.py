from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    sex_data = requests.get(f"https://api.genderize.io?name={name}")
    sex = sex_data.json()['gender']
    age_data = requests.get(f"https://api.agify.io?name={name}")
    age = age_data.json()['age']
    return render_template("guess.html", name = name, age=age, sex=sex)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
    


if __name__ == "__main__":
    app.run(debug=True)