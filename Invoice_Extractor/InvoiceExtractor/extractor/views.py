from django.shortcuts import render

import pdfplumber
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Invoice
from .forms import InvoiceUploadForm

def extract_invoice_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    
    invoice_id = re.search(r'Invoice Number\s+(\S+)', text)
    invoice_id = invoice_id.group(1) if invoice_id else None

    
    customer_name = re.search(r'To:\s*([A-Za-z\s]+?)(?=\d)', text)
    customer_name = customer_name.group(1).strip() if customer_name else None

    
    total_amount = re.search(r'Total Due\s+\$?(\d+\.\d{2})', text)
    total_amount = float(total_amount.group(1)) if total_amount else None

    return invoice_id, customer_name, total_amount

def upload_invoice(request):
    if request.method == 'POST':
        form = InvoiceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']

            with open('temp_invoice.pdf', 'wb') as f:
                f.write(pdf_file.read())

            invoice_id, customer_name, total_amount = extract_invoice_data('temp_invoice.pdf')

            if all([invoice_id, customer_name, total_amount]):
                Invoice.objects.create(
                    invoice_id=invoice_id,
                    customer_name=customer_name,
                    total_amount=total_amount
                )
                messages.success(request, "Database updated successfully!")
            else:
                messages.error(request, "Failed to extract required information from the PDF.")
            return redirect('upload_invoice')
    else:
        form = InvoiceUploadForm()
    return render(request, 'extractor/upload_invoice.html', {'form': form})
