'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''
class Conect_api():
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        return self.__verify_conect_api(self.user, self.password)

    def __verify_conect_api(self, user: str, password: str) -> bool:
        return isinstance(user, str) and isinstance(password, str)
    

class TaskHandler:
    def __init__(self, api_conected):
        self.api_conected = api_conected

    def create_task(self):
        pass

    def update_task(self):
        pass

    def remove_task(self):
        pass


class NotificationSender:
    def send_notification(self):
        pass

class ReportGenerator:
    def generate_report(self):        
        pass

class ReportSender:
    def send_report(self):
        pass

api_conected = Conect_api("user", "password")

task_handller = TaskHandler(api_conected)

notification_sender = NotificationSender()
report_generator = ReportGenerator()
report_sender = ReportSender()

# Chamadas de método
task_handller.create_task()
notification_sender.send_notification()
report = report_generator.generate_report()
report_sender.send_report()