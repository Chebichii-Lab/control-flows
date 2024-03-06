def calculate_discount(price, discount_percent):
    if discount_percent <= 20:
        discounted_price = price -(price * (discount_percent/100))
        return discounted_price
    else:
        return price
    

# to prompt user to enter original price
    
original_price = float(input('Enter original price:'))
discount_percentage = float(input('Enter discount percentage: '))


final_price = calculate_discount(original_price, discount_percentage)

#print final price after discount is applied
if final_price != original_price:
    print('Final price after Discount:', final_price)
else:
    print('Discount not applied. Final price: ', final_price)    