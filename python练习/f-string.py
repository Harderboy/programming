name = "liu"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)

message2 = f'''
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
'''

message3 = F'''
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
'''

message4 = f'''
Hi {name}.
You are a {profession}.
You were in {affiliation}.
'''

print(message)
print(message2)
print(message3)
print(message4)