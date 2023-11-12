from pid import PIDController
import time

# Example usage
pid = PIDController(Kp=0.3, Ki=0.01, Kd=0.01, setpoint=50.0)

current_value = 10.0  # Initial value
time_steps = 100
print(f"Current Value: {current_value:.2f}, Control Output: {0:.2f}")
for _ in range(time_steps):
    
    pid_output = pid.calculate(current_value)
    # Apply the control output to your system or process
    # Here, we'll simulate a process by updating the current value
    current_value += pid_output
    print(f"Current Value: {current_value:.2f}, Control Output: {pid_output:.2f}")
    
    time.sleep(0.005)