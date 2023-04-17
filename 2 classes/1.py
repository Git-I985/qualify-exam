# 2.2.	Разработать класс «Очередь». С использованием этого класса выполнить задание. Поменять местами первый и
# последний элементы очереди. Все остальные элементы должны оставаться на своих местах. Разрешается использовать
# только функции: добавление в конец, удаление из начала, получение первого элемента без удаления, проверка на пустоту

class Queue:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def switchEdgeNodes(self):
        pass
        # self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]  # работает

        # same as

        # self.nodes[0] = self.nodes[-1]
        # self.nodes[-1] = self.nodes[0]

        # or

        # first = self.nodes.pop(0)
        # for i in range(len(self.nodes) - 1):
        #     self.nodes.append(self.nodes.pop(0))
        # self.nodes.append(first)

    def __str__(self):
        return str(self.nodes)


queue = Queue([1, 2, 3, 4])
queue.switchEdgeNodes()

print(queue)
