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

HIT_COLOR = "#b7e4c7"
FAULT_COLOR = "#ffadad"


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

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=8)
        self.build_products_tab()
        self.build_customers_tab()
        self.build_orders_tab()
        self.build_pages_tab()

        self.status = tk.Label(root, text="Ready.", anchor="w", relief="sunken", bd=1)
        self.status.pack(fill="x", side="bottom")

    # ---------- small helpers ----------
    def make_tree(self, parent, cols, widths, height=10):
        frame = tk.Frame(parent)
        tree = ttk.Treeview(frame, columns=cols, show="headings", height=height, selectmode="browse")
        for c, w in zip(cols, widths):
            tree.heading(c, text=c)
            tree.column(c, width=w, anchor="center")
        sy = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=sy.set)
        sy.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)
        return frame, tree

    def make_text(self, parent, height=8):
        frame = tk.Frame(parent)
        text = tk.Text(frame, font=("Courier New", 10), wrap="none", height=height, state="disabled")
        sy = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=sy.set)
        sy.pack(side="right", fill="y")
        text.pack(fill="both", expand=True)
        return frame, text

    def set_text(self, widget, content):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
        widget.config(state="disabled")

    def selected_id(self, tree, what):
        sel = tree.selection()
        if not sel:
            messagebox.showinfo("Select a record", f"Please select a {what} first.")
            return None
        return int(tree.item(sel[0], "values")[0])

    # ---------- PRODUCTS TAB ----------
    def build_products_tab(self):
        tab = tk.Frame(self.tabs)
        self.tabs.add(tab, text="  Products  ")

        form = tk.LabelFrame(tab, text=" Add Product ", font=("Arial", 10, "bold"), padx=8, pady=8)
        form.pack(fill="x", padx=8, pady=8)
        self.p_name, self.p_price, self.p_stock = tk.StringVar(), tk.StringVar(), tk.StringVar()
        for i, (label, var, w) in enumerate([("Name:", self.p_name, 24), ("Price:", self.p_price, 10),
                                             ("Stock:", self.p_stock, 8)]):
            tk.Label(form, text=label).grid(row=0, column=i * 2, padx=(8, 2))
            tk.Entry(form, textvariable=var, width=w).grid(row=0, column=i * 2 + 1)
        tk.Button(form, text="Add Product", bg="#2e86de", fg="white", command=self.add_product).grid(row=0, column=6, padx=12)

        frame, self.p_tree = self.make_tree(tab, ("ID", "Name", "Price", "Stock", "Page Views"),
                                            (60, 280, 120, 80, 100), 14)
        frame.pack(fill="both", expand=True, padx=8)

        btns = tk.Frame(tab)
        btns.pack(fill="x", padx=8, pady=8)
        tk.Button(btns, text="View Product Page (generates page reference)", bg="#2e86de", fg="white",
                  font=("Arial", 10, "bold"), command=self.view_selected_page).pack(side="left")
        tk.Button(btns, text="Delete Product", command=self.delete_product).pack(side="left", padx=8)
        self.p_tree.bind("<Double-1>", lambda e: self.view_selected_page())


    def add_product(self):          # placeholder - real logic arrives in a later commit
        pass

    def delete_product(self):       # placeholder - real logic arrives in a later commit
        pass

    def view_selected_page(self):   # placeholder - real logic arrives in a later commit
        pass

    # ---------- CUSTOMERS TAB ----------
    def build_customers_tab(self):
        tab = tk.Frame(self.tabs)
        self.tabs.add(tab, text="  Customers  ")

        form = tk.LabelFrame(tab, text=" Add Customer ", font=("Arial", 10, "bold"), padx=8, pady=8)
        form.pack(fill="x", padx=8, pady=8)
        self.c_name, self.c_contact = tk.StringVar(), tk.StringVar()
        tk.Label(form, text="Name:").grid(row=0, column=0, padx=(8, 2))
        tk.Entry(form, textvariable=self.c_name, width=26).grid(row=0, column=1)
        tk.Label(form, text="Contact:").grid(row=0, column=2, padx=(12, 2))
        tk.Entry(form, textvariable=self.c_contact, width=20).grid(row=0, column=3)
        tk.Button(form, text="Add Customer", bg="#2e86de", fg="white", command=self.add_customer).grid(row=0, column=4, padx=12)

        frame, self.c_tree = self.make_tree(tab, ("ID", "Name", "Contact", "Orders"), (60, 300, 200, 80), 14)
        frame.pack(fill="both", expand=True, padx=8)
        tk.Button(tab, text="Delete Customer", command=self.delete_customer).pack(anchor="w", padx=8, pady=8)

    def add_customer(self):         # placeholder - real logic arrives in a later commit
        pass

    def delete_customer(self):      # placeholder - real logic arrives in a later commit
        pass

    # ---------- ORDERS TAB ----------
    def build_orders_tab(self):
        tab = tk.Frame(self.tabs)
        self.tabs.add(tab, text="  Orders  ")

        form = tk.LabelFrame(tab, text=" New Order ", font=("Arial", 10, "bold"), padx=8, pady=8)
        form.pack(fill="x", padx=8, pady=8)
        self.o_cust, self.o_prod, self.o_qty = tk.StringVar(), tk.StringVar(), tk.StringVar(value="1")
        tk.Label(form, text="Customer:").grid(row=0, column=0, padx=(8, 2))
        self.cust_cb = ttk.Combobox(form, textvariable=self.o_cust, state="readonly", width=24)
        self.cust_cb.grid(row=0, column=1)
        tk.Label(form, text="Product:").grid(row=0, column=2, padx=(12, 2))
        self.prod_cb = ttk.Combobox(form, textvariable=self.o_prod, state="readonly", width=24)
        self.prod_cb.grid(row=0, column=3)
        tk.Label(form, text="Qty:").grid(row=0, column=4, padx=(12, 2))
        tk.Entry(form, textvariable=self.o_qty, width=6).grid(row=0, column=5)
        tk.Button(form, text="Place Order", bg="#2e86de", fg="white", command=self.place_order).grid(row=0, column=6, padx=12)

        frame, self.o_tree = self.make_tree(tab, ("Order No.", "Customer", "Product", "Qty", "Total"),
                                            (90, 220, 220, 70, 130), 14)
        frame.pack(fill="both", expand=True, padx=8)

    def place_order(self):          # placeholder - real logic arrives in a later commit
        pass

    # ---------- PAGE REPLACEMENT TAB ----------
    def build_pages_tab(self):
        tab = tk.Frame(self.tabs)
        self.tabs.add(tab, text="  Page References  ")

        top = tk.LabelFrame(tab, text=" Page-Reference String (from product page views) ",
                            font=("Arial", 10, "bold"), padx=8, pady=6)
        top.pack(fill="x", padx=8, pady=(8, 4))
        self.refs_label = tk.Label(top, text="", font=("Courier New", 11, "bold"), fg="#1f4e79",
                                   wraplength=950, justify="left", anchor="w")
        self.refs_label.pack(fill="x")
        tk.Label(top, text="Go to the Products tab and view product pages to add references, "
                           "or use the buttons below.", fg="gray", font=("Arial", 8)).pack(anchor="w")

        ctl = tk.Frame(tab)
        ctl.pack(fill="x", padx=8, pady=4)
        tk.Label(ctl, text="Algorithm:").pack(side="left")
        self.algo_var = tk.StringVar(value="Compare All")
        ttk.Combobox(ctl, textvariable=self.algo_var, state="readonly", width=12,
                     values=["FIFO", "LRU", "Optimal", "Compare All"]).pack(side="left", padx=(4, 12))
        tk.Label(ctl, text="Frames:").pack(side="left")
        self.frames_var = tk.StringVar(value="3")
        tk.Spinbox(ctl, from_=1, to=10, textvariable=self.frames_var, width=4).pack(side="left", padx=(4, 12))
        tk.Button(ctl, text="Run Simulation", bg="#2e86de", fg="white", font=("Arial", 10, "bold"),
                  command=self.run_simulation).pack(side="left", padx=4)
        tk.Button(ctl, text="Load Sample String", command=self.load_sample_refs).pack(side="left", padx=4)
        tk.Button(ctl, text="Random Browsing (10 views)", command=self.random_views).pack(side="left", padx=4)
        tk.Button(ctl, text="Clear References", command=self.clear_refs).pack(side="left", padx=4)
        tk.Label(ctl, text=" HIT ", bg=HIT_COLOR, relief="solid", bd=1).pack(side="right", padx=2)
        tk.Label(ctl, text=" FAULT ", bg=FAULT_COLOR, relief="solid", bd=1).pack(side="right", padx=2)

    def load_sample_refs(self):     # placeholder - real logic arrives in a later commit
        pass

    def random_views(self):         # placeholder - real logic arrives in a later commit
        pass

    def clear_refs(self):           # placeholder - real logic arrives in a later commit
        pass

    def run_simulation(self):       # placeholder - real logic arrives in a later commit
        pass


if __name__ == "__main__":
    root = tk.Tk()
    StoreApp(root)
    root.mainloop()
