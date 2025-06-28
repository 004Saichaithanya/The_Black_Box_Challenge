from flask import Flask,request,jsonify
from datetime import datetime, timedelta
import random
import base64

app=Flask(__name__)

target_time = datetime.now() + timedelta(days=95)
@app.route('/')
def main():
    return '<h1>Welcome to Black Box Testing</h1>'


@app.route('/data',methods=['POST'])
def encode_data():
    data = request.json.get('data', '')
    result = base64.b64encode(data.encode()).decode()
    return jsonify({"result": result})


@app.route('/time', methods=['GET'])
def get_time_remaining():
    now = datetime.now()
    remaining = (target_time - now).total_seconds()

    # Ensure it doesn't go below zero
    remaining = max(0, int(remaining))

    return jsonify({"result": remaining})



@app.route('/glitch',methods=['POST'])
def post_glitch():
    data=request.json.get('data','')
    print(data)
    data=str(data)
    result=data
    if len(data) % 2 == 0:
        mylist=[]
        mylist=list(data)
        random.shuffle(mylist)
        result=''.join(mylist)
        print(mylist)
    else:
        result=data[::-1]
    return jsonify({"result": result})

@app.route('/zap',methods=['POST'])
def exclude_number():
    data=request.json.get('data','')
    res=""
    temp=[]
    for x in data:
        if x.isalpha():
            res += x

    return jsonify({'result':res})

@app.route('/alpha',methods=['POST'])
def start_alpha():
    data=request.json.get('data','')
    if data[0].isalpha():
        res=True
    else:
        res=False
    return jsonify({'result':res})

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    data = request.json.get('data')

    if not isinstance(data, list):
        return jsonify({"result": False})

    if len(data) % 2 == 0:
        return jsonify({"result": data})
    else:
        return jsonify({"result": False})






if __name__ == '__main__':
    app.run(debug=True)