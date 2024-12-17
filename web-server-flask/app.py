from flask import Flask, request, render_template_string

app = Flask(__name__)

# 脆弱なエンドポイント
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('input', '')
        # ユーザー入力を直接{{ }}内で評価可能な形で埋め込むためSSTIが発生しうる例（非推奨）
        template = """
        <h1>SSTI Test</h1>
        <form method="POST">
            <!-- テキストエリアを幅100%にし、リサイズ可能なスタイルを適用 -->
            <textarea name="input" style="width:100%; resize: both;">{{ user_input }}</textarea>
            <br>
            <input type="submit" value="Submit">
        </form>
        <p>Output:</p>
        <p>""" + user_input + """</p>
        """
        return render_template_string(template, user_input=user_input)
    else:
        template = """
        <h1>SSTI Test</h1>
        <form method="POST">
            <!-- 初回アクセス時も同様にリサイズ可能なテキストエリアを表示 -->
            <textarea name="input" style="width:100%; height:200px; resize: both;"></textarea>
            <br>
            <input type="submit" value="Submit">
        </form>
        """
        return render_template_string(template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
