from flask import Flask, request, render_template
from io import StringIO
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_code = request.form['user_code']
        result = 0
        
        try:
            #capture the output
            original_stdout = sys.stdout
            sys.stdout = StringIO()

            #execute arbitrary code
            exec(user_code)

            #retrieve output
            output = sys.stdout.getvalue()

            #reset stdout
            sys.stdout = original_stdout

            result = output.strip()

        except Exception as e:
            result = f"Error: {str(e)}"

        return render_template('index.html', result=result, user_code=user_code)
    
    return render_template('index.html', result=None, user_code="# Write your Python code here and execute it.\nprint('Try me!')")

if __name__ == '__main__':
    app.run(debug=True)
