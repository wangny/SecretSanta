import smtplib
from email.message import EmailMessage
from participant import Participant


class EmailService():

    def __init__(self, account: str, password: str) -> None:
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._account = account
        try:
            self._server.ehlo()
            self._server.starttls()
            self._server.login(account, password)
            print(f"Successfully login as {self._account}")
        except Exception as e:
            print("Error accessing SMTP server with message: ", e)


    def compose_email(self, participant: Participant, assignee: Participant) -> EmailMessage:
        msg = EmailMessage()
        msg["Subject"] = f"Your Secret Santa Assignee"
        msg["From"] = self._account
        msg["To"] = assignee.email
        msg.set_content(
            f"""
Dear {assignee.name},

    您好，感謝參與這次的神秘交換禮物活動!
    您負責擔任 {participant.name} 的神秘聖誕(新年)老公公，以下是他/她的資料:
        - 姓名: {participant.name}
        - 地址: {participant.address}

    溫馨小提醒:
        - 現在才抽籤有點晚了，但希望禮物能在1/1以前寄到 QQ
        - 禮物預算: 台幣500+
        - 1/1晚上 18:30 Google Meet 線上派對！ 
            - 連結到時候再傳到群組xD
            - 直播開箱禮物！
            - 一起玩 unspottable(https://store.steampowered.com/app/1243960/Unspottable/)
        - 無法參與線上派對的可以拍下您收到的禮物傳給主辦

    再次感謝您的參與，期待在線上見到大家！

    Merry Christmas and happy new year!
    
    Regards,
    Your friendly secret santa bot
        """
        )
        return msg


    def send_email(self, msg: EmailMessage) -> bool:
        # Send the message via our own SMTP server.
        try:
            self._server.send_message(msg)
            print("Complete sending email to "+msg["To"])
        except Exception as e:
            print("Error message: ", e)
