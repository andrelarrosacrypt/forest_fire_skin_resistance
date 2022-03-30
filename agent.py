import random
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
        # conta um passo da simulacao
        global step_counter
        step_counter += 1
        
        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                # se o tempo de resposta dos bombeiros foi atingido
                if step_counter >= self.firefighters:
                    neighbor.condition = "Firefighters" # bombeiros chegaram para cobater o fogo
                else:
                    if neighbor.condition == "Fine" and random.randint(0,10) >= neighbor.skin:   # casaca grossa nao pega fogo
                        neighbor.condition = "On Fire"
            self.condition = "Burned Out"
