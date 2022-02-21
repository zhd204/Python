def complete_link_address(link_address: str):
    if not ("https://www.zillow.com" in link_address):
        complete_address = "https://www.zillow.com" + link_address
    else:
        complete_address = link_address

    return complete_address


def get_price(price_str: str):
    special_characters = ["$", ",", "+", "/", "mo"]
    for cha in special_characters:
        price_str = price_str.replace(cha, "")
    return float(price_str)