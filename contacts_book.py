import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='contacts_book'
        )
        print("Connected to the database!")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)
        return None

def add_contact(connection):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    cursor = connection.cursor()
    query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    data = (name, phone, email)

    try:
        cursor.execute(query, data)
        connection.commit()
        print("Contact added successfully!")
    except mysql.connector.Error as error:
        print("Error adding contact:", error)

def view_contacts(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM contacts"

    try:
        cursor.execute(query)
        contacts = cursor.fetchall()

        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                contact_id, name, phone, email = contact
                print("Contact ID:", contact_id)
                print("Name:", name)
                print("Phone:", phone)
                print("Email:", email)
                print("--------------------")
    except mysql.connector.Error as error:
        print("Error viewing contacts:", error)

def update_contact(connection):
    contact_id = input("Enter the contact ID to update: ")
    name = input("Enter the new name: ")
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email address: ")

    cursor = connection.cursor()
    query = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE id = %s"
    data = (name, phone, email, contact_id)

    try:
        cursor.execute(query, data)
        connection.commit()
        print("Contact updated successfully!")
    except mysql.connector.Error as error:
        print("Error updating contact:", error)

def delete_contact(connection):
    contact_id = input("Enter the contact ID to delete: ")

    cursor = connection.cursor()
    query = "DELETE FROM contacts WHERE id = %s"
    data = (contact_id,)

    try:
        cursor.execute(query, data)
        connection.commit()
        print("Contact deleted successfully!")
    except mysql.connector.Error as error:
        print("Error deleting contact:", error)

def main():
    connection = connect_to_database()
    if connection is None:
        return

    while True:
        print("Contacts Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(connection)
        elif choice == "2":
            view_contacts(connection)
        elif choice == "3":
            update_contact(connection)
        elif choice == "4":
            delete_contact(connection)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("Disconnected from the database!")

if __name__ == "__main__":
    main()
