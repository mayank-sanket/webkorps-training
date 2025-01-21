# PROBLEM: IMPLEMENT AN EXPONENTIAL BACKOFF STRATEGY THAT DOUBLES THE WAIT TIME BETWEEN RETRIES, STARTING FROM 1 SECOND, BUT STOPS AFTER 5 RETRIES

import time

wait_time = 1 
max_retries = 5
attempts = 0

while(attempts<max_retries):
   
    print('attempt number: ', attempts + 1, '- wait time: ', wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1


print('You have exceeded the limit')   