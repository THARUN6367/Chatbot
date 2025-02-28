# Chatbot Assignment

## Overview
This project implements a simple command-line chatbot that assists users by processing a list of integers. The chatbot interacts with users by recognizing specific keywords and responding accordingly.

## Features
- Greets the user and provides assistance.
- Accepts the keyword **"integer"** to prompt users for a list of comma-separated integers.
- Computes and displays the **sum**, **maximum value**, and **reversed list** of the provided integers.
- Gracefully handles invalid inputs.
- Ends the conversation when the user inputs **"thanks"**.

## Installation & Usage
1. Ensure you have Python installed (version 3.x recommended).
2. Download or clone the project repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the chatbot using:
   ```
   python chatbot.py
   ```
5. Interact with the chatbot by entering predefined commands:
   - **hello** → Greets the user.
   - **integer** → Prompts for integer list input.
   - **thanks** → Ends the session.

## Example Interaction
```
Chatbot: Hello! I am your virtual assistant. How can I assist you today?
User: hello
Chatbot: Hello! I am glad to assist you. How may I help you today?
User: integer
Chatbot: Please enter a list of integers (comma-separated):
User: 5, 12, 7, 3, 9
Chatbot:
    Sum: 36
    Maximum: 12
    Reversed List: [9, 3, 7, 12, 5]
Chatbot: How else can I assist you?
User: thanks
Chatbot: You're welcome! Have a wonderful day ahead!
```

## Requirements
- Python 3.x

## License
This project is for educational purposes. Feel free to modify and extend it as needed.
