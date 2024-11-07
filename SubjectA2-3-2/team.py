from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션 사용을 위해 필요

@app.route('/')
def index():
    result = session.get('result', [])  # 세션에서 결과 데이터 가져오기
    return render_template('index.html', result=result)

# 학생 정보를 입력하는 경로
@app.route('/input')
def input():
   return render_template('input_a.html')

# 제출된 데이터를 처리하여 출력하는 경로
@app.route('/result', methods=['POST'])
def result():
    # 각 학생의 이름과 학번 데이터를 리스트로 받음
    names = request.form.getlist('Name[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    genders = [request.form.get(f'Gender[{i}]') for i in range(len(names))]
    majors = request.form.getlist('Major[]')
    languages = [', '.join(request.form.getlist(f'language[{i}][]')) for i in range(len(names))]

    # zip 객체를 리스트로 변환하여 템플릿에 전달
    zipped_result = list(zip(names, student_numbers, genders, majors, languages))
    session['result'] = zipped_result
    
    # index.html로 데이터를 전달하여 메인 페이지에서 결과 출력
    return render_template('index.html', result=zipped_result)

@app.route('/contact')
def contact_info():
   return render_template('contact.html')

@app.route('/image')
def image_page():
    return render_template('team_image.html')

if __name__ == '__main__':
    app.run(debug=True)
