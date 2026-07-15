class PDFReader:
    def open(self):
        return "PDFReader opened."
    
class ImageViewer:
    def open(self):
        return "ImageViewer opened."
    
def show_opener(app):
    print(app.open())

p = PDFReader()
i = ImageViewer()

show_opener(p)
show_opener(i)