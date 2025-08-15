def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if it's 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
