
Example Inputs and Outputs
emails = ["john.doe@example.com", "jane_doe@domain.co", "JohnDoe123@domain.corporate", "@gmail.com"]

for email in emails:
  print(validate_email(email)) # True True False False

phone_numbers = ["123-456-7890", "(123) 456-7890",  "123 456 7890", "(123)-456-7890", "1234567890", "123.456.7890", "123-45-7890"]

for number in phone_numbers:
  print(validate_phone_number(number)) # True True True True True False False
