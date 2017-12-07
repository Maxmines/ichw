"""
__name__   = "currency.py"

__author__ = "huangyang"

__pkuid__  = "1700011776"

__email__  = "1700011776@pku.edu.cn"

"""

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    jstr=f1(currency_from,currency_to,amount_from)
    value=f2(jstr)
    return(amount_from,currency_from,"is",value,currency_to)
    
def f1(currency_from,currency_to,amount_from):
    """Fanction for currency exchange
    This fanction uses inputed strings to implement a simple currency exchange routine 
    using an online currency service. """
    from urllib.request import urlopen
    b='from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?'+b)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return(jstr)

def f2(jstr):
    """This function find the value from inputed string."""
    c=jstr.find(':')
    c=jstr.find(':', c+1)
    jstr=jstr[c+3:]
    c=jstr.find(' ')
    return(jstr[:c])

def test_exchange():
    """Test function exchange."""
    assert(exchange("USD","EUR","2.5")==('2.5', 'USD', 'is', '2.0952375', 'EUR'))
    
def test_f1():
    """Test function f1."""
    assert(f1("USD","EUR","2.5")[84:]=='"error" : "" }')
    
def test_f2():
    """Test function f2."""
    assert(f2("for : x to : '2.0952375 EUR'")=="2.0952375")
    
def test_all():
    """Test all cases"""
    test_exchange()
    test_f1()
    test_f2()
    print("All tests passed")
    
currency_from=input("please enter kind of money you have:")
currency_to=input("please enter kind of money you want:")
amount_from=input("please enter amount of money you have:")
test_all()
print(" ".join(exchange(currency_from, currency_to, amount_from)),".")