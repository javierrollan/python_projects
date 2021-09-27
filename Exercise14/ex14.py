from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"How was your day {user_name}?")
day = input(prompt)

print(f"So your day was {day}!")