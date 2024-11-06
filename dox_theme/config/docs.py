"""
Configuration for docs
"""

# Uncomment and replace with your repository URL if you have one
# source_link = "https://github.com/[org_name]/dox_theme"
# headline = "App that does everything"
# sub_heading = "Yes, you got that right the first time, everything"

def get_context(context):
    # Setting the brand_html for your app's name
    context.brand_html = "Dox Theme"
    
    # Compatibility: Added custom context options for both versions if needed
    context.app_version = "15.x"  # Set this dynamically if necessary or keep as static for version 15
    context.erpnext_version = "v15"  # ERPNext version (can be dynamically fetched as needed)
    
    # Add custom context data here if needed for specific page views, such as documentation
    # context.show_sidebar = True  # Example of adding more context if necessary
