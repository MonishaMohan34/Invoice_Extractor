This project is an Invoice Extractor System built with Django. It allows users to upload invoice bills, then automatically extracts and saves key information like Invoice ID, Customer Name, and Total Due Amount directly to a database.



User Interface: A simple, easy-to-use interface for uploading invoice PDFs.
PDF Data Extraction: Uses `pdfplumber` and regular expressions to retrieve specific details from invoices.
Database Storage: Extracted information is stored in a pre-defined database table for easy access and future reference.



Technologies Used
Django: Backend framework
pdfplumber: PDF parsing
Regex: Data extraction from text
SQLite3: Database for storing extracted information
