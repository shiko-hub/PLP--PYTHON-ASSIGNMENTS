try:
    
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    
    from calculate_discount import calculate_discount
    final_price = calculate_discount(original_price, discount)


    if final_price < original_price:
        print(f" Discount applied! Final price: KES {final_price:.2f}")
    else:
        print(f" No discount applied. Final price remains: KES {original_price:.2f}")

except ValueError:
    print(" Invalid input. Please enter numeric values for price and discount.")
