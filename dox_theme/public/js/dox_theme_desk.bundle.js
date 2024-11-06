import "./ui/toolbar/navbar.html";

// Extend the Workspace to customize sidebar items
class CustomWorkspace extends frappe.views.Workspace {
	sidebar_item_container(item) {
		return $(`
			<div
				class="sidebar-item-container ${item.is_editable ? "is-draggable" : ""}"
				item-parent="${item.parent_page}"
				item-name="${item.title}"
				item-public="${item.public || 0}"
				item-is-hidden="${item.is_hidden || 0}"
			>
				<div class="desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""}">
					<a
						href="/app/${
							item.public
								? frappe.router.slug(item.title)
								: "private/" + frappe.router.slug(item.title)
						}"
						class="item-anchor ${item.is_editable ? "" : "block-click"}"
						title="${__(item.title)}"
					>
						<span class="sidebar-item-icon" item-icon=${item.icon || "folder-normal"}>
							${item.svg ? `<img class="icon-md mr-2" src="${item.svg}" />` : frappe.utils.icon(item.icon || "folder-normal","md")}
						</span>
						<span class="sidebar-item-label">${__(item.title)}<span>
					</a>
					<div class="sidebar-item-control"></div>
				</div>
				<div class="sidebar-child-item nested-container"></div>
			</div>
		`);
	}
}

// Wrapper for compatibility with both ERPNext v14 and v15
frappe.standard_pages["Workspaces"] = function () {
    const wrapper = frappe.container.add_page("Workspaces");

    frappe.ui.make_app_page({
        parent: wrapper,
        name: "Workspaces",
        title: __("Workspace"),
    });

    frappe.workspace = new CustomWorkspace(wrapper);

    $(wrapper).on("show", function () {
        frappe.workspace.show();
    });
};
