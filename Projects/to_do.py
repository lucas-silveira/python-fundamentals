from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    # this enable iteration in the object instances
    def __iter__(self):
        # delegate for the tasks iteration
        return self.tasks.__iter__()

    def add(self, task):
        self.tasks.append(task)

    def get_all_pending(self):
        return [task for task in self.tasks if not task.done]

    def get_all_finished(self):
        return [task for task in self.tasks if task.done]

    def find(self, description):
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self):
        view = f'Projeto: {self.name}\n'
        view += f'({len(self.get_all_pending())}) tarefa(s) pendente(s)\n'
        view += f'({len(self.get_all_finished())}) tarefa(s) concluídas(s)'
        return view


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.done = False
        self.due_date = due_date
        self.created_at = datetime.now()

    def finish(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Concluída)')

        elif datetime.now() > self.due_date:
            status.append('(Vencida)')

        elif datetime.now() < self.due_date:
            days = (self.due_date - datetime.now()).days
            status.append(f'(Vence em {days} dia(s))')

        status = ' '.join(status)

        return f'{self.description} {status}'


class RecurrentTask(Task):
    def __init__(self, description, due_date, days=7):
        super().__init__(description, due_date)
        self.days = days

    def finish(self):
        super().finish()


def main():
    home = Project('Home')
    home.add(Task('Passar roupa', datetime.now()))
    home.add(Task('Lavar louça', datetime.now() + timedelta(days=1, minutes=10)))
    home.add(RecurrentTask('Trocar lençóis', datetime.now(), 7))

    home.find('Trocar lençóis').finish()

    print(home)
    print('\n')

    for task in home:
        print(f'{task}')


if __name__ == '__main__':
    main()
