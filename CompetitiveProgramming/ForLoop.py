# ১। একটা পাইথন প্রোগ্রাম লিখতে হবে যা দিয়ে ১৫০০ থেকে ২৭০০ এর ভিতর নাম্বারগুলো খুঁজে বের করতে হবে, যেগুলো মূলত ৭ এবং ৫ দ্বারা বিভাজ্য।
#solve
# We define a dic for assign those number
store = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0):
        store.append(str(x))
print(','.join(store))

# ২।
