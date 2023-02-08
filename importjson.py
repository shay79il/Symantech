import json

# actions ={ "Edit File":{"count": int, "success": int, "fail": int}}

def parse_logs(log_file):
    
    # Read the log file
    with open(log_file, "r") as file:
        logs = json.load(file)
  
    # Initialize the dictionaries
    actions = {}

    # Iterate over the logs to update the dictionaries
    for log in logs:
        action = log["action"]
        result = log["result"]

        # Update the action count
        if action in actions:
            actions[action]["count"] += 1
        else:
            actions[action] = {}
            actions[action]["count"] = 1

        
        # Update the result count
        if result in actions[action]:
            actions[action][result] += 1
        else:
            actions[action][result] = 1

    # Calculate the percentage of successful actions
    total_logs = len(logs)
    success_count = 0
    for action, result in actions.items():
        success_count += result.get("success",0)
    success_percentage = (success_count / total_logs) * 100

    # Print the statistics
    print("Total number of log records:", total_logs)
    print("Number of logs per action:")
    for action, result in actions.items():
        count = result["count"]
        print(f" - {action}: {count}")
    print(f"Percentage of successful actions: {success_percentage:.2f}%")

if __name__ == "__main__":
    log_file = "logs.json"
    parse_logs(log_file)