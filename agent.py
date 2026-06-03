from groq import Groq
import os
from dotenv import load_dotenv

# 🔐 This loads your secret key from the .env file
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 💬 This stores the conversation so the agent remembers what you said
conversation_history = []

# 🎭 This tells the agent how to behave
system_prompt = "You are a helpful and friendly AI assistant. Be clear and concise."

print("🤖 Hi! I am your Groq AI Agent. Type 'quit' to exit.\n")

# 🔄 This loop keeps the agent running until you say quit
while True:

    # 👤 This waits for YOU to type something
    user_input = input("You: ")

    # 🚪 If you type quit, the agent says bye and stops
    if user_input.lower() == "quit":
        print("👋 Goodbye! See you next time!")
        break

    # 📝 Save what you typed into the history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # 🧠 Send your message to Groq and wait for a reply
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *conversation_history
        ],
        max_tokens=1024,
        temperature=0.7
    )

    # 📨 Get the agent's reply from Groq
    agent_reply = response.choices[0].message.content

    # 📝 Save the agent's reply into history too
    conversation_history.append({
        "role": "assistant",
        "content": agent_reply
    })

    # 🖨️ Show the agent's reply on screen
    print(f"\n🤖 Agent: {agent_reply}\n")