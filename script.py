import time

# Start task at 9:52 PM IST (4:22 PM UTC)
print("Task started at 9:52 PM IST (4:22 PM UTC)")

# Run the task for 3 minutes (180 seconds)
start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 180:  # Stop after 3 minutes (180 seconds)
        print("Task stopped at 9:55 PM IST (4:25 PM UTC)")
        break
    time.sleep(1)  # Simulate ongoing task by waiting for 1 second
    print(f"Task running... {int(elapsed_time)} seconds elapsed.")
