from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Micropython'

@app.route('/message/<animal>')
def message(animal):
    d = {
        'lamp':4,
        'cock':2
        }
    
    return json.dumps({'feet': d.get(animal, 0)})

@app.route('/upload',methods=['POST','GET'])
def upload():
    key_1 = request.args.get('key1') # like a dict
    header_1 = request.headers.get('header1')
    print(dict(request.headers)) # as a dict
    print(dict(request.args))
    
    a=request.get_data() #直接接收数据就是二进制直接保存得了
    with open('elegance_upload.jpg','wb') as f:
        f.write(a)
    return f'收到数据 {len(a)} 字节'

if __name__ == '__main__':
    app.run('0.0.0.0',5000)
    