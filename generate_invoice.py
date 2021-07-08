from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors

from reportlab.platypus import Table, TableStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import pathlib
import os
import datetime



# Create asset & output folder if doesn't exist
current_path = pathlib.Path(__file__).parent.absolute()
output_folder = os.path.join(current_path, 'output')
asset_folder = os.path.join(current_path, 'assets')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(asset_folder):
    os.makedirs(asset_folder)


# Set Font for the Script
regular_fontfile = os.path.join(current_path, 'fonts', 'Helvetica.ttf')
bold_fontfile = os.path.join(current_path, 'fonts', 'Helvetica-Bold.ttf')
pdfmetrics.registerFont(TTFont('Helvetica', regular_fontfile))
pdfmetrics.registerFont(TTFont('Helvetica-Bold', bold_fontfile))



def createHeader(canvas, filename, x_coor, y_coor, width, height):
    """
    This method will create a logo in canvas in the given coordinate.
    This will also write "Invoice" in the top center of the page in Header.
    """
    logo_file = os.path.join(current_path, 'assets', filename)
    canvas.drawInlineImage(logo_file, x_coor, y_coor, width, height)

    canvas.setFont('Helvetica-Bold', 24)
    invoice_str_x_coor = (A4[0]/2) - (20*mm)
    canvas.drawString(invoice_str_x_coor, y_coor+(2*mm), "INVOICE")
    canvas.setFont('Helvetica', 8)
    return canvas

def createFromAddress(canvas, x_coor, y_coor, from_name, 
        address_line1, address_line2, country):
    """
    This method will setup the From address on the Invoice
    """
    canvas.drawString(x_coor, y_coor, "FROM")
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(x_coor, y_coor-(10*mm), from_name)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(x_coor, y_coor-(15*mm), address_line1)
    canvas.drawString(x_coor, y_coor-(20*mm), address_line2)
    canvas.drawString(x_coor, y_coor-(25*mm), country)

    return canvas

def createToAddress(canvas, x_coor, y_coor, to_name, 
        address_line1, address_line2, country):
    """
    This method will setup the From address on the Invoice
    """
    canvas.drawString(x_coor, y_coor, "TO")
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(x_coor, y_coor-(10*mm), to_name)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(x_coor, y_coor-(15*mm), address_line1)
    canvas.drawString(x_coor, y_coor-(20*mm), address_line2)
    canvas.drawString(x_coor, y_coor-(25*mm), country)

    return canvas


def createTaxRegistration(canvas, x_coor, y_coor, tax_number):
    """
    This method will setup the From address on the Invoice
    """
    canvas.drawString(x_coor, y_coor, "TAX REGISTRATION NUMBER")
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(x_coor, y_coor-(5*mm), tax_number)
    canvas.setFont('Helvetica', 8)

    return canvas

def createInvoiceDetails(canvas, x_coor, y_coor, right_col_y_coor, invoice_number, 
        invoice_from, invoice_to):
    """
    This method will setup the invoice details. 
    """
    canvas.drawString(x_coor, y_coor, "Invoice No.: {}".format(invoice_number))
    current_date = datetime.datetime.now().strftime("%b %d, %Y")
    next_week_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%b %d, %Y")
    canvas.drawString(x_coor, y_coor-(5*mm), "Invoice Date: {}".format(current_date))
    canvas.drawString(x_coor, y_coor-(10*mm), "Due Date: {}".format(next_week_date))

    canvas.drawString(right_col_y_coor, y_coor, "Start Date: {}".format(invoice_from))
    canvas.drawString(right_col_y_coor, y_coor-(5*mm), "End Date: {}".format(invoice_to))
    return canvas

def createItems(canvas, x_coor, y_coor, data):
    """
    This method fills in the main items of the invoice.
    """
    table = Table(data, colWidths=35*mm)
    table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "LEFT"),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                # ('FONTSIZE', (0, 0), (-1, 0), 12), 
                ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'), 
                ('BACKGROUND', (0, 0), (-1, 0), '#cbdbf5'),
                ])

    height = len(data)*5*mm + (15*mm)
    table.wrapOn(canvas, A4[0], y_coor)
    table.drawOn(canvas, x_coor, y_coor)
    return canvas, height

def createTotal(canvas, x_coor, y_coor, data):
    """
    This method fills in the main items of the invoice.
    """
    table = Table(data, colWidths=30*mm)
    table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "LEFT"),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                # ('FONTSIZE', (0, 0), (-1, 0), 12), 
                ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'), 
                ('BACKGROUND', (0, 0), (-1, 0), '#cbdbf5'),
                ('SPAN', (0, 0), (-1, 0)),
                ])

    height = len(data)*5*mm + (5*mm)
    table.wrapOn(canvas, A4[0], y_coor)
    table.drawOn(canvas, x_coor, y_coor)
    return canvas, height


if __name__ == "__main__":
    """
    This is the main function which will run when the program begins. 
    """

    # Take user inputs

    invoice_number = input("Enter the Invoice number: ")
    # invoice_number = "INV202111"
    invoice_from = input("Enter the start date of the Invoice (eg format: Jul 06, 2021): ")
    # invoice_from = "Jun 06, 2021"
    invoice_to = input("Enter the end date of the Invoice (eg format: Jul 06, 2021): ")
    # invoice_to = "Jul 06, 2021"

    print('Please enter FROM address information below')
    from_address_highlight = input("Enter FROM address Individual/Company Name: ")
    from_address_line1 = input("Enter FROM address line1: ")
    from_address_line2 = input("Enter FROM address line2: ")
    from_address_country_code = input("Enter FROM address country code(eg. US): ")


    print('\nPlease enter TO address information below')
    to_address_highlight = input("Enter TO address Individual/Company Name: ")
    to_address_line1 = input("Enter TO address line1: ")
    to_address_line2 = input("Enter TO address line2: ")
    to_address_country_code = input("Enter TO address country code(eg. US): ")

    tax_registration = input("Enter your tax registration number: ")

    number_of_items = input("Enter the number of items you want to input: ")

    item_data = [['Item', 'Hrs/Qty', 'Rate($)', 'Tax', 'Subtotal']]
    for index, num_item in enumerate(range(0, int(number_of_items))):
        print('\n\nEnter the details for item {}:'.format(index+1))
        item = input("Enter Item Name: ")
        quantity = input("Enter Hrs/Qty(eg. 2): ")
        rate = input("Enter Rate in $(eg. 500): ")
        tax = input("Enter Tax %(eg. 18): ")
        total_ammount = (float(quantity)*float(rate))
        current_item = [item, quantity, rate, tax, (total_ammount+(total_ammount*float(tax)/100))]
        item_data.append(current_item)

    item_data = tuple(item_data)

    # Initiate an A4 size canvas
    now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    output_filename = 'Invoice_{}_{}.pdf'.format(invoice_number, now)
    output_file_path = os.path.join(current_path, 'output', output_filename)
    canvas = Canvas(output_file_path, pagesize=A4)

    # Set Logo
    canvas = createHeader(canvas, 'tcw_logo.png', 20*mm, A4[1]-(30*mm), 30*mm, 10*mm)

    # Set From Address
    # canvas = createFromAddress(canvas, 20*mm, A4[1]-(50*mm), 'TheCodeWork', 
    #     'H-12, Baghajatin Lane', 'Chengcoorie Road, Silchar, Assam.', 'IN')
    canvas = createFromAddress(canvas, 20*mm, A4[1]-(50*mm), from_address_highlight, 
        from_address_line1, from_address_line2, from_address_country_code)

    # Set To Address
    # canvas = createToAddress(canvas, ((A4[0]/2)+20*mm), A4[1]-(50*mm), 'General Company INC.', 
    #     '123, ABC Street, North', 'New York. USA', 'US')
    canvas = createToAddress(canvas, ((A4[0]/2)+20*mm), A4[1]-(50*mm), to_address_highlight, 
        to_address_line1, to_address_line2, to_address_country_code)

    # Set Tax Registration
    canvas = createTaxRegistration(canvas, 20*mm, A4[1]-(85*mm), tax_registration)

    # Set Invoice Primary Details
    canvas = createInvoiceDetails(canvas, 20*mm, A4[1]-(105*mm), ((A4[0]/2)+20*mm), 
        invoice_number, invoice_from, invoice_to)

    # Set items of the invoice
    # item_data = (
    #     ['Item', 'Hrs/Qty', 'Rate($)', 'Tax', 'Subtotal'], 
    #     ['Development', '2', '100', '3', "USD 200"], 
    #     ['Design', '2', '85', '0', "USD 170"],
    #     )
    canvas, height = createItems(canvas, 20*mm, A4[1]-(150*mm), item_data)

    # Set Summary of the invoice
    total_ammount = sum([float(item[1])*float(item[2]) for item in item_data[1:]])
    total_tax = sum([float(item[3]) for item in item_data[1:]])
    net_ammount = total_ammount + total_tax
    summary_data = (
        ['Invoice Summary'],
        ['Total Amount', "USD {}".format(total_ammount)],
        ['Tax', "USD {}".format(total_tax)],    
        ['Net Amount', "USD {}".format(net_ammount)]
        )
    canvas, height = createTotal(canvas, ((A4[0]/2)+20*mm), A4[1]-(150*mm)-height, summary_data)

    # Save the Canvas to the PDF file.
    canvas.save()
