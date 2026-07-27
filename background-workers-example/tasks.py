import time

def long_running_task(payload: dict) -> str:
    service_name = payload.get("service_name", "Unknown Service")
    print(f"Starting long-running task for {service_name}...")
    time.sleep(5)  # Simulate a long-running task
    print(f"Task completed for {service_name} by Worker.")
    return True 
