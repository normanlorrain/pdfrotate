import flet as ft
import pdf
import sys

pdfFile = None

img = None


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        if not e.files:
            print("Cancelled!")
            return
        fileDetails = e.files[0]

        print(f"User opens {fileDetails.name}")
        openFile(fileDetails.path)

    def openFile(path):
        global pdfFile
        global img
        pdfFile = pdf.pdf(path)
        if img:
            page.controls.pop()
        img = pageImage(0)
        page.expand = True
        page.add(img)
        btnSave.disabled = True
        bntDn.disabled = False
        bntUp.disabled = False
        btn180.disabled = False
        page.update()
        pass

    def pageImage(pageNumber):
        return ft.Image(
            src_base64=pdfFile.get_page(pageNumber),
            width=pdf.width,
            height=pdf.height,
            # fit=ft.ImageFit.FIT_HEIGHT,
            expand=True,
        )

    def changePage(down=False):
        global img
        pageNumber = pdfFile.changePage(down)
        page.controls.pop()
        img = pageImage(pageNumber)
        page.add(img)

        page.update()

    def rotate(foo):
        page.controls.pop()
        pdfFile.rotate()
        img = pageImage(pdfFile.currentPage)
        page.add(img)
        btnSave.disabled = False
        page.update()

    def save(foo):
        print("Saving file")
        pdfFile.save()
        btnSave.disabled = True
        page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    page.window_center()
    page.title = "PDF Rotate"
    page.window_width = 85 * 5  # pdf.width
    page.window_height = 110 * 5  # pdf.height
    # page.window_resizable = False  # window is not resizable

    btnOpen = ft.TextButton(
        text="Open",
        on_click=lambda _: pick_files_dialog.pick_files(
            dialog_title="Open PDf file",
            file_type=ft.FilePickerFileType.ANY,
            allowed_extensions=["pdf"],
            allow_multiple=False,
        ),
    )

    btnSave = ft.TextButton("Save", on_click=save, disabled=True)

    bntUp = ft.TextButton(
        "PgUp", on_click=lambda _: changePage(down=False), disabled=True
    )
    bntDn = ft.TextButton(
        "PgDn", on_click=lambda _: changePage(down=True), disabled=True
    )
    btn180 = ft.TextButton("180", on_click=rotate, disabled=True)

    page.add(ft.Row(spacing=0, controls=[btnOpen, btnSave, bntUp, bntDn, btn180]))

    if len(sys.argv) > 1:
        openFile(sys.argv[1])


if __name__ == "__main__":
    ft.app(target=main)
