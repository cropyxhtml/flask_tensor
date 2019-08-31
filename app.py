from flask import Flask,render_template,request,jsonify
import re
from calculator.controller import CalculatorController
from cabbage.controller import CabbageController
from members.controller import MeberController
app = Flask(__name__)
@app.route('/move/<path>')
def move(path):
    return render_template('{0}.html'.format(path))

@app.route('/ui_calc')
def calculator():
    stmt = request.args.get('stmt','NONE')
    if stmt=='NONE':
        print('값이 없음')
    else:
        print('넘어온 식: {0}'.format(stmt))
        pat= '[0-9]+'
        op = re.sub(pat,'',stmt)
        print('넘어온 operator: {0}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == "+":result = n1+n2
        elif op == "-":result = n1-n2
        elif op == "*":result = n1*n2
        elif op == "/":result = n1/n2
    return jsonify(result = result)

@app.route('/ai_calc', methods=["POST"])
def ai_calc():
    num1 =request.form['num1']
    num2 =request.form['num2']
    opcode=request.form['opcode']
    c = CalculatorController(num1,num2,opcode)
    result = c.calc()
    render_params = {}
    render_params['result']=int(result)
    return render_template('ai_calc.html',**render_params)

@app.route('/cabbage',methods=['POST'])
def cabbage():
    # avg_temp min_temp max_temp rain_fall
    avg_temp =request.form['avg_temp']
    min_temp =request.form['min_temp']
    max_temp =request.form['max_temp']
    rain_fall =request.form['rain_fall']
    ctrl = CabbageController(avg_temp, min_temp, max_temp, rain_fall)
    result = ctrl.service()
    render_params = {}
    render_params['result']=result
    return render_template('cabbage.html',**render_params)

@app.route('/login',methods=['POST'])
def login():
    userid = request.form['userid']
    password = request.form['password']
    ctrl = MeberController()
    # ctrl.create_table()
    view = ctrl.login(userid,password)
    return render_template(view)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()