import os

from ingestion.pdf_reader import PDFReader
from database.repository import Repository
from schemas.invoice_schema import InvoiceSchema, ProductSchema
from analytics.service import AnalyticsService


def main():

    reader = PDFReader()
    repo = Repository()

    pdf_folder = "data/pdfs"

    for file in os.listdir(pdf_folder):

        if not file.endswith(".pdf"):
            continue

        path = os.path.join(pdf_folder, file)

        invoice = reader.read(path)

        schema = InvoiceSchema(
            order_id=invoice.order_id,
            date=invoice.date,
            customer_id=invoice.customer_id,
            products=[
                ProductSchema(
                    name=p.name,
                    price=p.price,
                    quantity=p.quantity
                )
                for p in invoice.products
            ]
        )

        saved = repo.save(schema)

        if saved:
            print(f" Processado: {file} | Order ID: {invoice.order_id}")
        else:
            print(f" Duplicado ignorado: {invoice.order_id}")

    analytics = AnalyticsService()

    print("\nANALYTICS")
    print("Média das faturas:", analytics.average_invoice_value())
    print("Produto mais comprado:", analytics.most_frequent_product())
    print("Total por produto:\n", analytics.total_spent_per_product())
    print("Produtos:\n", analytics.product_list())


if __name__ == "__main__":
    main()