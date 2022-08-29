import numbers


name_1=input("what is your name :")
name_2=input("what is your name :")
name_3=input("what is your name :")

Slices_in_the_pizza=input("how many slice in the pizza :")
price_of_pizza=input("what is the price of the pizza :")

percentge_ate_by_the_person_1=input(name_1+"what is the percentage of thr pizza you have ate :")
percentge_ate_by_the_person_2=input(name_2+"what is the percentage of thr pizza you have ate: ")
percentge_ate_by_the_person_3=input(name_3+"what is the percentage of thr pizza you have ate :")

numbers_of_slices_ate_person_1=float(percentge_ate_by_the_person_1)*float(Slices_in_the_pizza)
numbers_of_slices_ate_person_2=float(percentge_ate_by_the_person_2)*float(Slices_in_the_pizza)
numbers_of_slices_ate_person_3=float(percentge_ate_by_the_person_3)*float(Slices_in_the_pizza)

price_payed_by_name_1=float(percentge_ate_by_the_person_1)*float(price_of_pizza)
price_payed_by_name_2=float(percentge_ate_by_the_person_2)*float(price_of_pizza)
price_payed_by_name_3=float(percentge_ate_by_the_person_3)*float(price_of_pizza)

print(name_1+" have ate "+str(numbers_of_slices_ate_person_1)+" slaices and have payed "+str(price_payed_by_name_1)+" $ for this meal ")
print(name_2+" have ate "+str(numbers_of_slices_ate_person_2)+" slaices and have payed "+str(price_payed_by_name_2)+" $ for this meal ")
print(name_3+" have ate "+str(numbers_of_slices_ate_person_3)+" slaices and have payed "+str(price_payed_by_name_3)+" $ for this meal ")

total_price_to_pay=price_payed_by_name_1+price_payed_by_name_2+price_payed_by_name_3
print(" TOTAL AMOUNT TO PAY: "+str(total_price_to_pay ))
print("Thanks for your visit")
