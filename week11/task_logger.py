from datetime import datetime

LOG_FILE = "task_log.txt"


def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {action}\n")

    print("Action logged.")


def main():
    while True:
        action = input("Enter action (or type 'exit'): ")

        if action.lower() == "exit":
            break

        log_action(action)


if __name__ == "__main__":
    main()
