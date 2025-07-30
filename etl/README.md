# Automated ETL Pipeline

This directory contains the automated Extract, Transform, Load (ETL) pipeline for the Customer Segmentation Data Pipeline. This production-ready pipeline automates the entire data processing workflow from raw data ingestion to final cleaned datasets.

## 🎯 Overview

The automated ETL pipeline provides a scalable, maintainable solution for processing customer data through multiple stages of validation, cleaning, transformation, and loading. It's designed for production environments with comprehensive error handling, logging, and monitoring capabilities.

## 🏗️ Pipeline Architecture

```
Raw Data → Extract → Transform → Load → Cleaned Data
    ↓         ↓         ↓         ↓         ↓
CSV Files → Ingest → Validate → Clean → Process → Output Files
                      ↓         ↓         ↓
                   Profile → Standardize → Model
```

### Pipeline Components

```
etl/
├── __init__.py                 # Package initialization
├── config/
│   ├── __init__.py
│   ├── settings.py             # Configuration settings
│   └── logging_config.py       # Logging configuration
├── extractors/
│   ├── __init__.py
│   ├── csv_extractor.py        # CSV data extraction
│   └── data_validator.py       # Data validation
├── transformers/
│   ├── __init__.py
│   ├── data_cleaner.py         # Data cleaning operations
│   ├── feature_engineer.py     # Feature engineering
│   └── data_standardizer.py    # Data standardization
├── loaders/
│   ├── __init__.py
│   ├── csv_loader.py           # CSV output loading
│   └── database_loader.py      # Database loading
├── utils/
│   ├── __init__.py
│   ├── logger.py               # Logging utilities
│   ├── file_manager.py         # File management
│   └── data_profiler.py        # Data profiling
├── pipeline.py                 # Main pipeline orchestrator
└── main.py                     # Entry point
```

## 🚀 Quick Start

### Prerequisites
```bash
# Navigate to project directory
cd "Customer Segmentation Data Pipeline"

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install additional ETL dependencies if needed
pip install pandas numpy sqlalchemy python-dotenv pyyaml
```

### Configuration Setup

#### 1. Environment Variables
Create `.env` file in the ETL directory:
```bash
# Create .env file
New-Item etl\.env -ItemType File

# Add environment variables
@"
# Data Paths
RAW_DATA_PATH=data/raw
PROCESSED_DATA_PATH=data/processed
FACT_DIM_PATH=data/fact_dim_tables
DATABASE_PATH=database/telco_churn.db

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/etl_pipeline.log

# Processing Options
HANDLE_MISSING=fill_zero
ENCODING_METHOD=binary_map
VALIDATION_STRICT=True
"@ | Out-File -FilePath etl\.env -Encoding utf8
```

#### 2. Configuration File
```bash
# Create config.yaml
@"
pipeline:
  name: customer_segmentation_etl
  version: 1.0.0
  
data:
  input_file: Customer_churn4.csv
  chunk_size: 1000
  encoding: utf-8
  
validation:
  required_columns:
    - customerID
    - gender
    - SeniorCitizen
    - Partner
    - Dependents
    - tenure
    - PhoneService
    - MultipleLines
    - InternetService
    - OnlineSecurity
    - OnlineBackup
    - DeviceProtection
    - TechSupport
    - StreamingTV
    - StreamingMovies
    - Contract
    - PaperlessBilling
    - PaymentMethod
    - MonthlyCharges
    - TotalCharges
    - Churn
  
  data_types:
    tenure: int64
    MonthlyCharges: float64
    TotalCharges: object  # Will be converted to float64
    SeniorCitizen: int64
    
cleaning:
  missing_value_strategy:
    TotalCharges: fill_zero
  
  binary_mapping:
    Yes: 1
    No: 0
    
  column_standardization:
    case: lower
    spaces: underscore
"@ | Out-File -FilePath etl\config.yaml -Encoding utf8
```

### Run the ETL Pipeline

#### Option 1: Complete Automated Run
```bash
# Run the full ETL pipeline
python run_etl_pipeline.py
```

#### Option 2: Step-by-Step Execution
```bash
# Run individual pipeline stages
python -m etl.main --stage extract
python -m etl.main --stage transform  
python -m etl.main --stage load
```

#### Option 3: Custom Configuration
```bash
# Run with custom config file
python -m etl.main --config custom_config.yaml
```

#### Option 4: Debug Mode
```bash
# Run in debug mode with verbose logging
python -m etl.main --debug --log-level DEBUG
```

## 📋 Pipeline Stages

### Stage 1: Extract
**Purpose**: Data ingestion and initial validation

```python
# Extract stage operations
def extract_stage():
    """
    - Read raw CSV data
    - Validate file structure
    - Check schema compliance
    - Log data quality metrics
    """
    pass
```

**Commands**:
```bash
# Extract only
python -c "
from etl.extractors.csv_extractor import CSVExtractor
from etl.extractors.data_validator import DataValidator

extractor = CSVExtractor('data/raw/Customer_churn4.csv')
data = extractor.extract()
print(f'✅ Extracted {len(data)} records')

validator = DataValidator()
is_valid = validator.validate_schema(data)
print(f'✅ Schema validation: {is_valid}')
"
```

### Stage 2: Transform
**Purpose**: Data cleaning, standardization, and feature engineering

```python
# Transform stage operations
def transform_stage():
    """
    - Handle missing values
    - Convert data types
    - Standardize formats
    - Engineer features
    - Create binary encodings
    """
    pass
```

**Commands**:
```bash
# Transform only
python -c "
import pandas as pd
from etl.transformers.data_cleaner import DataCleaner
from etl.transformers.data_standardizer import DataStandardizer

# Load raw data
df = pd.read_csv('data/raw/Customer_churn4.csv')

# Clean data
cleaner = DataCleaner()
cleaned_df = cleaner.clean(df)
print(f'✅ Data cleaned: {len(cleaned_df)} records')

# Standardize data
standardizer = DataStandardizer()
standardized_df = standardizer.standardize(cleaned_df)
print(f'✅ Data standardized: {standardized_df.shape}')
"
```

### Stage 3: Load
**Purpose**: Output generation and database loading

```python
# Load stage operations
def load_stage():
    """
    - Create fact and dimension tables
    - Export to CSV files
    - Load to database
    - Generate reports
    """
    pass
```

**Commands**:
```bash
# Load only
python -c "
import pandas as pd
from etl.loaders.csv_loader import CSVLoader
from etl.loaders.database_loader import DatabaseLoader

# Load processed data
df = pd.read_csv('data/processed/processed_df.csv')

# Create dimensional model
csv_loader = CSVLoader()
fact_dim_tables = csv_loader.create_dimensional_model(df)
print(f'✅ Created {len(fact_dim_tables)} tables')

# Load to database
db_loader = DatabaseLoader()
db_loader.load_to_database(fact_dim_tables)
print('✅ Data loaded to database')
"
```

## 🔧 Pipeline Components

### 1. Extractors

#### CSV Extractor (`extractors/csv_extractor.py`)
```python
class CSVExtractor:
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        
    def extract(self):
        """Extract data from CSV file with error handling"""
        try:
            data = pd.read_csv(self.file_path, encoding=self.encoding)
            self.logger.info(f"Extracted {len(data)} records")
            return data
        except Exception as e:
            self.logger.error(f"Extraction failed: {e}")
            raise
```

#### Data Validator (`extractors/data_validator.py`)
```python
class DataValidator:
    def validate_schema(self, data):
        """Validate data schema and quality"""
        # Check required columns
        # Validate data types
        # Check for missing values
        # Log validation results
        pass
```

### 2. Transformers

#### Data Cleaner (`transformers/data_cleaner.py`)
```python
class DataCleaner:
    def clean(self, data):
        """Clean and prepare data"""
        # Handle missing values
        # Convert data types
        # Remove duplicates
        # Validate ranges
        pass
```

#### Feature Engineer (`transformers/feature_engineer.py`)
```python
class FeatureEngineer:
    def engineer_features(self, data):
        """Create new features"""
        # Binary encoding
        # Categorical mapping
        # Derived features
        # Feature scaling
        pass
```

### 3. Loaders

#### CSV Loader (`loaders/csv_loader.py`)
```python
class CSVLoader:
    def save_to_csv(self, data, file_path):
        """Save data to CSV file"""
        data.to_csv(file_path, index=False)
        
    def create_dimensional_model(self, data):
        """Create fact and dimension tables"""
        # Create fact table
        # Create dimension tables
        # Return table dictionary
        pass
```

#### Database Loader (`loaders/database_loader.py`)
```python
class DatabaseLoader:
    def load_to_database(self, tables):
        """Load tables to database"""
        # Create database connection
        # Load fact table
        # Load dimension tables
        # Create indexes
        pass
```

## 📊 Monitoring and Logging

### Log Configuration
```python
# logging_config.py
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/etl_pipeline.log',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'etl': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}
```

### Monitoring Commands
```bash
# View logs in real-time
Get-Content logs\etl_pipeline.log -Wait

# Check pipeline status
python -c "
from etl.utils.logger import get_logger
logger = get_logger('etl.monitor')
logger.info('Pipeline status check')
"

# Generate pipeline report
python -c "
from etl.utils.data_profiler import DataProfiler
profiler = DataProfiler()
report = profiler.generate_report('data/processed/processed_df.csv')
print(report)
"
```

## 🚨 Error Handling

### Common Error Scenarios

#### 1. File Not Found
```python
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    logger.error(f"File not found: {file_path}")
    # Fallback strategy or raise exception
```

#### 2. Data Quality Issues
```python
if data.isnull().sum().sum() > threshold:
    logger.warning("High number of missing values detected")
    # Apply cleaning strategy
```

#### 3. Schema Validation Failure
```python
required_columns = ['customerID', 'gender', 'tenure']
missing_columns = set(required_columns) - set(data.columns)
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")
```

### Recovery Strategies
```bash
# Restart from last successful stage
python -m etl.main --resume --from-stage transform

# Skip failed records and continue
python -m etl.main --skip-errors --max-errors 10

# Run in safe mode with extensive validation
python -m etl.main --safe-mode --validate-all
```

## 📈 Performance Optimization

### Processing Large Files
```python
# Chunk processing for large files
def process_large_file(file_path, chunk_size=1000):
    chunks = pd.read_csv(file_path, chunksize=chunk_size)
    processed_chunks = []
    
    for chunk in chunks:
        processed_chunk = process_chunk(chunk)
        processed_chunks.append(processed_chunk)
    
    return pd.concat(processed_chunks, ignore_index=True)
```

### Parallel Processing
```bash
# Run multiple pipeline instances
python -m etl.main --parallel --workers 4

# Process different data segments
python -m etl.main --segment 1 --total-segments 4 &
python -m etl.main --segment 2 --total-segments 4 &
python -m etl.main --segment 3 --total-segments 4 &
python -m etl.main --segment 4 --total-segments 4 &
```

### Memory Optimization
```python
# Reduce memory usage
def optimize_dtypes(df):
    """Optimize data types to reduce memory usage"""
    for col in df.select_dtypes(include=['int64']).columns:
        if df[col].max() < 127 and df[col].min() >= -128:
            df[col] = df[col].astype('int8')
    return df
```

## 🔄 Scheduling and Automation

### Windows Task Scheduler
```bash
# Create scheduled task for daily runs
schtasks /create /sc daily /mo 1 /tr "python C:\path\to\run_etl_pipeline.py" /tn "CustomerETL"

# Run task immediately
schtasks /run /tn "CustomerETL"

# Check task status
schtasks /query /tn "CustomerETL"
```

### PowerShell Automation Script
```powershell
# automated_etl_runner.ps1
$ErrorActionPreference = "Stop"

try {
    Write-Host "Starting Customer Segmentation ETL Pipeline..."
    
    # Activate virtual environment
    & ".\.venv\Scripts\Activate.ps1"
    
    # Run ETL pipeline
    $result = python run_etl_pipeline.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ ETL Pipeline completed successfully"
        # Send success notification
    } else {
        Write-Host "❌ ETL Pipeline failed"
        # Send failure notification
    }
} catch {
    Write-Host "❌ Error running ETL Pipeline: $_"
    # Log error and send notification
}
```

### Batch Runner
```bash
# run_etl.bat
@echo off
echo Starting Customer Segmentation ETL Pipeline...

cd /d "C:\path\to\Customer Segmentation Data Pipeline"
call .venv\Scripts\activate.bat

python run_etl_pipeline.py

if %ERRORLEVEL% EQU 0 (
    echo ✅ ETL Pipeline completed successfully
) else (
    echo ❌ ETL Pipeline failed with error code %ERRORLEVEL%
)

pause
```

## 🧪 Testing

### Unit Tests
```bash
# Run unit tests
python -m pytest etl/tests/ -v

# Run specific test module
python -m pytest etl/tests/test_extractors.py -v

# Run with coverage
python -m pytest etl/tests/ --cov=etl --cov-report=html
```

### Integration Tests
```bash
# Test full pipeline with sample data
python -m etl.tests.integration_test

# Test individual components
python -m etl.tests.test_pipeline_stages
```

### Data Quality Tests
```bash
# Validate output data quality
python -c "
from etl.utils.data_profiler import DataProfiler
profiler = DataProfiler()
quality_report = profiler.validate_output('data/processed/processed_df.csv')
print('Data Quality Score:', quality_report['score'])
"
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: Import Errors
```bash
# Solution: Check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Add project root to Python path
$env:PYTHONPATH = "C:\path\to\Customer Segmentation Data Pipeline"
```

#### Issue 2: Memory Issues with Large Files
```bash
# Solution: Use chunked processing
python -m etl.main --chunk-size 500 --low-memory
```

#### Issue 3: Database Connection Issues
```bash
# Solution: Check database permissions and path
python -c "
import sqlite3
try:
    conn = sqlite3.connect('database/telco_churn.db')
    print('✅ Database connection successful')
    conn.close()
except Exception as e:
    print(f'❌ Database connection failed: {e}')
"
```

### Debug Mode
```bash
# Run in debug mode with maximum verbosity
python -m etl.main --debug --verbose --log-level DEBUG --profile
```

## 📚 API Reference

### Pipeline Class
```python
from etl.pipeline import ETLPipeline

# Initialize pipeline
pipeline = ETLPipeline(config_path='etl/config.yaml')

# Run complete pipeline
result = pipeline.run()

# Run specific stages
pipeline.extract()
pipeline.transform()
pipeline.load()

# Get pipeline status
status = pipeline.get_status()
```

### Configuration Management
```python
from etl.config.settings import Settings

# Load configuration
config = Settings.load('etl/config.yaml')

# Update configuration
config.update({'data.chunk_size': 2000})
config.save()
```

## 🤝 Integration

### Integration Points
- **Jupyter Notebook**: Can trigger ETL pipeline from notebook cells
- **Database Pipeline**: Automatically loads results to database
- **API Services**: Can be called via REST API endpoints
- **Monitoring Systems**: Provides logs and metrics for monitoring

### Example Integration
```python
# Trigger ETL from Jupyter notebook
from etl.pipeline import ETLPipeline

pipeline = ETLPipeline()
result = pipeline.run()

if result.success:
    print("✅ ETL completed, proceeding with analysis...")
    # Continue with data analysis
else:
    print("❌ ETL failed:", result.error_message)
```

## 🚀 Future Enhancements

- [ ] Real-time streaming data processing
- [ ] Cloud deployment (AWS/Azure)
- [ ] Docker containerization
- [ ] API endpoints for pipeline control
- [ ] Advanced data quality monitoring
- [ ] Machine learning model integration
- [ ] Data lineage tracking
- [ ] Multi-format input support (JSON, Parquet, etc.)

## 📄 License

This ETL pipeline is part of the Customer Segmentation Data Pipeline project and follows the same MIT License.
