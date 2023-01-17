# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {'USDEUR': 0.85,'GBPEUR': 1.13,'CHFEUR': 0.86,'EURGBP': 0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    # (100,'EUR')
    # USA Dollar
    conc=amount[1]+currency
    if conc in RATES:
        return round(RATES.get(conc)*amount[0])
    return None
