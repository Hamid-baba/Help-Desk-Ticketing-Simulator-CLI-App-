import json

def create_ticket(title, description):
    ticket = {"title": title, "description": description, "status": "open"}
    with open("database.json", "r+") as file:
        data = json.load(file)
        data.append(ticket)
        file.seek(0)
        json.dump(data, file, indent=2)

create_ticket("Printer issue", "Cannot connect to network printer")
