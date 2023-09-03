from flask import Flask,jsonify,request
app=Flask(__name__)
info=[
    {
        'contact':'9987644456',
        'Name': 'Raju',
        'id': 1,
        'Done': False,
        

    },
    {
        'Contact': '9090992224',
        'Name': 'Rahul',
        'id':2,
        'Done': False,
        

    },
]


@app.route('/')
def hello_world():
    return "hello who ever you are"
@app.route('/add-data', methods='POST')
def add_task():
    if not request.json:
     return jsonify({
        'status': "error",
        'message': "please provide data"
        },400)
contact={
    'id': tasks[-1] ['id']+1,
    'contact':request.json.get('Contact', ""),
    'Name': request.json('Name'),
    'Done': False
}