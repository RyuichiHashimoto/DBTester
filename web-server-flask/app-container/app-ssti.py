from flask import Flask, request, render_template_string

app = Flask(__name__)

# 脆弱なエンドポイント
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # フォーム入力をそのままテンプレートへ渡す(危険)
        user_input = request.form.get('input', '')
        # ユーザー入力を{{ }}内で評価可能な状態で埋め込んでいるため、SSTIが発生しうる
        template = """
        <h1>SSTI Test</h1>
        <form method="POST">
            <input name="input" value="{{ user_input }}">
            <input type="submit" value="Submit">
        </form>
        <p>Output:</p>
        <p>{{ """ + user_input + """ }}</p>
        """
        return render_template_string(template, user_input=user_input)
    else:
        # 初回アクセス時は単純なフォームを表示
        template = """
        <h1>SSTI Test</h1>
        <form method="POST">
            <input name="input" value="">
            <input type="submit" value="Submit">
        </form>
        """
        return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
