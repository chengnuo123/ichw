###Assign2

###chengnuo,1800011785
###12.2


"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

"""Unit test for module test

When run as a script, this module invokes several procedures that 
test the various functions in the module test."""

def exchange(currency_from,currency_to,amount_from ):
    """generate a URL for getting datas from the website"""
    d='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=x&to=y&amt=z'    
    e=d.replace('x',currency_from)
    f=e.replace('y',currency_to)
    g=f.replace('z',amount_from)
    from urllib.request import urlopen
    doc=urlopen(g)
    docstr=doc.read()
    doc.close()
    jstr=docstr.decode('ascii')
    return jstr

def test_exchange():
    """test the 'exchange' function """
    a="USD"
    b="EUR"
    c="2.5"
    test1=exchange(a,b,c)
    Test1='{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
    assert (test1==Test1)
    a="BWP"
    b="NZD"
    c="4.73"
    test2=exchange(a,b,c)
    Test2='{ "from" : "4.73 Botswanan Pula", "to" : "0.66796788832763 New Zealand Dollars", "success" : true, "error" : "" }'
    assert (test2==Test2)
    
def extract(m):
    """output the result"""
    i=m.split('"')
    h=i[7]
    """amount and currency"""
    j=h.partition(' ')
    k=j[0]
    return k
def test_extract():
    """test the 'extract' function """
    a="USD"
    b="EUR"
    c="2.5"
    test1=exchange(a,b,c)
    i1=extract(test1)
    I1='2.1589225'
    assert (i1==I1)
    a="BWP"
    b="NZD"
    c="4.73"
    test2=exchange(a,b,c)
    i2=extract(test2)
    I2='0.66796788832763'
    assert (i2==I2)
def testAll():
    """test all cases"""
    test_exchange()
    test_extract()
    print("All tests passed")
def main():
    """input,test,then output"""
    x=input()
    y=input()
    z=input()
    q=exchange(x,y,z)
    s=extract(q)
    print(s)
    testAll() 
if __name__=="__main__":
    main()
