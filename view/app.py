from model.user.user import Users
from model.patient.patient import Patient


class Main:
    @staticmethod
    def main():
        count: int = 0
        email = input("Enter your email ==>\t")
        while count < 3:
            if not Users.find_by_email(email):
                print("Sorry we could not find your email")
                email = input("Enter your email again ==>\t")
            else:
                doc = Users.find_by_email(email)
                doc_id = doc.id
                print(doc_id)
                password = input("Enter your password ==>\t")
                if Users.login(email, password):
                    while True:
                        print("Welcome To breast Cancer Detection")
                        print("1. View Patents Record\n2. Add Patients\n3. Find Patients")
                        choice = int(input("Enter your choice ==>\t"))
                        if choice == 1:
                            val = Patient.find_all_by_doc_id(doc_id)
                            for i in range(len(val)):
                                print("---------------------------------------------")
                                print(f"First name = {val[i].f_name}")
                                print(f"Last name = {val[i].l_name}")
                                print(f"Contact no = {val[i].contact_no}")
                                print(f"Consultant = {doc.f_name} {doc.l_name}")
                            print("---------------------------------------------")

                        elif choice == 2:
                            f_name = input("Enter First Name ==>\t")
                            l_name = input("Enter Last Name ==>\t")
                            contact_no = input("Enter contact no ==>\t")
                            Patient.add_patient(f_name, l_name, contact_no, doc_id)
                        elif choice == 3:
                            contact_no = input("Enter contact no ==>\t")
                            a = Patient.find_by_contact_no(contact_no)
                            print(a.f_name)
                        else:
                            break
                elif count < 2:
                    print("Sorry, Password does not match\nTry again!")
                    count += 1
                else:
                    print("Sorry")
                    break

if __name__ == '__main__':
    Main.main()