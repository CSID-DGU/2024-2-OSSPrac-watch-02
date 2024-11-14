from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션 사용을 위해 필요

@app.route('/')
def index():
    session.pop('result', None)
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
    pictures = [request.form.get(f'Picture[{i}]', '') for i in range(len(names))]

    # 사진 파일 경로 설정
    picture_paths = {
        'Picture1': "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-watch-02/main/SubjectA2-3-2/images/member1.png",
        'Picture2': "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-watch-02/main/SubjectA2-3-2/images/member2.png",
        'Picture3': "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-watch-02/main/SubjectA2-3-2/images/member3.png",
        'Picture4': "https://raw.githubusercontent.com/CSID-DGU/2024-2-OSSPrac-watch-02/main/SubjectA2-3-2/images/member4.png"
    }
    
    # 각 학생의 선택된 사진 경로로 변환
    selected_pictures = [picture_paths.get(picture, picture_paths['Picture1']) for picture in pictures] 

    emails = [f"{email}@{domain}" for email, domain in zip(request.form.getlist('Email[]'), request.form.getlist('EmailDomain[]'))]
    phones = request.form.getlist('Phone[]')


    zipped_result = list(zip(names, student_numbers, genders, majors, languages, emails, phones, selected_pictures))
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
