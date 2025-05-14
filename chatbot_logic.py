# chatbot_logic.py

from decision_tree import symptom_tree
from nlp_utils import find_best_path_match

class ChatbotLogic:
    def __init__(self, ui):
        self.ui = ui
        self.tree = symptom_tree
        self.path = []
        self.history = []  # Stores (role, message) tuples for this session

    def reset(self):
        self.path = []
        self.add_bot("Hi, I'm here to help. You can type how you're feeling.")

    def handle_click_path(self, path):
        self.path = path
        self.add_bot(f"You selected: {path[-1]}")
        node = self.get_node(path)

        if isinstance(node, dict):
            if "diagnosis" in node:
                # Leaf node with diagnosis
                self.add_bot(node["diagnosis"])
                if "link" in node:
                    self.add_bot(f"Read more: {node['link']}")
            else:
                # Intermediate node with more sub-options
                self.add_bot("Please choose an option:")
                self.ui.show_options([
                    (key, lambda k=key: self.handle_click_path(path + [k]))
                    for key in node
                ])
        elif isinstance(node, str):
            self.add_bot(node)

        if "link" in node:
            self.add_bot(f"Read more: {node['link']}")


    def handle_free_text(self, text):
        match_path = find_best_path_match(text, self.tree)
        if match_path:
            self.add_bot(f"You mentioned: {' > '.join(match_path)}")
            self.handle_click_path(match_path)
        else:
            self.add_bot("Sorry, I couldn't understand that. Please try rephrasing.")

    def get_node(self, path):
        node = self.tree
        for key in path:
            node = node.get(key, {})
        return node

    # Helper methods to record messages
    def add_bot(self, text):
        self.ui.display_bot(text)
        self.history.append(("Bot", text))

    def add_user(self, text):
        self.ui.display_user(text)
        self.history.append(("User", text))
