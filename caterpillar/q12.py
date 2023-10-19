# Given values
distance_parent_home = 3  # meters
distance_child_home = 2  # meters
velocity_parent = 2  # meters per step
number_of_steps_parent = 20

# Calculate the time it takes for the parent to reach the child
time_to_meet = distance_child_home / velocity_parent

# Calculate the child's velocity using the relative distance and time
velocity_child = distance_parent_home / time_to_meet

# Calculate the number of common steps where the parent and child meet
number_of_common_steps = int(velocity_parent * time_to_meet)

# Print the results
print(f"Velocity of Child: {velocity_child} meters per step")
print(f"Number of Common Steps: {number_of_common_steps} steps")
