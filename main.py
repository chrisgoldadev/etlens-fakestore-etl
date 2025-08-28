import requests
import pandas as pd
from urllib.parse import urljoin
from syspyconnhandler import ConnectionHandler as ch

pd.set_option('display.max_columns', None)

BASE_SERVICE = "https://services.odata.org/V4/Northwind/Northwind.svc/"

# Tabela → lista kolumn (nazwy dokładnie jak w OData $metadata)
TABLE_COLS = {
    "Categories": [
        "CategoryID", "CategoryName", "Description"
    ],
    "CustomerDemographics": [
        "CustomerTypeID", "CustomerDesc"
    ],
    "Customers": [
        "CustomerID", "CompanyName", "ContactName", "ContactTitle",
        "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax"
    ],
    "Employees": [
        "EmployeeID", "LastName", "FirstName", "Title", "TitleOfCourtesy",
        "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode",
        "Country", "HomePhone", "Extension", "Notes", "ReportsTo"
    ],
    "Order_Details": [
        "OrderID", "ProductID", "UnitPrice", "Quantity", "Discount"
    ],
    "Orders": [
        "OrderID", "CustomerID", "EmployeeID", "OrderDate", "RequiredDate",
        "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress",
        "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry"
    ],
    "Products": [
        "ProductID", "ProductName", "SupplierID", "CategoryID",
        "QuantityPerUnit", "UnitPrice", "UnitsInStock",
        "UnitsOnOrder", "ReorderLevel", "Discontinued"
    ],
    "Regions": [
        "RegionID", "RegionDescription"
    ],
    "Shippers": [
        "ShipperID", "CompanyName", "Phone"
    ],
    "Suppliers": [
        "SupplierID", "CompanyName", "ContactName", "ContactTitle",
        "Address", "City", "Region", "PostalCode", "Country",
        "Phone", "Fax", "HomePage"
    ],
    "Territories": [
        "TerritoryID", "TerritoryDescription", "RegionID"
    ],
}

def extract_northwind_data(table_name: str, select_cols: list | None = None) -> pd.DataFrame:
    """Pobierz tabelę z OData (JSON, bez metadanych) z obsługą @odata.nextLink."""
    base_url = f"{BASE_SERVICE}{table_name}"
    params = {"$format": "application/json;odata.metadata=none"}
    if select_cols:
        params["$select"] = ",".join(select_cols)

    rows, url, first = [], base_url, True
    while url:
        r = requests.get(url, params=params if first else None, timeout=30)
        r.raise_for_status()
        js = r.json()
        rows.extend(js.get("value", []))
        next_link = js.get("@odata.nextLink")
        url = urljoin(base_url, next_link) if next_link else None
        first = False
    return pd.DataFrame(rows)

def load_data_to_db(df: pd.DataFrame, table_name: str):
    """Zapisz DataFrame do Postgresa (replace tabelę)."""
    eng = ch.connect_to_database()
    with eng.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"✅ Załadowano {len(df):,} wierszy do tabeli {table_name}")

if __name__ == "__main__":
    for tbl, cols in TABLE_COLS.items():
        print(f"→ Extract {tbl} …")
        df = extract_northwind_data(tbl, cols)
        # (opcjonalnie) lekkie casty dat:
        if tbl == "Orders" and not df.empty:
            for c in ("OrderDate","RequiredDate","ShippedDate"):
                if c in df.columns:
                    df[c] = pd.to_datetime(df[c], errors="coerce")
        if tbl == "Employees" and not df.empty:
            for c in ("BirthDate","HireDate"):
                if c in df.columns:
                    df[c] = pd.to_datetime(df[c], errors="coerce")
        load_data_to_db(df, tbl)
