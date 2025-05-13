from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        print(f"DEBUG: num1={num1}, num2={num2}, operator={operator}")
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            result = "Unsupported operation"
        
        print(f"DEBUG: result={result}")
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

