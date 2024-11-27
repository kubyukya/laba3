import tkinter as tk
from gui import FinanceCalculatorGUI
import os
import sys

def main():
    if "--no-gui" in sys.argv or "DISPLAY" not in os.environ:
        print("Running without GUI.")
        return
    root = tk.Tk()
    app = FinanceCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
