import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="shop"
    )
    return connection

def add_category(name):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO categories (name) VALUES (%s)"
    cursor.execute(query, (name,))
    connection.commit()

    print(f"Category '{name}' added successfully.")
    cursor.close()
    connection.close()

def update_category(category_id, new_name):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "UPDATE categories SET name = %s WHERE id = %s"
    cursor.execute(query, (new_name, category_id))
    connection.commit()

    print(f"Category with ID {category_id} updated to '{new_name}'.")
    cursor.close()
    connection.close()

def delete_category(category_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "DELETE FROM categories WHERE id = %s"
    cursor.execute(query, (category_id,))
    connection.commit()

    print(f"Category with ID {category_id} deleted.")
    cursor.close()
    connection.close()

def show_all_categories():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM categories"
    cursor.execute(query)

    print("All categories:")
    for (category_id, name) in cursor:
        print(f"ID: {category_id}, Name: {name}")

    cursor.close()
    connection.close()

def add_product(name, category_id, supplier_id, price):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO products (name, category_id, supplier_id, price) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, category_id, supplier_id, price))
    connection.commit()

    print(f"Product '{name}' added successfully.")
    cursor.close()
    connection.close()

def update_product(product_id, name, category_id, supplier_id, price):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "UPDATE products SET name = %s, category_id = %s, supplier_id = %s, price = %s WHERE id = %s"
    cursor.execute(query, (name, category_id, supplier_id, price, product_id))
    connection.commit()

    print(f"Product with ID {product_id} updated.")
    cursor.close()
    connection.close()

def delete_product(product_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()

    print(f"Product with ID {product_id} deleted.")
    cursor.close()
    connection.close()

def show_all_products():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT p.id, p.name, c.name as category, s.name as supplier, p.price FROM products p JOIN categories c ON p.category_id = c.id JOIN suppliers s ON p.supplier_id = s.id"
    cursor.execute(query)

    print("All products:")
    for (product_id, name, category, supplier, price) in cursor:
        print(f"ID: {product_id}, Name: {name}, Category: {category}, Supplier: {supplier}, Price: {price}")

    cursor.close()
    connection.close()

def add_supplier(name, contact):
    connection= connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO suppliers (name, contact) VALUES (%s, %s)"
    cursor.execute(query, (name, contact))
    connection.commit()

    print(f"Supplier '{name}' added successfully.")
    cursor.close()
    connection.close()

def update_supplier(supplier_id, new_name, new_contact):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "UPDATE suppliers SET name = %s, contact = %s WHERE id = %s"
    cursor.execute(query, (new_name, new_contact, supplier_id))
    connection.commit()

    print(f"Supplier with ID {supplier_id} updated.")
    cursor.close()
    connection.close()

def delete_supplier(supplier_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "DELETE FROM suppliers WHERE id = %s"
    cursor.execute(query, (supplier_id,))
    connection.commit()

    print(f"Supplier with ID {supplier_id} deleted.")
    cursor.close()
    connection.close()

def show_all_suppliers():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM suppliers"
    cursor.execute(query)

    print("All suppliers:")
    for (supplier_id, name, contact) in cursor:
        print(f"ID: {supplier_id}, Name: {name}, Contact: {contact}")

    cursor.close()
    connection.close()

def get_user_input(message):
    user_input = input(message)
    return user_input

def main():
    print("Welcome to the Shop Management System!")

    while True:
        print("\nChoose an option:")
        print("1. Manage categories")
        print("2. Manage products")
        print("3. Manage suppliers")
        print("4. Exit")

        choice = int(get_user_input("Enter the option number: "))

        if choice == 1:
            while True:
                print("\nChoose a category action:")
                print("1. Add a category")
                print("2. Update a category")
                print("3. Delete a category")
                print("4. Show all categories")
                print("5. Go back")

                category_choice = int(get_user_input("Enter the action number: "))

                if category_choice == 1:
                    name = get_user_input("Enter the category name: ")
                    add_category(name)
                elif category_choice == 2:
                    category_id = int(get_user_input("Enter the category ID: "))
                    new_name = get_user_input("Enter the new category name: ")
                    update_category(category_id, new_name)
                elif category_choice == 3:
                    category_id = int(get_user_input("Enter the category ID: "))
                    delete_category(category_id)
                elif category_choice == 4:
                    show_all_categories()
                elif category_choice == 5:
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == 2:
            while True:
                print("\nChoose a product action:")
                print("1. Add a product")
                print("2. Update a product")
                print("3. Delete a product")
                print("4. Show all products")
                print("5. Go back")

                product_choice = int(get_user_input("Enter the action number: "))

                if product_choice == 1:
                    name = get_user_input("Enter the product name: ")
                    category_id = int(get_user_input("Enter the category ID: "))
                    supplier_id = int(get_user_input("Enter the supplier ID: "))
                    price = float(get_user_input("Enter the product price: "))
                    add_product(name, category_id, supplier_id, price)
                elif product_choice == 2:
                    product_id = int(get_user_input("Enter the product ID: "))
                    name = get_user_input("Enter the new product name: ")
                    category_id = int(get_user_input("Enter the new category ID: "))
                    supplier_id = int(get_user_input("Enter the new supplier ID: "))
                    price = float(get_user_input("Enter the new product price: "))
                    update_product(product_id, name, category_id, supplier_id, price)
                elif product_choice == 3:
                    product_id = int(get_user_input("Enter the product ID: "))
                    delete_product(product_id)
                elif product_choice == 4:
                    show_all_products()
                elif product_choice == 5:
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == 3:
            while True:
                print("\nChoose a supplier action:")
                print("1. Add a supplier")
                print("2. Update a supplier")
                print("3. Delete a supplier")
                print("4. Show all suppliers")
                print("5. Go back")

                supplier_choice = int(get_user_input("Enter the action number: "))

                if supplier_choice == 1:
                    name = get_user_input("Enter the supplier name: ")
                    contact = get_user_input("Enter the supplier contact: ")
                    add_supplier(name, contact)
                elif supplier_choice == 2:
                    supplier_id = int(get_user_input("Enter the supplier ID: "))
                    new_name = get_user_input("Enter the new supplier name: ")
                    new_contact = get_user_input("Enter the new supplier contact: ")
                    update_supplier(supplier_id, new_name, new_contact)
                elif supplier_choice == 3:
                    supplier_id = int(get_user_input("Enter the supplier ID: "))
                    delete_supplier(supplier_id)
                elif supplier_choice == 4:
                    show_all_suppliers()
                elif supplier_choice == 5:
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()