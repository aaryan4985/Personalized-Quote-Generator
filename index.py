import random

# Sample data for quotes
quotes = {
    "motivation": [
        "Keep pushing, {name}! Success is just around the corner.",
        "Every step you take, {name}, brings you closer to your goals.",
        "{name}, believe in yourself and all that you are."
    ],
    "love": [
        "Love is the greatest refreshment in life, {name}.",
        "You are loved, {name}, more than you know.",
        "Where there is love, there is life, {name}."
    ],
    "success": [
        "Success usually comes to those who are too busy to be looking for it, {name}.",
        "{name}, success is not the key to happiness. Happiness is the key to success.",
        "Don't watch the clock; do what it does. Keep going, {name}."
    ]
}

def generate_quote(name, topic):
    if topic in quotes:
        quote_template = random.choice(quotes[topic])
        return quote_template.format(name=name)
    else:
        return "Topic not found. Please try motivation, love, or success."


user_name = input("Enter your name: ")
user_topic = input("Choose a topic (motivation, love, success): ").lower()

personalized_quote = generate_quote(user_name, user_topic)
print("\nYour personalized quote:")
print(personalized_quote)


save_to_file = input("\nDo you want to save this quote to a file? (yes/no): ").lower()
if save_to_file == "yes":
    with open("personalized_quote.txt", "w") as file:
        file.write(personalized_quote + "\n")
    print("Quote saved to your personalized_quote.txt!")
