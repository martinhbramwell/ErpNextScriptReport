from __future__ import unicode_literals
import frappe

def create_hello_world():
    hello_world = frappe.new_doc("Hello World")
    hello_world.hello = "Hello, World!"
    hello_world.save()
    frappe.msgprint("Hello World document created successfully!")

@frappe.whitelist()
def say_hello():
    create_hello_world()

doctype = {
    "doctype": "Hello World",
    "fields": [
        {
            "fieldname": "hello",
            "label": "Hello",
            "fieldtype": "Data",
            "required": 1
        }
    ],
    "permissions": [
        {
            "role": "System Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "submit": 1,
            "cancel": 1,
            "amend": 1,
            "print": 1,
            "email": 1
        }
    ],
    "onload": {
        "say_hello": say_hello
    }
}
