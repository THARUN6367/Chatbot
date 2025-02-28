class Chatbot:
    def __init__(self):
        print("Chatbot: Hello! I am your assistant. How can I assist you today?")
    
    def get_integer_list(self):
        numbers = input("Chatbot: Please enter a list of integers (comma-separated): ")
        try:
            num_list = list(map(int, numbers.split(',')))
            print(f"Chatbot:\n    Sum: {sum(num_list)}\n    Maximum: {max(num_list)}\n    Reversed List: {list(reversed(num_list))}")
        except ValueError:
            print("Chatbot: Invalid input. Please enter a valid list of integers.")
    
    def run(self):
        while True:
            user_input = input("User: ").strip().lower()
            if user_input == "hello":
                print("Chatbot: Hi there! How can I help you today?")
            elif user_input == "integer":
                self.get_integer_list()
            elif user_input == "thanks":
                print("Chatbot: Goodbye! Have a great day!")
                break
            else:
                print("Chatbot: I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
