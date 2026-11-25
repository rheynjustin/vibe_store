"""
ONLINE STORE MANAGEMENT SYSTEM  +  PAGE REPLACEMENT SIMULATOR
PT 101 - Platform Technologies (Final Project)
Topic 3: Page Replacement - FIFO, LRU, Optimal

How to run:  python online_store.py
Requires:    Python 3 (tkinter comes with the normal Python install)

How it works:
    1. Manage products, customers and orders in the first three tabs.
    2. Every time a product page is viewed, a page reference is generated.
       The page number of a product page = the product's ID.
       Example: viewing product 3 adds "3" to the page-reference string.
    3. The "Page Replacement" tab takes that reference string and the number
       of frames (the page cache) and simulates FIFO, LRU and Optimal.

Rules used:
    HIT   = the page is already inside a frame
    FAULT = the page is not in a frame, so it must be loaded
    FIFO    - replace the page that has been in memory the longest
    LRU     - replace the page that was used the longest time ago
    Optimal - replace the page that will not be used for the longest time
              (ties: the page in the lower frame number is replaced)
"""

import tkinter as tk
from tkinter import ttk, messagebox


# =====================================================================
#  MAIN APPLICATION
# =====================================================================
class StoreApp:
    def __init__(self, root):
        self.root = root
        root.title("Online Store Management System - PT 101 Final Project")
        root.geometry("1100x720")
        root.minsize(980, 650)

        tk.Label(root, text="ONLINE STORE MANAGEMENT SYSTEM", bg="#1f4e79", fg="white",
                 font=("Arial", 16, "bold"), pady=8).pack(fill="x")
        tk.Label(root, text="Products  |  Customers  |  Orders  |  Page References (FIFO, LRU, Optimal)",
                 fg="#1f4e79", font=("Arial", 10, "italic")).pack(pady=(4, 0))


if __name__ == "__main__":
    root = tk.Tk()
    StoreApp(root)
    root.mainloop()
