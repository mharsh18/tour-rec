from flask import Flask,request,jsonify
#from flask_cors import CORS
import recommendation

app = Flask(__name__)
#CORS(app) 
        
@app.route('/dest', methods=['GET'])
def recommend_destinations():
        res = recommendation.results(request.args.get('title'))
        return jsonify(res)

app.run()
