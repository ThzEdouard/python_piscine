import time

print("Seconds since", time.strftime("%B %d, %Y", time.gmtime()),
      ":{:,.3f}".format(time.time()), "or", "{:.2e}".format(time.time()),
      "in scientific notation")
print(time.strftime("%b %d %Y", time.gmtime()))
