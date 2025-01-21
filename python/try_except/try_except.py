try:
  print(x) # try block generates an error because x is not defined
except:
  print("An exception occurred") # this will be executed as the try block raises error



# note: Without the try block, the program will crash and raise an error

# print(x) # error || the   program crashes


# MULTIPLE EXCEPTIONS

try:
  print(y)
except NameError:
  print("Variable x is not defined") # this gets executed
except:
  print("Something else went wrong")


# or

try:
  print(y)
except ReferenceError:
  print('Referece error')
except:
  print('SOMETHING ELSE went wrong') # this gets executed


# -----------------------------------------------------------------------------

# ELSE

try:
  print("Hello") # this gets executed
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") # this also gets executed



# -------------------------------------------------

# FINALLY

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") # gets printed no matter what


  # ____________________________________________________


# NESTED TRY EXCEPT
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")




# _________________________________________________________________________________________

# RAISE an Exception

# To throw (or raise) an exception, use the raise keyword

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# ------------

y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")






