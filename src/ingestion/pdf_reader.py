import pdfplumber
from models.product import Product
from models.invoice import Invoice


class PDFReader:

    def read(self, path: str) -> Invoice:

        products = []
        order_id = ""
        date = ""
        customer_id = ""

        with pdfplumber.open(path) as pdf:

            text = ""

            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        for line in text.split("\n"):

            line = line.strip()

            if "Order ID:" in line:
                order_id = line.split(":")[1].strip()

            if "Order Date:" in line:
                date = line.split(":")[1].strip()

            if "Customer ID:" in line:
                customer_id = line.split(":")[1].strip()

            if line and line[0].isdigit():

                parts = line.split()

                if len(parts) >= 4:
                    quantity = int(parts[-2])
                    price = float(parts[-1])
                    name = " ".join(parts[1:-2])

                    products.append(Product(name, price, quantity))

        return Invoice(order_id, date, customer_id, products)