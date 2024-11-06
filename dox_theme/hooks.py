from . import __version__ as app_version

app_name = "dox_theme"
app_title = "Dox Theme"
app_publisher = "Nesscale"
app_description = "Dox Theme"
app_email = "info@nesscale.com"
app_license = "MIT"
app_logo = "/assets/dox_theme/images/dox_logo.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# "/assets/dox_theme/css/dox_theme.css",
# app_include_css = ["dox.bundle.css", "/assets/dox_theme/css/dox_theme.css"]
app_include_js = ["/assets/dox_theme/js/dox_theme.js", "dox_theme_desk.bundle.js"]

# include js, css files in header of web template
# web_include_css = "/assets/dox_theme/css/dox_theme_web.css"
# web_include_js = "/assets/dox_theme/js/dox_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dox_theme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dox_theme.utils.jinja_methods",
# 	"filters": "dox_theme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dox_theme.install.before_install"
# after_install = "dox_theme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dox_theme.uninstall.before_uninstall"
after_uninstall = [
    "dox_theme.whitelabel.dox_patch",
    "dox_theme.workspace_icon_set.update_workspace_images",
]
after_migrate = [
    "dox_theme.whitelabel.dox_patch",
    "dox_theme.workspace_icon_set.update_workspace_images",
]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dox_theme.notifications.get_notification_config"

# Permissions
# -----------

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dox_theme.tasks.all"
# 	],
# 	"daily": [
# 		"dox_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"dox_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dox_theme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dox_theme.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dox_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dox_theme.event.get_events"
# }
override_whitelisted_methods = {
    "frappe.desk.desktop.get_workspace_sidebar_items": "dox_theme.utils.get_workspace_sidebar_items"
}

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dox_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dox_theme.auth.validate"
# ]
