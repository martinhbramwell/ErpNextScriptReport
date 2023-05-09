from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def say_hello():
    return "Hello, World!"
