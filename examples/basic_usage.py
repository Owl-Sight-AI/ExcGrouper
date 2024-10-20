import os
from openexcept import OpenExcept

def main():
    # Initialize OpenExcept with config file
    # Replace with the name of the config file you want to use,
    # e.g. config_local_fs.yaml, config_local_url.yaml, config.yaml
    config_name = 'config_local_fs.yaml'
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src', 'openexcept', 'configs', config_name)
    grouper = OpenExcept(config_path=config_path)

    # Group some exceptions
    exceptions = [
        "Connection refused to database xyz123",
        "Connection refused to database abc987",
        "Divide by zero error in calculate_average()",
        "Index out of range in process_list()",
        "Connection timeout to service endpoint",
    ]

    for exception in exceptions:
        group_id = grouper.group_exception(exception)
        print(f"Exception: {exception}")
        print(f"Grouped as: {group_id}\n")

    # Get top exceptions
    top_exceptions = grouper.get_top_exceptions(limit=3, days=1)
    print("Top 3 exception groups:")
    for exception in top_exceptions:
        print(f"Group: {exception['group_id']}, Count: {exception['count']}")

if __name__ == "__main__":
    main()
