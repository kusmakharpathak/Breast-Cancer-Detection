from model.user.admin import Admin
from model.user.user import Users


class Main:
    @staticmethod
    def main():
        count: int = 0
        print("\n\n*******************************************************************************")
        email = input("Enter your email ==>\t")
        while count < 3:
            if not Admin.find_by_email(email):
                print("\n\n*******************************************************************************")
                print("Sorry we could not find your email")
                email = input("Enter your email again ==>\t")
            else:
                admin = Admin.find_by_email(email)
                admin_id = admin.id
                print(admin_id)
                print("\n\n*******************************************************************************")
                password = input("Enter your password ==>\t")
                if Admin.login(email, password):
                    while True:
                        print("\n\n*******************************************************************************")
                        print("Welcome To breast Cancer Detection Admin Panel")
                        print("1. View Doctors Record\n2. Add Doctors\n3. Remove Doctors\n4. Logout\nPress any key and Enter to exit")
                        choice = int(input("Enter your choice ==>\t"))
                        if choice == 1:
                            val = Users.find_all()
                            for i in range(len(val)):
                                print("\n---------------------------------------------")
                                print(f"First name = {val[i].f_name}")
                                print(f"Last name = {val[i].l_name}")
                                print(f"Contact no = {val[i].contact_no}")
                                print(f"Address = {val[i].address}")
                                print(f"Specialist = {val[i].specialist}")
                                print(f"Email = {val[i].email}")
                            print("---------------------------------------------\n")

                        elif choice == 2:
                            print("\n\n*******************************************************************************")
                            f_name = input("Enter First Name ==>\t")
                            l_name = input("Enter Last Name ==>\t")
                            address = input("Enter Address ==>\t")
                            contact_no = input("Enter Contact No ==>\t")
                            specialist = input("Enter Specialist ==>\t")
                            email = input("Enter Email ==>\t")
                            password = input("Enter Password ==>\t")
                            # cls, f_name: str, l_name: str, address: str, contact_no: str, specialist: str, email: str, password: str
                            if Users.find_by_email(email):
                                print("Email already registered")
                            else:
                                Users.add_doctor(f_name, l_name, address, contact_no, specialist, email, password)

                        elif choice == 3:
                            email = input("Enter contact no ==>\t")
                            if Users.remove_doc(email):
                                print("\n\n*******************************************************************************")
                                print("Removed Success")
                            else:
                                print("\n\n*******************************************************************************")
                                print("Something Error")
                        elif choice == 4:
                            break
                        else:
                            exit()
                elif count < 2:
                    print("\n\n*******************************************************************************")
                    print("Sorry, Password does not match\nTry again!")
                    count += 1
                else:
                    print("Sorry")
                    break


if __name__ == '__main__':
    Main.main()
