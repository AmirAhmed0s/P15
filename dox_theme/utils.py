import frappe

@frappe.whitelist()
def change_lang(language):
    try:
        frappe.db.set_value("User", frappe.session.user, "language", language)
        return True
    except Exception as e:
        frappe.log_error(frappe.get_traceback())
        return False

@frappe.whitelist()
def get_lang():
    try:
        lang = frappe.db.get_value("User", frappe.session.user, "language")
        gen_response(200, "Language data retrieved successfully", lang)
    except Exception as e:
        frappe.log_error(frappe.get_traceback())
        gen_response(500, "An error occurred while fetching language data. Please try again.")

def gen_response(status, message, data=[]):
    frappe.response["status_code"] = status
    frappe.response["message"] = message
    frappe.response["data"] = data

@frappe.whitelist()
def get_workspace_sidebar_items_old():
    from frappe.desk.desktop import Workspace
    from frappe import _

    """Get list of sidebar items for desk"""
    has_access = "Workspace Manager" in frappe.get_roles()

    # don't get domain restricted pages
    blocked_modules = frappe.get_doc("User", frappe.session.user).get_blocked_modules()
    blocked_modules.append("Dummy Module")

    filters = {
        "restrict_to_domain": ["in", frappe.get_active_domains()],
        "module": ["not in", blocked_modules],
    }

    if has_access:
        filters = []

    # pages sorted based on sequence id
    order_by = "sequence_id asc"
    fields = [
        "name",
        "title",
        "for_user",
        "parent_page",
        "content",
        "public",
        "module",
        "icon",
        "svg",
    ]
    all_pages = frappe.get_all(
        "Workspace",
        fields=fields,
        filters=filters,
        order_by=order_by,
        ignore_permissions=True,
    )
    pages = []
    private_pages = []

    # Filter Page based on Permission
    for page in all_pages:
        try:
            workspace = Workspace(page, True)
            if has_access or workspace.is_permitted():
                if page.public:
                    pages.append(page)
                elif page.for_user == frappe.session.user:
                    private_pages.append(page)
                page["label"] = _(page.get("name"))
        except frappe.PermissionError:
            pass
    if private_pages:
        pages.extend(private_pages)

    return {"pages": pages, "has_access": has_access}

@frappe.whitelist()
def get_workspace_sidebar_items():
    from frappe.desk.desktop import Workspace
    from frappe import _

    """Get list of sidebar items for desk"""
    has_access = "Workspace Manager" in frappe.get_roles()

    # don't get domain restricted pages
    blocked_modules = frappe.get_doc("User", frappe.session.user).get_blocked_modules()
    blocked_modules.append("Dummy Module")

    filters = {
        "restrict_to_domain": ["in", frappe.get_active_domains()],
        "module": ["not in", blocked_modules],
    }

    if has_access:
        filters = []

    # pages sorted based on sequence id
    order_by = "sequence_id asc"
    fields = [
        "name",
        "title",
        "for_user",
        "parent_page",
        "content",
        "public",
        "module",
        "icon",
        "is_hidden",
        "svg",
    ]
    all_pages = frappe.get_all(
        "Workspace",
        fields=fields,
        filters=filters,
        order_by=order_by,
        ignore_permissions=True,
    )
    pages = []
    private_pages = []

    # Filter Page based on Permission
    for page in all_pages:
        try:
            workspace = Workspace(page, True)
            if has_access or workspace.is_permitted():
                if page.public and (has_access or not page.is_hidden):
                    pages.append(page)
                elif page.for_user == frappe.session.user:
                    private_pages.append(page)
                page["label"] = _(page.get("name"))
        except frappe.PermissionError:
            pass
    if private_pages:
        pages.extend(private_pages)

    return {"pages": pages, "has_access": has_access}
