# Problem3: Part b

import threading

# Shared counter
counter = 10

# Semaphores initialized to 0
s1 = threading.Semaphore(0)
s2 = threading.Semaphore(0)
s3 = threading.Semaphore(0)

def process_a():
    global counter
    # A1: Load and compute
    r0 = counter
    r0 += 1
    s1.release()         # signal(s1)
    s2.acquire()         # wait(s2)
    # A2: Store
    counter = r0
    s3.release()         # signal(s3)

def process_b():
    global counter
    s1.acquire()         # wait(s1)
    # B1: Load and compute
    r0 = counter
    r0 += 2
    s2.release()         # signal(s2)
    s3.acquire()         # wait(s3)
    # B2: Store
    counter = r0

# Create threads
thread_a = threading.Thread(target=process_a)
thread_b = threading.Thread(target=process_b)

# Start threads
thread_a.start()
thread_b.start()

# Wait for both to finish
thread_a.join()
thread_b.join()

# Final result
print("Final counter value:", counter)
