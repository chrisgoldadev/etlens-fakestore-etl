# ETLens – Northwind ETL

Ten projekt demonstruje kompletny pipeline **ETL (Extract – Transform – Load)** z darmowego źródła danych **Northwind (OData V4)** do bazy **PostgreSQL (Neon)**.  
Następnie dane mogą być konsumowane w narzędziach BI, takich jak **Power BI** czy **Looker Studio**.

---

## 🔹 Architektura

1. **Extract**  
   - Pobieranie danych z publicznego API OData: [Northwind](https://services.odata.org/V4/Northwind/Northwind.svc/).  
   - Obsługa paginacji (`@odata.nextLink`) i selekcji tylko potrzebnych kolumn (`$select`).  

2. **Transform**  
   - Normalizacja nazw kolumn i typów danych.  
   - Konwersja pól dat (`OrderDate`, `ShippedDate`, `HireDate` itd.) do `datetime`.  

3. **Load**  
   - Ładowanie DataFrame’ów do **PostgreSQL (Neon)** przy pomocy **SQLAlchemy** i `to_sql`.  
   - Tryb domyślny: `replace` (każdy run nadpisuje tabelę).  
   - Możliwość zmiany na `append` + deduplikacja dla scenariuszy inkrementalnych.  

---

## 🔹 Technologie

- Python 3.11+  
- Biblioteki: `pandas`, `requests`, `sqlalchemy`, `psycopg` (lub `psycopg2-binary`)  
- Baza danych: **PostgreSQL (Neon)**  
- BI: **Power BI Desktop** / **Power BI Service** (z CSV/OneDrive/GitHub Pages)  

---

## 🔹 Struktura tabel

Projekt pobiera i ładuje poniższe encje z Northwind:

- `Categories` → `CategoryID`, `CategoryName`, `Description`  
- `CustomerDemographics` → `CustomerTypeID`, `CustomerDesc`  
- `Customers` → dane klientów (ID, CompanyName, Address, …)  
- `Employees` → dane pracowników (EmployeeID, Name, Title, Dates, …)  
- `Order_Details` → linie zamówień (OrderID, ProductID, UnitPrice, Quantity, Discount)  
- `Orders` → nagłówki zamówień (OrderID, CustomerID, EmployeeID, Dates, Shipping, …)  
- `Products` → dane produktów (ProductID, Name, SupplierID, CategoryID, Price, Stock, …)  
- `Regions` → RegionID, RegionDescription  
- `Shippers` → ShipperID, CompanyName, Phone  
- `Suppliers` → dane dostawców (CompanyName, Address, Phone, …)  
- `Territories` → TerritoryID, TerritoryDescription, RegionID  

---

## 🔹 Wymagania wstępne

Do uruchomienia projektu wymagane jest:
- **Darmowe konto w [Neon.tech](https://neon.tech/)**  
- Utworzenie **podstawowej bazy PostgreSQL** (np. `etlens_fakestore`)  
- Dane logowania (host, user, password, port, database) do wpisania w `secrets.env`  

---

## 🔹 Jak uruchomić

1. **Sklonuj repozytorium**  
   ```bash
   git clone https://github.com/chrisgoldadev/etlens-northwind-etl.git
   cd etlens-northwind-etl

2. **Utwórz i aktywuj wirtualne środowisko**
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. **Zainstaluj zależności**
pip install -r requirements.txt

4.**Utwórz plik secrets.env z danymi Neon:**
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/etlens_fakestore?sslmode=require

5. **Uruchom ETL:**
python main.py


