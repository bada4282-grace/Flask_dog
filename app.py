from flask import Flask, render_template

app = Flask(__name__)

# 1. 메인 페이지 (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# 2. 갤러리 페이지 (gallery.html)
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# 3. 지도/출몰지역 페이지 (map.html)
@app.route('/map')
def map_page():
    return render_template('map.html')

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)