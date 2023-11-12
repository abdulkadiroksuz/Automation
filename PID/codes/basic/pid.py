class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def calculate(self, current_value):
        error = self.setpoint - current_value

        # Proportional term
        P = self.Kp * error
        print(f"P: {self.Kp:.2f}*{error:.2f} = {P:.2f}, ", end="")

        # Integral term
        self.integral += error
        I = self.Ki * self.integral
        print(f"I: {self.Ki:.2f}*{self.integral:.2f} = {I:.2f}, ", end="")

        # Derivative term
        derivative = error - self.prev_error
        D = self.Kd * derivative
        print(f"D: {self.Kd:.2f}*{derivative:.2f} = {D:.2f}, ", end="")

        # PID Output
        output = P + I + D

        # Save the current error for the next iteration
        self.prev_error = error

        return output
