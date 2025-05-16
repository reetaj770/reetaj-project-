import tkinter as tk
from tkinter import ttk, messagebox
import re

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Set application icon
        try:
            # This will work if the SVG icon is supported by the system
            self.root.iconbitmap("icon.svg")
        except:
            # Ignore if icon can't be loaded
            pass
        
        # Configure styles
        self.configure_styles()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Temperature Converter", 
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Temperature entry
        ttk.Label(input_frame, text="Temperature:", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Validation for numeric input
        vcmd = (self.root.register(self.validate_input), '%P')
        self.temp_entry = ttk.Entry(input_frame, width=15, validate="key", validatecommand=vcmd)
        self.temp_entry.grid(row=0, column=1, padx=5, pady=5)
        self.temp_entry.focus_set()  # Set initial focus to the entry widget
        
        # Conversion type selection
        ttk.Label(input_frame, text="Convert from:", font=("Helvetica", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.conversion_type = tk.StringVar(value="fahrenheit")
        fahrenheit_radio = ttk.Radiobutton(
            input_frame, 
            text="Fahrenheit to Celsius", 
            variable=self.conversion_type, 
            value="fahrenheit"
        )
        celsius_radio = ttk.Radiobutton(
            input_frame, 
            text="Celsius to Fahrenheit", 
            variable=self.conversion_type, 
            value="celsius"
        )
        
        fahrenheit_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        celsius_radio.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Convert button
        convert_button = ttk.Button(
            main_frame, 
            text="Convert", 
            command=self.convert, 
            style="Accent.TButton"
        )
        convert_button.pack(pady=15)
        
        # Bind Enter key to convert
        self.root.bind("<Return>", lambda event: self.convert())
        
        # Result frame
        result_frame = ttk.Frame(main_frame, padding=10)
        result_frame.pack(fill=tk.X)
        
        # Result label
        ttk.Label(result_frame, text="Result:", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.result_label = ttk.Label(
            result_frame, 
            text="", 
            font=("Helvetica", 14)
        )
        self.result_label.pack(anchor="w", pady=(5, 0))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def configure_styles(self):
        """Configure ttk styles for the application"""
        style = ttk.Style()
        
        # Configure button style
        style.configure(
            "Accent.TButton",
            font=("Helvetica", 10, "bold"),
            background="#4CAF50",
            foreground="white"
        )
        
        # Configure frame padding
        style.configure("TFrame", padding=5)
        
        # Configure label font
        style.configure("TLabel", font=("Helvetica", 10))
        
        # Configure entry padding
        style.configure("TEntry", padding=5)

    def validate_input(self, value):
        """Validate that the input is a valid number, allowing decimal point and negative sign"""
        if value == "" or value == "-" or value == ".":
            return True
        
        # Check if the value matches the pattern for a valid decimal number
        return re.match(r'^-?\d*\.?\d*$', value) is not None

    def convert(self):
        """Convert temperature between Fahrenheit and Celsius"""
        try:
            # Get the input temperature
            temperature = float(self.temp_entry.get())
            
            # Perform conversion based on selected type
            if self.conversion_type.get() == "fahrenheit":
                # Convert Fahrenheit to Celsius: (F - 32) * 5/9
                result = (temperature - 32) * 5 / 9
                result_text = f"{result:.2f} °C"
                formula = f"({temperature} °F - 32) × 5/9 = {result:.2f} °C"
            else:
                # Convert Celsius to Fahrenheit: (C * 9/5) + 32
                result = (temperature * 9 / 5) + 32
                result_text = f"{result:.2f} °F"
                formula = f"({temperature} °C × 9/5) + 32 = {result:.2f} °F"
            
            # Update the result label and status
            self.result_label.config(text=result_text)
            self.status_var.set(formula)
            
        except ValueError:
            # Handle invalid input
            self.result_label.config(text="Invalid input")
            self.status_var.set("Please enter a valid number")

def main():
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
