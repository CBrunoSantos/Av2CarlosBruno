clients_2_login = {
  "Manoel" : "manoel1@mail.com"
  , "Emmanoel" : "emmanoel1@mail.com"
}
login_2_password = {
  "manoel1@mail.com" : "123"
  , "emmanoel1@mail.com" : "1234"
}
inside = lambda l, p, l2p : l2p [l] == p if l in l2p.keys() else False
c2l = clients_2_login
l2p = login_2_password
cl_is_reg = lambda name : (lambda l, p : cl_log_pass (l, p, l2p)) if name in c2l.keys() else False
"ERROR"
cl_log_pass = lambda l, p, l2p : cl_logs_in () if inside (l, p, l2p) else (lambda l2, p2 :
cl_log_pass (l2, p2, l2p))
cl_logs_in = lambda : "SUCCESSFULL LOGIN! SETTINGS DISPLAYED"
start = cl_is_reg
print (start ("Manoel") ("manoel1@mail.com", "123"))
print (start ("Manoel") ("wrongmailnoel1@mail.com", "123") ("manoel1@mail.com", "123"))
print (start ("Manoel") ("wrongmailnoel1@mail.com", "123"))