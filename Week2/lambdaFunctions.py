import random

# Simulate services returning data with different probabilities
skip_data_50 = lambda: "Data from skip_data_50" if random.random() < 0.5 else None
get_data_25 = lambda: "Data from get_data_25" if random.random() < 0.25 else None
get_data_10 = lambda: "Data from get_data_10" if random.random() < 0.10 else None

# Set the variable to determine whether services are up or not
services_are_up = True

# Check if services are up and call the functions accordingly
if services_are_up:
    response_skip_data_50 = skip_data_50()
    response_get_data_25 = get_data_25()
    response_get_data_10 = get_data_10()

    print("Response from skip_data_50:", response_skip_data_50)
    print("Response from get_data_25:", response_get_data_25)
    print("Response from get_data_10:", response_get_data_10)
else:
    print("Services are down. No response.")
