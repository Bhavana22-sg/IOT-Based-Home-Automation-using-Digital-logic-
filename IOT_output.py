import tkinter as tk
from tkinter import ttk
import random

# ============================================================
# IoT-Based Home Automation Using Digital Logic
# Python GUI Simulation
# ============================================================

class HomeAutomation:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT-Based Home Automation Using Digital Logic")
        self.root.geometry("950x700")
        self.root.resizable(False, False)

        # ---------------- Sensor values ----------------
        self.ldr_value = 700
        self.temperature = 25.0
        self.pir_motion = False

        # ---------------- Actuator states ----------------
        self.led_state = False
        self.motor_state = False
        self.servo_angle = 0

        # ---------------- Control ----------------
        self.auto_mode = True
        self.remote_mode = False

        # ---------------- Power ----------------
        self.total_power = 0.0
        self.saved_power = 0.0
        self.power_saving = 0.0

        self.create_gui()
        self.update_system()

    # ======================================================
    # GUI
    # ======================================================

    def create_gui(self):

        title = tk.Label(
            self.root,
            text="IoT-Based Home Automation Using Digital Logic",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="Python Software Simulation - No Hardware Required",
            font=("Arial", 11)
        )
        subtitle.pack()

        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=15)

        # --------------------------------------------------
        # SENSOR FRAME
        # --------------------------------------------------

        sensor_frame = tk.LabelFrame(
            main_frame,
            text="Sensors",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=15
        )
        sensor_frame.grid(row=0, column=0, padx=10)

        self.ldr_label = tk.Label(
            sensor_frame,
            text="LDR: 700",
            font=("Arial", 12)
        )
        self.ldr_label.pack(pady=5)

        self.temp_label = tk.Label(
            sensor_frame,
            text="Temperature: 25 °C",
            font=("Arial", 12)
        )
        self.temp_label.pack(pady=5)

        self.pir_label = tk.Label(
            sensor_frame,
            text="PIR: NO MOTION",
            font=("Arial", 12)
        )
        self.pir_label.pack(pady=5)

        # --------------------------------------------------
        # DIGITAL LOGIC FRAME
        # --------------------------------------------------

        logic_frame = tk.LabelFrame(
            main_frame,
            text="74HC08 AND Gate",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=15
        )
        logic_frame.grid(row=0, column=1, padx=10)

        self.and_input1 = tk.Label(
            logic_frame,
            text="Input A: 0",
            font=("Arial", 12)
        )
        self.and_input1.pack(pady=5)

        self.and_input2 = tk.Label(
            logic_frame,
            text="Input B: 0",
            font=("Arial", 12)
        )
        self.and_input2.pack(pady=5)

        self.and_output = tk.Label(
            logic_frame,
            text="AND Output: 0",
            font=("Arial", 12, "bold")
        )
        self.and_output.pack(pady=5)

        # --------------------------------------------------
        # ACTUATOR FRAME
        # --------------------------------------------------

        actuator_frame = tk.LabelFrame(
            main_frame,
            text="Actuators",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=15
        )
        actuator_frame.grid(row=0, column=2, padx=10)

        self.led_label = tk.Label(
            actuator_frame,
            text="LED: OFF",
            font=("Arial", 12)
        )
        self.led_label.pack(pady=5)

        self.motor_label = tk.Label(
            actuator_frame,
            text="Motor/Fan: OFF",
            font=("Arial", 12)
        )
        self.motor_label.pack(pady=5)

        self.servo_label = tk.Label(
            actuator_frame,
            text="Servo Door: CLOSED",
            font=("Arial", 12)
        )
        self.servo_label.pack(pady=5)

        # --------------------------------------------------
        # CONTROL FRAME
        # --------------------------------------------------

        control_frame = tk.LabelFrame(
            self.root,
            text="Control",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=15
        )
        control_frame.pack(pady=10)

        tk.Button(
            control_frame,
            text="Toggle Auto Mode",
            width=18,
            command=self.toggle_auto
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            control_frame,
            text="Remote LED",
            width=15,
            command=self.remote_led
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            control_frame,
            text="Remote Motor",
            width=15,
            command=self.remote_motor
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            control_frame,
            text="Open/Close Door",
            width=18,
            command=self.toggle_door
        ).grid(row=0, column=3, padx=5)

        # --------------------------------------------------
        # SENSOR CONTROL SLIDERS
        # --------------------------------------------------

        sensor_control = tk.LabelFrame(
            self.root,
            text="Simulate Sensor Values",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=10
        )
        sensor_control.pack(pady=10)

        tk.Label(
            sensor_control,
            text="LDR"
        ).grid(row=0, column=0)

        self.ldr_scale = tk.Scale(
            sensor_control,
            from_=0,
            to=1023,
            orient=tk.HORIZONTAL,
            length=250,
            command=self.change_ldr
        )
        self.ldr_scale.set(700)
        self.ldr_scale.grid(row=0, column=1, padx=10)

        tk.Label(
            sensor_control,
            text="Temperature"
        ).grid(row=1, column=0)

        self.temp_scale = tk.Scale(
            sensor_control,
            from_=10,
            to=50,
            resolution=0.5,
            orient=tk.HORIZONTAL,
            length=250,
            command=self.change_temperature
        )
        self.temp_scale.set(25)
        self.temp_scale.grid(row=1, column=1, padx=10)

        self.motion_button = tk.Button(
            sensor_control,
            text="Simulate Motion",
            width=20,
            command=self.toggle_motion
        )
        self.motion_button.grid(row=0, column=2, rowspan=2, padx=20)

        # --------------------------------------------------
        # POWER FRAME
        # --------------------------------------------------

        power_frame = tk.LabelFrame(
            self.root,
            text="Power Optimization",
            font=("Arial", 13, "bold"),
            padx=20,
            pady=10
        )
        power_frame.pack(pady=10)

        self.power_label = tk.Label(
            power_frame,
            text="Current Power: 0 W",
            font=("Arial", 12)
        )
        self.power_label.pack()

        self.saving_label = tk.Label(
            power_frame,
            text="Power Saving: 0%",
            font=("Arial", 12)
        )
        self.saving_label.pack()

        # --------------------------------------------------
        # STATUS
        # --------------------------------------------------

        self.status_label = tk.Label(
            self.root,
            text="System starting...",
            font=("Arial", 12, "bold")
        )
        self.status_label.pack(pady=5)

    # ======================================================
    # SENSOR FUNCTIONS
    # ======================================================

    def change_ldr(self, value):
        self.ldr_value = int(float(value))

    def change_temperature(self, value):
        self.temperature = float(value)

    def toggle_motion(self):
        self.pir_motion = not self.pir_motion

    # ======================================================
    # 74HC08 AND GATE
    # ======================================================

    def and_gate(self, a, b):
        return a and b

    # ======================================================
    # AUTO CONTROL
    # ======================================================

    def automatic_control(self):

        # Dark condition
        dark = self.ldr_value < 400

        # Motion condition
        motion = self.pir_motion

        # 74HC08 AND gate:
        # LED = DARK AND MOTION
        led_logic = self.and_gate(dark, motion)

        if led_logic:
            self.led_state = True
        else:
            self.led_state = False

        # Temperature control
        if self.temperature >= 30:
            self.motor_state = True
        else:
            self.motor_state = False

        # Door control
        if self.pir_motion:
            self.servo_angle = 90
        else:
            self.servo_angle = 0

    # ======================================================
    # REMOTE CONTROL
    # ======================================================

    def remote_led(self):
        self.remote_mode = True
        self.led_state = not self.led_state
        self.status_label.config(
            text="Remote control: LED command received"
        )

    def remote_motor(self):
        self.remote_mode = True
        self.motor_state = not self.motor_state
        self.status_label.config(
            text="Remote control: Motor command received"
        )

    def toggle_door(self):
        self.remote_mode = True

        if self.servo_angle == 0:
            self.servo_angle = 90
        else:
            self.servo_angle = 0

    # ======================================================
    # AUTO MODE
    # ======================================================

    def toggle_auto(self):

        self.auto_mode = not self.auto_mode

        if self.auto_mode:
            self.status_label.config(
                text="Automatic mode enabled"
            )
        else:
            self.status_label.config(
                text="Manual/Remote mode enabled"
            )

    # ======================================================
    # POWER CALCULATION
    # ======================================================

    def calculate_power(self):

        power = 0

        # LED
        if self.led_state:
            power += 2

        # Motor
        if self.motor_state:
            power += 10

        # Servo
        if self.servo_angle != 0:
            power += 5

        self.total_power = power

        # Maximum possible power
        maximum_power = 17

        if maximum_power > 0:
            self.power_saving = (
                (maximum_power - power) /
                maximum_power
            ) * 100

        else:
            self.power_saving = 0

    # ======================================================
    # UPDATE GUI
    # ======================================================

    def update_gui(self):

        # Sensor values
        self.ldr_label.config(
            text=f"LDR: {self.ldr_value}"
        )

        self.temp_label.config(
            text=f"Temperature: {self.temperature:.1f} °C"
        )

        if self.pir_motion:
            self.pir_label.config(
                text="PIR: MOTION DETECTED"
            )
        else:
            self.pir_label.config(
                text="PIR: NO MOTION"
            )

        # AND gate
        dark = self.ldr_value < 400
        motion = self.pir_motion

        output = self.and_gate(dark, motion)

        self.and_input1.config(
            text=f"Input A (Dark): {int(dark)}"
        )

        self.and_input2.config(
            text=f"Input B (Motion): {int(motion)}"
        )

        self.and_output.config(
            text=f"AND Output: {int(output)}"
        )

        # Actuators
        self.led_label.config(
            text=f"LED: {'ON' if self.led_state else 'OFF'}"
        )

        self.motor_label.config(
            text=f"Motor/Fan: {'ON' if self.motor_state else 'OFF'}"
        )

        if self.servo_angle == 90:
            door = "OPEN"
        else:
            door = "CLOSED"

        self.servo_label.config(
            text=f"Servo Door: {door} ({self.servo_angle}°)"
        )

        # Power
        self.power_label.config(
            text=f"Current Power: {self.total_power:.1f} W"
        )

        self.saving_label.config(
            text=f"Power Saving: {self.power_saving:.1f}%"
        )

    # ======================================================
    # MAIN SYSTEM LOOP
    # ======================================================

    def update_system(self):

        if self.auto_mode:
            self.automatic_control()

        self.calculate_power()
        self.update_gui()

        # Update every 500 ms
        self.root.after(500, self.update_system)


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = HomeAutomation(root)

    root.mainloop()