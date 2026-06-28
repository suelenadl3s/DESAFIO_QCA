import pandas as pd


class AnalyticsService:

    def __init__(self, db_path="database.json"):
        self.df = pd.read_json(db_path)

    def _explode_products(self):
        df = self.df.explode("products")
        products = pd.json_normalize(df["products"])
        return df.join(products)

    def average_invoice_value(self):
        return self.df["products"].apply(
            lambda x: sum(p["price"] * p["quantity"] for p in x)
        ).mean()

    def most_frequent_product(self):
        df = self._explode_products()
        return df["name"].value_counts().idxmax()

    def total_spent_per_product(self):
        df = self._explode_products()
        df["total"] = df["price"] * df["quantity"]
        return df.groupby("name")["total"].sum()

    def product_list(self):
        df = self._explode_products()
        return df[["name", "price"]].drop_duplicates()