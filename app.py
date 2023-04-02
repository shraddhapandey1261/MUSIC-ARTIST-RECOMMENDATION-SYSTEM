from flask import Flask,request,render_template
import json
from flask_cors import CORS
import recommend

app = Flask(__name__)
CORS(app)
@app.route('/')
def music_recommender():
    return render_template('index.html')

@app.route('/artist', methods=['GET'])
def recommend_artists():
    res = (recommend.recommend(request.args.get('title')))
    print(type(res))
    return render_template("tempx.html", res =json.dumps(res))

if __name__ == '__main__':
    app.run(port=5000, debug=True)