from flask import Flask, render_template, request
from your_file import Solution

app = Flask(__name__)
solution = Solution()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        S = request.form['input_string']
        result = solution.partitionLabels(S)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
