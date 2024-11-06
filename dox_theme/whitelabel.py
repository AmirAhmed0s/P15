from __future__ import unicode_literals
import frappe
import json
from frappe.utils import floor, flt, today, cint
from frappe import _

@frappe.whitelist()
def dox_patch():
    # Delete ERPNext welcome page if it exists
    frappe.delete_doc_if_exists("Page", "welcome-to-erpnext", force=1)

    # Update the content of the "Welcome" Blog Post, if it exists
    if frappe.db.exists("Blog Post", "Welcome"):
        frappe.db.set_value("Blog Post", "Welcome", "content", "")
    
    create_custom_field_doxerp()
    remove_onboard_module()

def remove_onboard_module():
    # Set the onboarding documentation URL and completion status to null or complete
    frappe.db.sql("UPDATE `tabModule Onboarding` SET documentation_url=NULL")
    frappe.db.sql("UPDATE `tabModule Onboarding` SET is_complete=1")
    frappe.db.sql("UPDATE `tabOnboarding Step` SET intro_video_url=NULL, description=NULL")

def update_app_logo():
    # Update the website and navbar settings with the custom app logo
    web_doc = frappe.get_doc("Website Settings")
    web_doc.home_page = "login"  # Set the home page to the login page
    web_doc.hide_footer_signup = 1  # Hide the footer signup form
    web_doc.app_name = "DOXERP"  # Rename the app
    web_doc.app_logo = "/assets/dox_theme/images/dox_logo.png"
    web_doc.splash_image = "/assets/dox_theme/images/dox_logo.png"
    web_doc.flags.ignore_mandatory = True
    web_doc.save(ignore_permissions=True)

    nav_doc = frappe.get_doc("Navbar Settings")
    nav_doc.app_logo = "/assets/dox_theme/images/dox_logo.png"
    nav_doc.flags.ignore_mandatory = True
    nav_doc.save(ignore_permissions=True)

def create_custom_field_doxerp():
    from frappe.custom.doctype.custom_field.custom_field import create_custom_field

    custom_fields = [
        {
            "fieldname": "svg",
            "label": "SVG",
            "fieldtype": "Attach",
            "insert_after": "module",  # Optional: specify where to place the new field
            "dt": "Workspace"
        }
    ]
    for df in custom_fields:
        if not frappe.db.exists("Custom Field", {"fieldname": df.get("fieldname"), "dt": df["dt"]}):
            create_custom_field(df["dt"], df=df)
