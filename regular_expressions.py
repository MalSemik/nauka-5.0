import re

date_pattern = r"[0123]?\d[-./]\d{1,2}[-./]\d{1,4}"
example_date_str = "01.22.1995"
bad_date_str = "01.33/dupa"
if re.match(date_pattern, example_date_str):
    print("Matches")


if re.match(date_pattern,bad_date_str):
    print(f"{bad_date_str} matches pattern {date_pattern}")
else:
    print(f"{bad_date_str} doesn't match pattern {date_pattern}")


print([letter for letter in 'ale jajca panie ferdku'])
print(re.search("(a)(b)(c)","abc").groups())

print(re.sub("(.*)=(.*)",r"\2=\1","dupa=10"))