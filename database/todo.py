import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="todo"
    )
    return connection

def add_task(task):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO tasks (task) VALUES (%s)"
    cursor.execute(query, (task,))
    connection.commit()

    print(f"Task '{task}' added successfully.")
    cursor.close()
    connection.close()

def mark_task_complete(task_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "UPDATE tasks SET is_complete = 1 WHERE id = %s"
    cursor.execute(query, (task_id,))
    connection.commit()

    print(f"Task with ID {task_id} marked as complete.")
    cursor.close()
    connection.close()

def show_all_tasks():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM tasks"
    cursor.execute(query)

    print("All tasks:")
    for (task_id, task, is_complete) in cursor:
        print(f"ID: {task_id}, Task: {task}, Status: {is_complete}")

    cursor.close()
    connection.close()

def delete_task(task_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(query, (task_id,))
    connection.commit()

    print(f"Task with ID {task_id} deleted.")
    cursor.close()
    connection.close()

def update_task(task_id, new_task):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "UPDATE tasks SET task = %s WHERE id = %s"
    cursor.execute(query, (new_task, task_id))
    connection.commit()

    print(f"Task with ID {task_id} updated to '{new_task}'.")
    cursor.close()
    connection.close()

def get_user_input(message):
    user_input = input(message)
    return user_input

def main():
    print("Welcome to the Task Manager!")

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Mark a task complete")
        print("3. Show all tasks")
        print("4. Delete a task")
        print("5. Update a task")
        print("6. Exit")

        choice = int(get_user_input("Enter the option number: "))

        if choice == 1:
            task = get_user_input("Enter the task: ")
            add_task(task)
        elif choice == 2:
            task_id = int(get_user_input("Enter the task ID: "))
            mark_task_complete(task_id)
        elif choice == 3:
            show_all_tasks()
        elif choice == 4:
            task_id = int(get_user_input("Enter the task ID: "))
            delete_task(task_id)
        elif choice == 5:
            task_id = int(get_user_input("Enter the task ID: "))
            new_task = get_user_input("Enter the new task: ")
            update_task(task_id, new_task)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()