from mod_python import apache
from mod_python import util


def reverse(s):
    return s[::-1]
 
def isPalindrome(s):

    rev = reverse(s)
    return rev

def index(req):
    req.content_type = "text/html"
    info = req.form
    strr = info['usr']
    
    ans = isPalindrome(strr)
    if ans == strr:
        req.write("<html><br><body><br><h2 style='color:green;'>given string is palindrome<br></h2><br></body><br></html>")
        
    else:
        req.write("<html><br><body><h2 style='color:red;'>given string is not palindrome</h2><br><body><br></html>")
    
    
    
        

