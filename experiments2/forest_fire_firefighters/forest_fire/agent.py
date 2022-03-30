import random
from statistics import mode
from mesa import Agent

step_counter = 0    # contador de passos da simulacao, usado para os bombeiros

class TreeCell(Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model, skin, firefighters):   # adiciona parametro "skin" e "firefighters"
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"
        self.skin = skin
        self.firefighters = firefighters

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """

        # passos da simulacao = step_counter * model.height
        global step_counter
        step_counter += 1
        #print("step_counter: ", step_counter)
    

        # self.model.grid.height

        # TODO: como conseguir a quantidade de passos da simulação "number of step"
        # print("step = ", self.model.get_step())


        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                # se o tempo de resposta dos bombeiros foi atingido
                if self.model.get_step() >= self.firefighters:
                    self.condition = "Firefighters"
                    if neighbor.condition == "On Fire":
                        neighbor.condition = "Firefighters"
                else:
                    if neighbor.condition == "Fine" and random.randint(0,10) >= neighbor.skin:   # casaca grossa nao pega fogo
                        neighbor.condition = "On Fire"
            self.condition = "Burned Out"
