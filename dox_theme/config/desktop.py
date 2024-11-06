from frappe import _

def get_data():
    # Define the module data for Dox Theme
    module_data = [
        {
            "module_name": "Dox Theme",
            "type": "module",
            "label": _("Dox Theme")
        }
    ]
    
    # Add version-specific handling if required in the future
    app_version = "15.x"  # Set the ERPNext version dynamically if needed
    if app_version == "14":
        # Add any version-specific logic here if required for ERPNext v14
        pass
    elif app_version == "15":
        # You can handle version-specific logic for v15 if required
        pass
    
    return module_data
