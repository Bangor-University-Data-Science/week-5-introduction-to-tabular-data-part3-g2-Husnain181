import pandas as pd

def import_data(OnlineRetail: str) -> pd.DataFrame:
    if filename.endswith('.xlsx'):
        df = pd.read_excel(OnlineRetail.xlsx)
    elif filename.endswith('.csv'):
        df = pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format. Use .xlsx or .csv")
    return df

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    return df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    customer_counts = df.groupby('CustomerID').size()
    loyal_customers = customer_counts[customer_counts >= min_purchases].reset_index(name='purchase_count')
    return loyal_customers

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    quarterly_revenue = df.groupby('Quarter').apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum()).reset_index(name='total_revenue')
    return quarterly_revenue

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    product_totals = df.groupby('StockCode')['Quantity'].sum().nlargest(top_n).reset_index()
    return product_totals

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby('StockCode').agg(avg_quantity=('Quantity', 'mean'), avg_unit_price=('UnitPrice', 'mean')).reset_index()
    return summary

def answer_conceptual_questions() -> dict:
    answers = {
        "Q1": {"A", "D"},
        "Q2": {"B"},
        "Q3": {"A", "B", "C"},
        "Q4": {"A", "B"},
        "Q5": {"A"}
    }
    return answers

