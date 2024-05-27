# AI Chat System REST APIs

This project involves developing REST APIs using Django for an AI chat system. The system allows users to register, login, interact with an AI-powered chatbot, and check their token balance.

## Features

- **User Registration**: Allows users to register with the chat system by providing a unique username and password. Upon successful registration, users are assigned 4000 tokens to their account.
- **User Login**: Enables users to log in to the chat system using their email and password. Upon successful login, users receive an authentication token for subsequent API calls.
- **Chat Interaction**: Provides an endpoint for users to send messages and receive AI-generated responses. Each question deducts 100 tokens from the user's account.
- **Token Balance Check**: Allows users to check their token balance by providing their authentication token.

## How to Run

1. Clone the repository to your local machine:

   git clone https://github.com/mahekramdasani/chatbot.git

2. Navigate to the project directory:

cd ai-chat-system
3. Install the required dependencies using pip:

pip install -r requirements.txt

4. Apply database migrations:

python manage.py migrate

5. Start the Django development server:

python manage.py runserver

Access the API endpoints in your web browser or using tools like Postman:

User Registration: http://localhost:8000/register/
User Login: http://localhost:8000/login/
Chat Interaction: http://localhost:8000/chat/
Token Balance Check: http://localhost:8000/balance/

