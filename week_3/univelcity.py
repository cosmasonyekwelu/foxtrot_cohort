# input_value = input()
# print("The value i wrote in my terminal is:",input_value)

ui_ux_design = []
frontend_development = []
backend_development = []

print("Welcome to Univelcity")
name = input("What is your name")
course = input(
    f"What course are you planning to take?\n1. UI/UX design.\n2. Frontend Development\n3. Backend Development\n(Choose one 1/2/3): ")

if course == "1":
    ui_ux_design.append(name)
elif course == "2":
    frontend_development.append(name)
elif course == "3":
    backend_development.append(name)
else:
    print("You choses the wrong option. You are to choose between 1, 2 or 3.")

print("UI/UX Design:", ui_ux_design)
print("Frontend Development:", frontend_development)
print("Backend Development:", backend_development)
