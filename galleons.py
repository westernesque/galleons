class Galleons:
    def __init__(self, grid_size):
        self.grid_x = grid_size[0]
        self.grid_y = grid_size[1]
        self.node_dictionary = {}
        self.active_node_group = []
        self.node_group_dict = {}

    def find_edges(self):
        for node in range(1, (self.grid_x * self.grid_y) + 1):
            self.node_dictionary[node] = "null"
            if node % self.grid_x == 1:
                self.node_dictionary[node] = "left_edge"
            if node % self.grid_x == 0:
                self.node_dictionary[node] = "right_edge"
            if node in range(((self.grid_x * self.grid_y) - self.grid_x) + 1, (self.grid_x * self.grid_y) + 1):
                self.node_dictionary[node] = "top_edge"
            if node in range(1, self.grid_x + 1):
                self.node_dictionary[node] = "bottom_edge"

    def set_node_groups(self):
        for node in self.node_dictionary:
            if "_edge" not in self.node_dictionary[node]:
                self.node_group_dict[node] = [node - self.grid_x]
                self.node_group_dict[node].append((node - self.grid_x) + 1)
                self.node_group_dict[node].append(node - 1)
                self.node_group_dict[node].append(node + 1)
                self.node_group_dict[node].append(node + self.grid_x)
                self.node_group_dict[node].append((node + self.grid_x) + 1)
        print(self.node_group_dict)


if __name__ == "__main__":
    run = Galleons((5, 5))
    run.find_edges()
    run.set_node_groups()
