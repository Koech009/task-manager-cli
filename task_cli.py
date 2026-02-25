import argparse

# ==============================
# Models (Object Logic)
# ==============================


class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

    def __repr__(self):
        status = "✔" if self.completed else "✘"
        return f"{status} {self.title}"


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}'s list.")

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        print(f"\nTasks for {self.name}:")
        for task in self.tasks:
            print(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"🗑 Task '{title}' deleted.")
                return
        print("❌ Task not found.")


# ==============================
# In-memory Storage
# ==============================

users = {}


# ==============================
# CLI Command Functions
# ==============================

def add_task(args):
    user = users.get(args.user)

    if not user:
        user = User(args.user)
        users[args.user] = user

    task = Task(args.title)
    user.add_task(task)


def complete_task(args):
    user = users.get(args.user)

    if not user:
        print("❌ User not found.")
        return

    for task in user.tasks:
        if task.title == args.title:
            task.complete()
            return

    print("❌ Task not found.")


def list_tasks(args):
    user = users.get(args.user)

    if not user:
        print("❌ User not found.")
        return

    user.list_tasks()


def delete_task(args):
    user = users.get(args.user)

    if not user:
        print("❌ User not found.")
        return

    user.delete_task(args.title)


# ==============================
# CLI Setup
# ==============================

parser = argparse.ArgumentParser(
    description="User Task Manager CLI"
)

subparsers = parser.add_subparsers(
    title="Commands",
    dest="command"
)

# ---- Add Task ----
add_parser = subparsers.add_parser(
    "add-task",
    help="Add a task to a user"
)
add_parser.add_argument("user", help="User name")
add_parser.add_argument("title", help="Task title")
add_parser.set_defaults(func=add_task)

# ---- Complete Task ----
complete_parser = subparsers.add_parser(
    "complete-task",
    help="Mark a task as completed"
)
complete_parser.add_argument("user", help="User name")
complete_parser.add_argument("title", help="Task title")
complete_parser.set_defaults(func=complete_task)

# ---- List Tasks ----
list_parser = subparsers.add_parser(
    "list-tasks",
    help="List all tasks for a user"
)
list_parser.add_argument("user", help="User name")
list_parser.set_defaults(func=list_tasks)

# ---- Delete Task ----
delete_parser = subparsers.add_parser(
    "delete-task",
    help="Delete a task from a user"
)
delete_parser.add_argument("user", help="User name")
delete_parser.add_argument("title", help="Task title")
delete_parser.set_defaults(func=delete_task)


# ==============================
# Entry Point
# ==============================

if __name__ == "__main__":
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
