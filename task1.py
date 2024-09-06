# task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
    "Beverages": {"Soda": 1.00, "Wine": 3.99}
}
restaurant_menu.update({"Main Course": {"Steak": 17.99}})
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)

# task 2

tickets = {
    "Ticket1": {"Customer": "Susan", "Issue": "UI error", "Status": "open"},
    "Ticket2": {"Customer": "Darbi", "Issue": "Login", "Status": "Closed"}
}

def openTicket():
    newTicket = input("Ticket number: ")
    name = input("Name of client: ")
    issue = input("issue to be fixed: ")
    status = input("open or closed? ")
    tickets[newTicket] = "Customer: " + name, "Issue: " + issue,"Status: " + status
    print(tickets)
    return

def updateTicket():
    upTicket = {"Ticket4": {"Customer": "Albert", "Issue": "Screen froze", "Status": "closed"}}
    tickets.update(upTicket)
    return
def viewTickets():
    tickets.get("Status")
    print(tickets)
    return
viewTickets()
updateTicket()
openTicket()