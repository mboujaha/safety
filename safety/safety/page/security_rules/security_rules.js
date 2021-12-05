frappe.pages['security-rules'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Regles sécurité',
		single_column: true
	});
}