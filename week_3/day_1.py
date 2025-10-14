# ========CONTROL STRUCTURE======

# Conditions

# If statement

# if True:
#     print("I am following road A")
# else:
#     print("I am following road B")

# if False:
#           print("I am following road A")
# else:
#     print("I am following road B")


destination_fee = 1000
transport_fee = 900
train = "available"

# if transport_fee <= destination_fee:
#     print(f"{"==" * 24}\nGetting to destination Successful.\n{"==" * 24}")
# else:
#     print(f"{"==" * 24}\nGetting to destination Unsuccessful.\n{"==" * 24}")

if transport_fee <= destination_fee and train == "available":
    print(f"{"==" * 24}\nGetting to destination Successful.\n{"==" * 24}")
elif transport_fee <= destination_fee and train != "available":
    print(f"{"==" * 24}\nTrain Not Available.\n{"==" * 24}")
else:
    print(f"{"==" * 24}\nGetting to destination Unsuccessful.\n{"==" * 24}")
