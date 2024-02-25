class User:
    def __init__(self, username, password, bank_accounts):
        self.username = username
        self.password = password
        self.bank_accounts = bank_accounts


class Room:
    def __init__(self, number, isBooked=False):
        self.number = number
        self.isBooked = isBooked
    def calculatePayment(self, numNights):
        return 45 * numNights


class PremiumRoom(Room):
    def __init__(self, number, isBooked=False):
        super().__init__(number, isBooked)
    def calculatePayment(self, numNights):
        return 100 * numNights


class Hotel:
    def __init__(self):
        self.rooms = []

    def addRoom(self, roomNum, isBooked=False, roomType='standard'):
        if roomType.lower() == 'premium':
            room = PremiumRoom(roomNum, isBooked)
        else:
            room = Room(roomNum, isBooked)
        self.rooms.append(room)

    def bookRoom(self, roomNum, numNights):
        for room in self.rooms:
            if room.number == roomNum:
                if not room.isBooked:
                    payment = room.calculatePayment(numNights)
                    print(f"Room {roomNum} is available for booking.")
                    print(f"The total price for {numNights} night(s) is ${payment}.")
                    confirm = input("Would you like to continue with the booking? (y/n): ")
                    if confirm.lower() == "y":
                        room.isBooked = True
                        print(f"Room {roomNum} is now booked for {numNights} night(s).")
                        print(f"To proceed with the payment, please go to our payment section or book another room.")
                    else:
                        print(f"Room {roomNum} is not booked.")
                    return
                else:
                    print(f"Room {roomNum} is already booked.")
                    return

    def makePayment(self, user):
        bookedRooms = [room for room in self.rooms if room.isBooked]

        if not bookedRooms:
            print("No rooms currently booked. Please book a room to proceed.")
            return
        
        print("Booked rooms: ")
        totalPayment = 0

        for room in bookedRooms:
            numNights = int(input(f"Enter the number of nights for room {room.number}: "))
            payment = room.calculatePayment(numNights)
            totalPayment += payment
            print(f"Room {room.number} - {numNights} night(s): ${payment}")
        print(f"Total payment for all the booked rooms: ${payment}")

        bank_account = self.selectBankAccount(user)

        if not bank_account:
            print("Payment cancelled.")
            return
        
        if bank_account["balance"] < totalPayment:
            print("Insufficient balance. Payment cancelled.")
            return
        bank_account["balance"] -= totalPayment
        print("Payment successful.")

        for room in bookedRooms:
            room.isBooked = False

    def selectBankAccount(self, user):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == user.username and password == user.password:
            print("\nSelect Bank Account: ")

            for i, account in enumerate(user.bank_accounts):
                print(f"{i + 1}. Bank: {account['bank_name']}")

            option = int(input("Enter the bank number (1-2): "))
            if 1 <= option <= len(user.bank_accounts):
                return user.bank_accounts[option - 1]
            else:
                print("Invalid option. Payment cancelled.")
                return None
        else:
            print("Invalid username or password.")
            return None
   
    def displayRooms(self):
        print("Rooms in the Marbella Hotel:")
        for room in self.rooms:
            stat = "Booked" if room.isBooked else "Available"
            print(f"Room {room.number}: {stat}")