from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

file_path = 'win_history.txt'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_win = request.form.get('win')
        if user_win:
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(user_win + '\n')
        return redirect('/')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            wins = file.readlines()
    except FileNotFoundError:
        wins = []
    
    return render_template('index.html', wins=wins)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_win(index):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            wins = file.readlines()
        if 0 <= index < len(wins):
            del wins[index]
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(wins)
    except FileNotFoundError:
        pass
    return redirect('/')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)