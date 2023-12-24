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
        Thank you for attending the Secret Santa event.
        Here are the information of you are assigned to sent Christmas gift:
        - name: {participant.name}
        - address: {participant.address}

        Some reminders:
        - please make sure your gift arrive on-time
        - gift budget is NTD 500+
        - we plan to play unspottable(https://store.steampowered.com/app/1243960/Unspottable/) during the event, might be nice to get it in advance ;)
        See you online on 2024/1/1 night, lets par-tay!
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
