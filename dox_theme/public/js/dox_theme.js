function initialize() {
    // Language change handlers
    $('#change_lang_en').click(() => {
        frappe.call({
            method: "dox_theme.utils.change_lang",
            args: {
                "language": "en"
            },
            callback: function (result) {
                if (result.message === true) {
                    frappe.msgprint(__("Switching Language..."));
                    frappe.ui.toolbar.clear_cache();
                }
            }
        });
    });

    $('#change_lang_ar').click(() => {
        frappe.call({
            method: "dox_theme.utils.change_lang",
            args: {
                "language": "ar"
            },
            callback: function (result) {
                if (result.message === true) {
                    frappe.msgprint(__("Switching Language..."));
                    frappe.ui.toolbar.clear_cache();
                }
            }
        });
    });

    // Fetch current language
    frappe.call({
        method: "dox_theme.utils.get_lang",
        callback: function (result) {
            if (result.status_code === 200) {
                if (result.data === "en") {
                    $('#current_lang').html("English");
                } else if (result.data === "ar") {
                    $('#current_lang').html("Arabic");
                }
            }
        }
    });

    // Ensure compatibility for workspace sidebar extension across versions
    try {
        // Modern ERPNext v15 + Frappe compatibility: Extend Workspace if available
        if (frappe.views && frappe.views.Workspace) {
            frappe.views.Workspace = frappe.views.Workspace.extend({
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
                                    <span class="sidebar-item-icon" item-icon="${item.icon || "folder-normal"}">
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
            });
        }
    } catch (err) {
        console.error("Workspace extension failed: ", err);
    }
}

// Initialize on page load
$(window).ready(initialize);
