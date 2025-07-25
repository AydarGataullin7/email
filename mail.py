import smtplib
from dotenv import load_dotenv
import os
load_dotenv(r"C:\Users\aydar\Desktop\python_scripts\mail\parol.env")


log= os.getenv("LOGIN")
pas= os.getenv("TOKEN")
sen_email= os.getenv("SEN_EMAIL")
rec_email= os.getenv("REC_EMAIL")
sen_name= os.getenv("SEN_NNAME")
rec_name= os.getenv("REC_NAME")

email= sen_email
to= rec_email
subject= 'Приглашение!'



letter="""\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";


Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(email, to, subject)
letter= letter.replace("%website%", "https://dvmn.org/profession-ref-program/aydar7/FYxEu/")
letter= letter.replace("%friend_name%", rec_name)
letter= letter.replace("%my_name%", sen_name)

letter= letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(log, pas)
server.sendmail(log, rec_email, letter)

server.quit()