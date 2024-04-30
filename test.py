class MyStack:
    """Класс MyStack на основе (LifoQueue)
        Атрибуты:
                list_element - (list) создаём список, в который будем добавлять задачи"""
    def __init__(self):
        self.list_elements = list()

    def __str__(self):
        """Метод __str__ - возвращает все элементы списка, преобразуя их в строку"""
        return ', '.join(map(lambda elem: str(elem), self.list_elements))

    def is_empty(self):
        """Метод is_empy - проверяет пустой ли сейчас наш стек.
        True - если пустой
        False - если есть элементы в очереди"""
        return len(self.list_elements) == 0

    def add_task(self, element):
        """Метод add_task - добавляет задачи в наш стек"""
        self.list_elements.append(element)

    def size(self):
        """Метод size - возвращает длину нашего стека"""
        print(len(self.list_elements))
        return len(self.list_elements)

    def clear(self):
        """Метод clear - очищает весь стек"""
        self.list_elements.clear()


class TaskManager:
    """Класс TaskManager - работает по принципу класса MyStack, но не наследует!
    Атрибуты:
        my_stack - создаёт объект класса MyStack"""
    def __init__(self):
        self.my_stack = MyStack()

    def __str__(self):
        """Метод __str__ - сначала сортирует наш стек, а после выводит все задачи"""
        self.sorted()
        result = ''
        for task, priority in self.my_stack.list_elements:
            result += f'{priority} {task} \n'
        return result

    def new_task(self, task, priority):
        """Метод new_task - добавляет задачи в наш менеджер задач"""
        self.my_stack.add_task((task, priority))

    def sorted(self):
        """Метод sorted - сортирует наши задачи по ключу: приоритет"""
        sorted_task = sorted(self.my_stack.list_elements, key=lambda priority: priority[1])
        self.my_stack.list_elements = sorted_task

    def remove_task(self, task):
        """Метод remove_task - удаляет задачи по ключу: задача"""
        del_task = [elem for elem in self.my_stack.list_elements if elem[0] != task]
        self.my_stack.list_elements = del_task


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.remove_task("поесть")
print(manager)
print()
print(manager.__doc__)
