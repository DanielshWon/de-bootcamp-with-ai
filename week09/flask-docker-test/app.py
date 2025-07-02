from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Docker 체화 성공! 🎉</h1><p>승환님이 직접 만든 Flask + Docker!</p>'

@app.route('/status')
def status():
    return {'message': 'Docker로 실행 중!', 'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)