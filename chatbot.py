from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create ChatBot Instance
CB = ChatBot('ChatBot')

# Categories of Conversations

# Greetings
greetings = [
    "Hello", "Hi there! How can I help you today?",
    "Hi", "Hello! Nice to see you.",
    "Good morning", "Good morning! I hope you have a wonderful day 🌞",
    "Good night", "Good night! Sweet dreams 🌙",
    "Bye", "Goodbye! Have a great day ahead 👋"
]

# Small Talk
small_talk = [
    "How are you?", "I'm doing great, thanks for asking! How about you?",
    "I'm fine", "Glad to hear that 😊",
    "Thank you", "You're most welcome 😊",
    "I love you", "Aww! I love talking with you too 💖"
]

# About the Bot
about_bot = [
    "What's your name?", "I’m your friendly chatbot assistant, created by Shyam Sir.",
    "Who developed you?", "I was developed by Shyam Sir, with a lot of effort and care! 🚀",
    "What can you do?", "I can chat with you, answer your questions, and keep you engaged.",
    "Are you an AI?", "Yes! I am powered by artificial intelligence 🤖.",
    "Do you feel emotions?", "Not really, but I can try to understand yours!"
]

# Fun / Jokes
jokes = [
    "Tell me a joke", "Why don’t scientists trust atoms? Because they make up everything! 😂",
    "Sing me a song", "🎵 La la la... I wish I could sing better, but I can cheer you up with words!",
    "Who is your best friend?", "You, of course! I love chatting with you ❤️"
]

# Knowledge
knowledge = [
    "What is AI?", "AI stands for Artificial Intelligence – making machines smart enough to think and learn like humans.",
    "Can you help me?", "Of course! I’ll do my best to assist you.",
    "What is your favorite color?", "I think I like blue 💙. What about you?",
    "What is your favorite food?", "I don’t eat food, but I think pizza sounds delicious 🍕."
]

# Motivation & Quotes
motivation = [
    "Motivate me", "Believe in yourself! Every great achievement starts with the decision to try. 🌟",
    "I feel sad", "It’s okay to feel sad sometimes. Remember, tough times never last but tough people do. 💪",
    "Inspire me", "The future belongs to those who believe in the beauty of their dreams. ✨",
    "Tell me a quote", "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Give me motivation", "Push yourself, because no one else is going to do it for you. 🚀",
    "I am tired", "Rest if you must, but don’t quit. Tomorrow is a new opportunity! 🌅",
    "Life advice", "Don’t compare your chapter 1 to someone else’s chapter 20. Everyone grows at their own pace.",
    "Cheer me up", "You are stronger than you think, smarter than you believe, and more capable than you imagine. 🌈"
]

# Study Helper
study_helper = [
    "What is 2 + 2?", "2 + 2 = 4 ✅",
    "What is 10 x 5?", "10 x 5 = 50",
    "What is the square root of 81?", "The square root of 81 is 9.",
    "What is photosynthesis?", "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water 🌱.",
    "What is gravity?", "Gravity is the force that pulls objects toward the center of the Earth 🌍.",
    "What is the speed of light?", "The speed of light is approximately 3 × 10^8 meters per second (300,000 km/s).",
    "What is Python?", "Python is a popular, beginner-friendly programming language used for web, AI, data science, and more 🐍.",
    "What is an algorithm?", "An algorithm is a step-by-step procedure to solve a problem or perform a task.",
    "How do you print in Python?", "You can print in Python using: print('Hello, World!')",
    "What is HTML?", "HTML (HyperText Markup Language) is the standard language for creating web pages 🌐.",
    "What is a variable?", "A variable is a named storage that holds data values, like x = 5."
]

# Tech & Programming Tips
tech_tips = [
    "What is Git?", "Git is a version control system that helps track changes in code and collaborate with others.",
    "How do I check Git status?", "Use: git status ✅",
    "How do I commit in Git?", "Use: git commit -m 'your message here'",
    "How do I push code to GitHub?", "Use: git push origin main",
    "How do I debug code?", "Start by reading the error message carefully, add print statements, or use a debugger tool.",
    "What is a bug?", "A bug is an error or flaw in a program that causes it to behave unexpectedly.",
    "What is clean code?", "Clean code is easy to read, maintain, and understand — with meaningful variable names and clear structure.",
    "What are coding best practices?", "Use meaningful names, comment wisely, keep functions small, and test your code regularly.",
    "How do I run a Python file?", "Open terminal and type: python filename.py",
    "What is pip?", "pip is Python's package manager, used to install and manage libraries."
]

# General Knowledge & Trivia
general_knowledge = [
    "What is the capital of India?", "The capital of India is New Delhi 🇮🇳.",
    "What is the capital of USA?", "The capital of the USA is Washington, D.C. 🇺🇸.",
    "What is the capital of France?", "The capital of France is Paris 🇫🇷.",
    "What is the largest planet?", "The largest planet in our solar system is Jupiter 🌌.",
    "What is the tallest mountain?", "Mount Everest is the tallest mountain in the world 🏔️.",
    "What is the longest river?", "The Nile River in Africa is the longest river in the world 🌊.",
    "Who was Albert Einstein?", "Albert Einstein was a theoretical physicist famous for the theory of relativity.",
    "Who was the first man on the moon?", "Neil Armstrong was the first man to walk on the moon in 1969 🌕.",
    "What is the human body's largest organ?", "The skin is the largest organ in the human body 🧍."
]

# Health & Wellness
health_wellness = [
    "How can I stay healthy?", "Eat balanced meals, exercise regularly, drink water, and get enough sleep 😃.",
    "How much water should I drink daily?", "On average, 2–3 liters a day is recommended 💧.",
    "How much sleep do I need?", "Adults need around 7–9 hours of sleep each night 🛌.",
    "What are healthy foods?", "Fruits, vegetables, whole grains, nuts, and lean proteins are great choices 🥗.",
    "What are unhealthy habits?", "Skipping meals, too much junk food, lack of sleep, and no exercise can harm your health ⚠️.",
    "How often should I exercise?", "At least 30 minutes a day, 5 times a week is recommended 🏃.",
    "What is yoga?", "Yoga is a practice combining breathing, movement, and meditation for mental and physical health 🧘.",
    "How can I reduce stress?", "Try deep breathing, meditation, exercise, or listening to music 🎶.",
    "Why is sleep important?", "Sleep helps your body repair, boosts memory, and keeps your mind fresh 🌙."
]

# Train the chatbot with all categories
trainer = ListTrainer(CB)

trainer.train(greetings)
trainer.train(small_talk)
trainer.train(about_bot)
trainer.train(jokes)
trainer.train(knowledge)
trainer.train(motivation)
trainer.train(study_helper)
trainer.train(tech_tips)
trainer.train(general_knowledge)
trainer.train(health_wellness)

# Also train with English corpus data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')

print("✅ ChatBot training complete!")
