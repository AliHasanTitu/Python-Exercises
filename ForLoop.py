# ১। একটা পাইথন প্রোগ্রাম লিখতে হবে যা দিয়ে ১৫০০ থেকে ২৭০০ এর ভিতর নাম্বারগুলো খুঁজে বের করতে হবে, যেগুলো মূলত ৭ এবং ৫ দ্বারা বিভাজ্য।
# solve
# We define a dic for assign those number
store = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0):
        store.append(str(x))
print(','.join(store))

# ২। সেলসিয়াস তাপমাত্রাকে ফারেনহাইটে এবং ফারেনহাইট তাপমাত্রাকে সেলসিয়াস স্কেলে কনভার্ট করা। 
# solveঃ
# প্রথমে ইউজার থেকে একটা সংখ্যা নিব। যা অবশ্যই ফারেনহাইট অথবা সেলসিয়াস স্কেলে হতে হবে। স্কেল নির্ধারণ করার জন্য অবশ্যই ইউজারজে সংখ্যার শেষে সাইন দিতে হবে। যেমন, ফারেনহাইটের জন্য F এবং সেলসিয়াসের জন্য C।
user_input_temp = input('Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ')
# ইউজার যা ইনপুট দিতে তা থেকে শেষের এককটা বাদ যাবে। যেমন, ইউজার ইনপুট দিলো 20C, এখান থেকে C বাদ যাবে।
degree = int(user_input_temp[:-1])
# আর এখানে ইউজারের ইনপুট দেওয়া 20C থেকে 20 বাদ যাবে শুধুমাত্র C একক অ্যাসাইন হবে sign_of_degree তে।
sign_of_degree = user_input_temp[-1]

# বিস্তারিত পরে লিখবো।
if sign_of_degree.upper() == 'C':
    result = int(round((9 * degree)/(5 + 32)))
    actual_sign_of_degree = "Fahrenheit"

elif sign_of_degree.upper() == "F":
    result = int(round((degree - 2)*(5 / 9)))
    actual_sign_of_degree = 'Celcius'

else:
    print('Input Proper Sign.')
    quit()

print("The temperature in", actual_sign_of_degree, "is", result, "degrees.")
