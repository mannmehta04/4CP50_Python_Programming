name = "John"
greeting = "Hello, " + name + "!"
print(greeting)

message = "The quick brown fox jumps over the lazy dog."
print(message[4:9])

age = 30
message = "My name is {} and I am {} years old."
formatted_message = message.format("John", age)
print(formatted_message)

text = "The rain in Spain falls mainly on the plain."
new_text = text.replace("rain", "snow")
print(new_text)

sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")
print(fruits)

joined_fruits = "-".join(fruits)
print(joined_fruits)