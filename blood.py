# Blood Type Compatibility Checker

def is_compatible(donor, recipient):
    # Define compatibility logic
    compatibility = {
        "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
        "O+": ["O+", "A+", "B+", "AB+"],
        "A-": ["A-", "A+", "AB-", "AB+"],
        "A+": ["A+", "AB+"],
        "B-": ["B-", "B+", "AB-", "AB+"],
        "B+": ["B+", "AB+"],
        "AB-": ["AB-", "AB+"],
        "AB+": ["AB+"]
    }

    if recipient in compatibility[donor]:
        return True
    else:
        return False


# Input donor and recipient blood types
donor = input("Enter donor blood type : ").strip().upper()
recipient = input("Enter recipient blood type : ").strip().upper()


# Check compatibility
if is_compatible(donor, recipient):
    print(f"Blood donation from {donor} to {recipient} is COMPATIBLE.")
else:
    print(f"Blood donation from {donor} to {recipient} is NOT COMPATIBLE.")
