while True:
   
   password = ("enter your password;")
   
   has_letter = any(ch.isalpha() for ch in password)
    
   has_number = any(ch.isalpha() for ch in password)
   
   is_valid = has_letter and has_number
   
   
   if is_valid:
       print ("password is valid")
       break
   else:
       print ("invalid password")