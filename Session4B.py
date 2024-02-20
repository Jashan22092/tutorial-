product_prices=[200,300,450,500,845,600]
max = product_prices[0]
print("Initial Max Is: ")
for idx in range(1 , len(product_prices)):
       print("Compare" , max , "With" , product_prices[idx])
       if product_prices[idx] > max:
          max = product_prices[idx]
          print("New Max Is: " , max)

print("Real Max Is: " , max)

print()
ipl_score_pt=[10,12,13,14,17,15]
max1 = ipl_score_pt[0]
print("Initial Score Is: " , max1)

for idx in range(1, len(ipl_score_pt)):
    print("Compare" , max1 , "With" , ipl_score_pt[idx])
    if ipl_score_pt[idx] > max1:
        max1 = ipl_score_pt[idx]
        print("New Max Is: " , max1)

print("Real Max: " , max1)