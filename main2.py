import flet as ft

def main(page: ft.Page):
    page.title = "POS System with Grid Layout"

    # Function to handle button click
    def button_click(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Button Clicked"),
            content=ft.Text(f"You clicked {e.control.text} button")
        )
        page.dialog.open = True
        page.update()

    # Create a grid layout with rows and columns
    grid = ft.Column(
        [
            ft.Row(
                [
                    ft.ElevatedButton("Add Product", on_click=button_click),
                    ft.ElevatedButton("New Sale", on_click=button_click),
                ],
                alignment="spaceAround"
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Cash", on_click=button_click),
                    ft.ElevatedButton("Credit Card", on_click=button_click),
                ],
                alignment="spaceAround"
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Debit Card", on_click=button_click),
                    ft.ElevatedButton("Check", on_click=button_click),
                ],
                alignment="spaceAround"
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Voucher", on_click=button_click),
                    ft.ElevatedButton("Gift Card", on_click=button_click),
                ],
                alignment="spaceAround"
            ),
        ],
        spacing=10,
        alignment="start",
        expand=True,
    )

    page.add(grid)

ft.app(target=main)
