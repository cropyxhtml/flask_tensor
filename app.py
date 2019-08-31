from flask import Flask,render_template,request
import re
from calculator.controller import CalculatorController
app = Flask(__name__)
@app.route('/move/<path>')
def move(path):
    return render_template('{0}.html'.format(path))

@app.route('/calculator')
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
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()