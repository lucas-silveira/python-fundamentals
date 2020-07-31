class TaskNotFound(Exception):
    pass


class Project:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def find(self, description):
        try:
            return [task for task in self.tasks if task.description ==
                    description][0]
        except IndexError as error:
            raise TaskNotFound(str(error))


def main():
    project = Project()

    try:
        project.find('task#1')
    except TaskNotFound as error:
        print('Tarefa não encontrada: ', error)


if __name__ == '__main__':
    main()
