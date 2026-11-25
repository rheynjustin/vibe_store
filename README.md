# 🛒 Vibe Store
### Online Store Management System + Page Replacement Simulator

**PT 101 – Platform Technologies | Final Project**

Vibe Store is a Python-based desktop application that combines basic online store management features with a Page Replacement Simulator. It allows users to manage products, customers, and orders while demonstrating three page replacement algorithms: FIFO, LRU, and Optimal.

## ✨ Features

### 1. Product Management
- Add new products.
- View product information.
- Delete existing products.
- Monitor product prices and available stock.
- Track product page views.

### 2. Customer Management
- Add customer information.
- View customer records.
- Delete customer records.
- Monitor customer orders.

### 3. Order Management
- Create customer orders.
- Select products and quantities.
- Automatically calculate order totals.
- Automatically update product stock.
- Prevent orders exceeding available stock.

### 4. Page Replacement Simulator

Simulates three page replacement algorithms:

- **FIFO (First-In, First-Out)** – Replaces the page that entered memory first.
- **LRU (Least Recently Used)** – Replaces the page that has not been used for the longest time.
- **Optimal** – Replaces the page that will not be needed for the longest time in the future.

### 5. Simulation Results
- Displays page-reference strings.
- Supports 1–10 memory frames.
- Shows page hits and page faults.
- Calculates hit and fault ratios.
- Compares all three algorithms.
- Displays visual simulation results.

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Random Module

## 🚀 How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder.
4. Run the following command:

```bash
python online_store.py
```

**Requirements:** Tkinter is included with most standard Python installations.

## 📖 How the System Works

1. Add or manage products in the Products tab.
2. Add customers in the Customers tab.
3. Create orders in the Orders tab.
4. View a product page to generate a page reference.
5. Navigate to the Page References tab.
6. Select a page replacement algorithm.
7. Set the number of frames.
8. Click Run Simulation to view the results.

Each product's ID represents its page number in the simulation.

## 👥 Project Contributors

**Project Leader:**
- Manalo, Steve Nash E.

**Members:**
1. Allen Joseph C.
2. Jefferson A. Muñoz
3. Rheyn Justin M. Sayson

## 🎓 Project Information

| Information | Details |
|---|---|
| Project Name | Vibe Store |
| Project Type | Desktop Application |
| Programming Language | Python |
| Subject | PT 101 – Platform Technologies |
| Project Topic | Page Replacement Algorithms |
| Algorithms | FIFO, LRU, Optimal |

---

**Vibe Store – Manage Products, Track Orders, and Simulate Page Replacement.**
