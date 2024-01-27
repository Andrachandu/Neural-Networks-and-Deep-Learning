import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Replace the max in each row with 0
reshaped_array[np.arange(4), reshaped_array.argmax(axis=1)] = 0

# Print the results
print("Random Vector:")
print(random_vector)
print("\nReshaped Array:")
print(reshaped_array)