# Database Modeling Pipeline

This directory contains the database modeling components of the Customer Segmentation Data Pipeline. The pipeline creates a star schema optimized for analytical queries and customer segmentation analysis.

## 🎯 Overview

The database modeling pipeline transforms cleaned customer data into a dimensional model with fact and dimension tables, then loads them into a SQLite database for efficient querying and analysis.

## 🏗️ Database Architecture

### Star Schema Design

```
                    ┌─────────────────────┐
                    │   dim_customer      │
                    │ ─────────────────── │
                    │ customerid (PK)     │
                    │ gender              │
                    │ seniorcitizen       │
                    │ partner             │
                    │ dependents          │
                    └─────────┬───────────┘
                              │
          ┌─────────────────────────────────────────┐
          │           fact_table                    │
          │ ─────────────────────────────────────── │
          │ customerid (FK) ←────────────────────── │
          │ tenure                                  │
          │ monthlycharges                         │
          │ totalcharges                           │
          │ churn                                  │
          └──────────┬──────────────┬──────────────┘
                     │              │
      ┌──────────────┴───────────┐  │  ┌─────────────────────┐
      │     dim_services         │  │  │  dim_subscription   │
      │ ──────────────────────── │  │  │ ─────────────────── │
      │ customerid (PK)          │  │  │ customerid (PK)     │
      │ phoneservice             │  │  │ contract            │
      │ multiplelines            │  │  │ paperlessbilling    │
      │ internetservice          │  │  │ paymentmethod       │
      │ onlinesecurity           │  │  └─────────────────────┘
      │ onlinebackup             │  │
      │ deviceprotection         │  │
      │ techsupport              │  │
      │ streamingtv              │  │
      │ streamingmovies          │  │
      └──────────────────────────┘  │
                                    │
                                    └─→ Foreign Key Relationships
```

## 📊 Table Specifications

### Fact Table: `fact_table`
**Purpose**: Contains measurable, quantitative data about customer activities and outcomes.

| Column | Type | Description |
|--------|------|-------------|
| customerid | TEXT | Customer identifier (Foreign Key) |
| tenure | INTEGER | Number of months customer has stayed |
| monthlycharges | REAL | Customer's monthly charge amount |
| totalcharges | REAL | Customer's total charges to date |
| churn | TEXT | Whether customer churned (Yes/No) |

### Dimension Table: `dim_customer_table`
**Purpose**: Customer demographic information.

| Column | Type | Description |
|--------|------|-------------|
| customerid | TEXT | Customer identifier (Primary Key) |
| gender | TEXT | Customer gender (Male/Female) |
| seniorcitizen | INTEGER | Senior citizen flag (0/1) |
| partner | INTEGER | Has partner flag (0/1) |
| dependents | INTEGER | Has dependents flag (0/1) |

### Dimension Table: `dim_services_table`
**Purpose**: Service subscription details.

| Column | Type | Description |
|--------|------|-------------|
| customerid | TEXT | Customer identifier (Primary Key) |
| phoneservice | TEXT | Phone service subscription |
| multiplelines | TEXT | Multiple lines service |
| internetservice | TEXT | Internet service type |
| onlinesecurity | TEXT | Online security service |
| onlinebackup | TEXT | Online backup service |
| deviceprotection | TEXT | Device protection service |
| techsupport | TEXT | Tech support service |
| streamingtv | TEXT | Streaming TV service |
| streamingmovies | TEXT | Streaming movies service |

### Dimension Table: `dim_subscription_table`
**Purpose**: Billing and contract information.

| Column | Type | Description |
|--------|------|-------------|
| customerid | TEXT | Customer identifier (Primary Key) |
| contract | TEXT | Contract type (Month-to-month, One year, Two year) |
| paperlessbilling | TEXT | Paperless billing preference |
| paymentmethod | TEXT | Payment method type |

## 🚀 Quick Start

### Prerequisites
```bash
# Ensure you're in the project root directory
cd "Customer Segmentation Data Pipeline"

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Verify required packages
pip list | findstr -i "pandas sqlalchemy"
```

### Run Database Pipeline

#### Step 1: Ensure Data is Processed
```bash
# Make sure processed data exists
dir data\fact_dim_tables\
# Should contain: fact_df.csv, dim_customer_df.csv, dim_service_df.csv, dim_subscription_df.csv
```

#### Step 2: Create Database
```bash
# Run the database creation process
python -c "
import pandas as pd
import os
from sqlalchemy import create_engine

# Paths
data_path = 'data/fact_dim_tables'
database_path = 'database/telco_churn.db'

# Create database directory if it doesn't exist
os.makedirs('database', exist_ok=True)

# Load DataFrames
fact = pd.read_csv(os.path.join(data_path, 'fact_df.csv'))
dim_customer = pd.read_csv(os.path.join(data_path, 'dim_customer_df.csv'))
dim_services = pd.read_csv(os.path.join(data_path, 'dim_service_df.csv'))
dim_subscription = pd.read_csv(os.path.join(data_path, 'dim_subscription_df.csv'))

# Create SQLite connection
engine = create_engine(f'sqlite:///{database_path}')

# Write tables to SQLite
fact.to_sql('fact_table', con=engine, if_exists='replace', index=False)
dim_customer.to_sql('dim_customer_table', con=engine, if_exists='replace', index=False)
dim_services.to_sql('dim_services_table', con=engine, if_exists='replace', index=False)
dim_subscription.to_sql('dim_subscription_table', con=engine, if_exists='replace', index=False)

print('✅ Database created successfully!')
"
```

#### Step 3: Verify Database Creation
```bash
# Check if database file exists
dir database\telco_churn.db

# Query the database to verify tables
python -c "
import sqlite3

con = sqlite3.connect('database/telco_churn.db')
cursor = con.cursor()

# List all tables
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table';\")
tables = cursor.fetchall()
print('📊 Tables in database:', [table[0] for table in tables])

# Check record counts
for table in ['fact_table', 'dim_customer_table', 'dim_services_table', 'dim_subscription_table']:
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    count = cursor.fetchone()[0]
    print(f'📈 {table}: {count} records')

con.close()
"
```

## 🔍 Database Queries

### Sample Analytical Queries

#### 1. Customer Churn Analysis by Demographics
```sql
SELECT 
    dc.gender,
    dc.seniorcitizen,
    COUNT(*) as total_customers,
    SUM(CASE WHEN ft.churn = 'Yes' THEN 1 ELSE 0 END) as churned_customers,
    ROUND(
        (SUM(CASE WHEN ft.churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2
    ) as churn_rate
FROM fact_table ft
JOIN dim_customer_table dc ON ft.customerid = dc.customerid
GROUP BY dc.gender, dc.seniorcitizen
ORDER BY churn_rate DESC;
```

#### 2. Revenue Analysis by Service Type
```sql
SELECT 
    ds.internetservice,
    COUNT(*) as customer_count,
    AVG(ft.monthlycharges) as avg_monthly_revenue,
    SUM(ft.totalcharges) as total_revenue
FROM fact_table ft
JOIN dim_services_table ds ON ft.customerid = ds.customerid
WHERE ds.internetservice != 'No'
GROUP BY ds.internetservice
ORDER BY total_revenue DESC;
```

#### 3. Contract Analysis
```sql
SELECT 
    dsub.contract,
    dsub.paymentmethod,
    COUNT(*) as customers,
    AVG(ft.tenure) as avg_tenure,
    AVG(ft.monthlycharges) as avg_monthly_charges
FROM fact_table ft
JOIN dim_subscription_table dsub ON ft.customerid = dsub.customerid
GROUP BY dsub.contract, dsub.paymentmethod
ORDER BY avg_tenure DESC;
```

#### 4. High-Value Customer Segments
```sql
SELECT 
    ft.customerid,
    dc.gender,
    dc.seniorcitizen,
    dsub.contract,
    ft.tenure,
    ft.monthlycharges,
    ft.totalcharges,
    ft.churn,
    CASE 
        WHEN ft.totalcharges > 5000 THEN 'High Value'
        WHEN ft.totalcharges > 2000 THEN 'Medium Value'
        ELSE 'Low Value'
    END as customer_segment
FROM fact_table ft
JOIN dim_customer_table dc ON ft.customerid = dc.customerid
JOIN dim_subscription_table dsub ON ft.customerid = dsub.customerid
WHERE ft.totalcharges > 3000
ORDER BY ft.totalcharges DESC;
```

## 📊 Database Performance

### Indexing Strategy
```sql
-- Create indexes for better query performance
CREATE INDEX idx_fact_customerid ON fact_table(customerid);
CREATE INDEX idx_fact_churn ON fact_table(churn);
CREATE INDEX idx_fact_tenure ON fact_table(tenure);
CREATE INDEX idx_dim_customer_gender ON dim_customer_table(gender);
CREATE INDEX idx_dim_services_internet ON dim_services_table(internetservice);
CREATE INDEX idx_dim_subscription_contract ON dim_subscription_table(contract);
```

### Database Statistics
- **Total Records**: 7,043 customers
- **Database Size**: ~2.5 MB
- **Table Count**: 4 tables (1 fact + 3 dimensions)
- **Query Performance**: Optimized for analytical workloads

## 🛠️ Maintenance Commands

### Backup Database
```bash
# Create backup
copy "database\telco_churn.db" "database\telco_churn_backup_$(Get-Date -Format 'yyyyMMdd').db"
```

### Database Cleanup
```bash
# Remove and recreate database
del "database\telco_churn.db"
# Then run the creation script again
```

### Export Tables to CSV
```bash
python -c "
import sqlite3
import pandas as pd

con = sqlite3.connect('database/telco_churn.db')

# Export each table
tables = ['fact_table', 'dim_customer_table', 'dim_services_table', 'dim_subscription_table']
for table in tables:
    df = pd.read_sql_query(f'SELECT * FROM {table}', con)
    df.to_csv(f'database/export_{table}.csv', index=False)
    print(f'✅ Exported {table} to database/export_{table}.csv')

con.close()
"
```

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: Database File Not Found
```bash
# Solution: Check if database directory exists
mkdir database
# Then run the creation script
```

#### Issue 2: Table Already Exists
```bash
# Solution: Use 'replace' mode in to_sql()
# This is already handled in the pipeline
```

#### Issue 3: Permission Denied
```bash
# Solution: Check if database file is locked
# Close any open connections and try again
```

## 📈 Future Enhancements

- [ ] Add data validation constraints
- [ ] Implement incremental loading
- [ ] Add database versioning
- [ ] Create stored procedures for common queries
- [ ] Add data lineage tracking
- [ ] Implement automatic backup scheduling

## 🤝 Integration

This database pipeline integrates with:
- **Jupyter Notebook Pipeline**: Receives processed data files
- **ETL Pipeline**: Can be triggered after ETL completion
- **Analytics Tools**: Provides structured data for BI tools
- **API Services**: Database can be queried via REST APIs

## 📚 Additional Resources

- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Star Schema Design Patterns](https://en.wikipedia.org/wiki/Star_schema)
