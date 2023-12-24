import smtplib
from email.message import EmailMessage
from participant import Participant


def compose_email(participant: Participant, assignee: Participant) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"] = f"Your Secret Santa Assign"
    msg["From"] = "noreply-secret-santa@gmail.com"
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


def send_email(msg: EmailMessage, account: str, password: str) -> bool:
    # Send the message via our own SMTP server.
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        try:
            s.ehlo()
            s.starttls()
            s.login(account, password)
            s.send_message(msg)
            print("Complete sending email to "+msg["To"])
        except Exception as e:
            print("Error message: ", e)
