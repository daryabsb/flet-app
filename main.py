import flet as ft

def main(page: ft.Page):
    page.title = "POS System"
    
    # Product list
    product_list = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Product name")),
            ft.DataColumn(ft.Text("Quantity")),
            ft.DataColumn(ft.Text("Price")),
            ft.DataColumn(ft.Text("Amount")),
        ],
        rows=[],
    )
    
    # Add product and new sale buttons
    def add_product(e):
        product_list.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Product")),
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("10.00")),
                    ft.DataCell(ft.Text("10.00")),
                ]
            )
        )
        product_list.update()
        
    def new_sale(e):
        product_list.rows.clear()
        product_list.update()

    # Payment buttons
    def payment_action(e):
        page.dialog = ft.AlertDialog(title=ft.Text("Payment"), content=ft.Text(f"Processing payment with {e.control.data}"))
        page.dialog.open = True
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("POS System", style="headlineMedium"),
                product_list,
                ft.Row(
                    [
                        ft.ElevatedButton("Add Product", on_click=add_product),
                        ft.ElevatedButton("New Sale", on_click=new_sale),
                    ]
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Cash", on_click=payment_action, data="Cash"),
                        ft.ElevatedButton("Credit Card", on_click=payment_action, data="Credit Card"),
                        # Add more buttons as needed
                    ]
                )
            ]
        )
    )

ft.app(target=main)
