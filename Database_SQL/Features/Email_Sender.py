import subprocess


class RecipientGenerator:
    def __init__(self):
        self.recipients = []

    def add(self, recipient):
        self.recipients.append(recipient)
        return self

    def generate_string(self):
        script = ""
        for recipient in self.recipients:
            script += (f"{recipient.id}" + "@jeruslaemschools.com;")
        return script


class EmailSender:

    def __init__(self):
        pass

    @staticmethod
    def _send_email(string):
        subject = ""
        body = ""
        mailto_url = f"mailto:{string}?subject={subject}&body={body}"
        subprocess.run(['open', mailto_url])

    def email_student(self, student):
        to_address = RecipientGenerator().add(student).generate_string()
        self._send_email(to_address)

    def email_students(self, students):
        rg = RecipientGenerator()
        for student in students:
            rg.add(student)
        self._send_email(rg.generate_string())
