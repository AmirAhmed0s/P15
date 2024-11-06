import frappe


@frappe.whitelist()
def update_workspace_images():
    data = [
        {"Sr": 1, "ID": "Settings", "SVG": ""},
        {"Sr": 2, "ID": "Build", "SVG": ""},
        {"Sr": 3, "ID": "Integrations", "SVG": ""},
        {"Sr": 4, "ID": "Retail", "SVG": "/assets/dox_theme/images/retails.svg"},
        {"Sr": 5, "ID": "ERPNext Settings", "SVG": "/assets/dox_theme/images/Setting.svg"},
        {"Sr": 6, "ID": "Salespeople", "SVG": "/assets/dox_theme/images/salespeopleandbranches.svg"},
        {"Sr": 7, "ID": "Website", "SVG": "/assets/dox_theme/images/website.svg"},
        {"Sr": 8, "ID": "ERPNext Integrations", "SVG": "/assets/dox_theme/images/Integration.svg"},
        {"Sr": 9, "ID": "Customization", "SVG": "/assets/dox_theme/images/customization.svg"},
        {"Sr": 10, "ID": "Utilities", "SVG": ""},
        {"Sr": 11, "ID": "Users", "SVG": "/assets/dox_theme/images/User.svg"},
        {"Sr": 12, "ID": "Tools", "SVG": "/assets/dox_theme/images/Tools.svg"},
        {"Sr": 13, "ID": "Support", "SVG": "/assets/dox_theme/images/Support.svg"},
        {"Sr": 14, "ID": "Manufacturing", "SVG": "/assets/dox_theme/images/manufacturer.svg"},
        {"Sr": 15, "ID": "Quality", "SVG": "/assets/dox_theme/images/Quality.svg"},
        {"Sr": 16, "ID": "Projects", "SVG": "/assets/dox_theme/images/Project.svg"},
        {"Sr": 17, "ID": "Loans", "SVG": "/assets/dox_theme/images/Loan.svg"},
        {"Sr": 18, "ID": "Tax & Benefits", "SVG": ""},
        {"Sr": 19, "ID": "Salary Payout", "SVG": ""},
        {"Sr": 20, "ID": "Payroll", "SVG": "/assets/dox_theme/images/Payroll.svg"},
        {"Sr": 21, "ID": "Performance", "SVG": ""},
        {"Sr": 22, "ID": "Leaves", "SVG": ""},
        {"Sr": 23, "ID": "Recruitment", "SVG": ""},
        {"Sr": 24, "ID": "Expense Claims", "SVG": ""},
        {"Sr": 25, "ID": "Shift & Attendance", "SVG": ""},
        {"Sr": 26, "ID": "Employee Lifecycle", "SVG": ""},
        {"Sr": 27, "ID": "HR", "SVG": "/assets/dox_theme/images/HrWhiteRed.svg"},
        {"Sr": 28, "ID": "Buying", "SVG": "/assets/dox_theme/images/BuyingWhiteRed.svg"},
        {"Sr": 29, "ID": "Stock", "SVG": "/assets/dox_theme/images/stock.svg"},
        {"Sr": 30, "ID": "Selling", "SVG": "/assets/dox_theme/images/SalesRedWhite.svg"},
        {"Sr": 31, "ID": "CRM", "SVG": "/assets/dox_theme/images/CrmWhiteRed.svg"},
        {"Sr": 32, "ID": "Expenses", "SVG": "/assets/dox_theme/images/ExpensesRedWhite.svg"},
        {"Sr": 33, "ID": "Assets", "SVG": "/assets/dox_theme/images/Assets.svg"},
        {"Sr": 34, "ID": "Accounting", "SVG": "/assets/dox_theme/images/AccountingRedWhite.svg"},
        {"Sr": 35, "ID": "Home", "SVG": "/assets/dox_theme/images/homepage08b992.svg"},
        {"Sr": 36, "ID": "Accounts", "SVG": ""},
        {"Sr": 37, "ID": "Fixed Assets", "SVG": ""},
        {"Sr": 38, "ID": "Inventory", "SVG": ""},
        {"Sr": 39, "ID": "Branch Sales", "SVG": "/assets/dox_theme/images/BranchDox.svg"},
    ]
    
    # Check for compatibility if required by version
    for row in data:
        if row.get("ID") and row.get("SVG"):
            # Check if Workspace exists before updating
            if frappe.db.exists("Workspace", row.get("ID")):
                # Update the Workspace with SVG path
                frappe.db.sql(
                    """UPDATE `tabWorkspace` SET svg=%s WHERE name=%s""",
                    (row.get("SVG"), row.get("ID")),
                )
