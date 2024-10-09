from FPrinter_Driver.FP_Datex import FP_Datex as FPD

datex = FPD()

pload = {
			"DiscountSum":0,
			"FooterText":"Thank you!",
			"HeaderText":"Operator 1",
			"Lines":[{
						"Amount":2.0,
						"Discount":1.5,
						"Name":"Coca-Cola 0.5L",
						"PLU":0,
						"Price":12.33,
						"VAT":"A"
					},{
						"Amount":1.0,
						"Discount":2.2,
						"Name":"Ciocolata Mars",
						"PLU":0,
						"Price":7.30,
						"VAT":"A"
					}],
			"Number":"1",
			"Payments":[{
						"Code":"1",
						"PaymentSum":50
			}]
}
pload2 = {
	"Lines":["Text liber"]
}


datex.HeaderText = "operatar 2"
datex.FooterText = "Multumim pentru cumparaturi"
datex.Payments['Code'] = "4"

PLU = [{
        "Amount":2.0,
        "Discount":1.5,
        "Name":"Coca-Cola 0.5L",
        "PLU":0,
        "Price":12.33,
        "VAT":"A"
       }, {
		"Amount":1.0,
		"Discount":2.2,
		"Name":"Ciocolata Mars",
		"PLU":0,
		"Price":7.30,
		"VAT":"A"
	}]


datex.setFiscalReceiptPLU(PLU)
# print datex.Payments['Code']
print(datex.PrintFiscalReceipt())