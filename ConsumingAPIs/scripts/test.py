from getrequest import getcall
from postrequest import postcallnoheaders,postcallheaders
from putrequest import putcall
from patchrequest import patchcall
from deleterequest import deletecall

print(getcall())
print()
postcallnoheaders()
print()
postcallheaders()
print()
putcall()
print()
patchcall()
print()
deletecall()