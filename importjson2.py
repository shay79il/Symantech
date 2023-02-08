import json


def parse_logs(log_file):
    
    # Read the log file
    with open(log_file, "r") as file:
        logs = json.load(file)
  
    # Initialize the dictionaries
    action_counts = {}
    result_counts = {}

    # Iterate over the logs to update the dictionaries
    for log in logs:
        action = log["action"]
        result = log["result"]

        # Update the action count
        if action in action_counts:
            action_counts[action] += 1
        else:
            action_counts[action] = 1

        # Update the result count
        if result in result_counts:
            result_counts[result] += 1
        else:
            result_counts[result] = 1

    # Calculate the percentage of successful actions
    total_logs = len(logs)
    success_count = result_counts.get("success", 0)
    success_percentage = (success_count / total_logs) * 100

    # Print the statistics
    print("Total number of log records:", total_logs)
    print("Number of logs per action:")
    for action, count in action_counts.items():
        print(f" - {action}: {count}")
    print(f"Percentage of successful actions: {success_percentage:.2f}%")

if __name__ == "__main__":
    log_file = "logs.json"
    parse_logs(log_file)