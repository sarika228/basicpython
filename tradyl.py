country_code=input("enter the country code:")
product_code=input("enter the product code:")
weight_in_kg=float(input("enter the weight in kg:"))

if (country_code=="Uk") or (weight_in_kg <5) and(product_code ==123):
    print("shipping cost",5*1.2*(1+0.18))
if (country_code=="Uk") or (weight_in_kg <5) and (product_code==234):
    print("shipping cost",5*1.5*(1+0.18))
if (country_code=="Uk") or (weight_in_kg>=5) and (product_code==123):
    print("shipping cost",15*1.2*(1+0.18))
if (country_code=="Uk") or (weight_in_kg>=5) and (product_code==234):
    print("shipping cost",15*1.5*(1+0.18))
if (country_code=="Us") or (weight_in_kg<10) and (product_code==123):
    print("shipping cost",5*1.2*(1+0.18))
if (country_code=="Us") or  (weight_in_kg<10) and (product_code==234):
    print("shipping cost",5*1.5*(1+0.18))
if (country_code=="Us") or (weight_in_kg>=10) and (product_code==123):
    print("shipping cost", 15*1.2*(1+0.18))
if (country_code=="Us") or (weight_in_kg>=10) and (product_code==234):
    print("shipping cost",15*1.5*(1+0.18))
else:
    print("no change in cost")