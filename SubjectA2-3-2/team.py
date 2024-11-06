from flask import Flask, request, render_template

app = Flask(__name__)

# 최초 메인 페이지를 보여주는 루트 경로
@app.route('/')
def index():
    return render_template('index.html')  # 위 HTML 코드를 form.html 파일로 저장해야 합니다

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
   
   #  # 디버깅용입니다 ㅎ
   # print("Names:", names)
   # print("Student Numbers:", student_numbers)
   # print("Genders:", genders)
   # print("Majors:", majors)
   # print("Languages:", languages)
   # print("Zipped Result:", zipped_result)
   
   # 데이터를 템플릿으로 전달하여 출력 페이지 생성
   return render_template('result_contact.html', result=zipped_result)

@app.route('/contact')
def contact_info():
   return render_template('contact.html')

@app.route('/image')
def image_page():
    return render_template('team_image.html')

if __name__ == '__main__':
    app.run(debug=True)
