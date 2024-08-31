from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")

# print("type of config: ", type(config))
# print("config=", config)

rails = LLMRails(config)

user_greeting = "Sup!"

response = rails.generate(messages=[{
  "role": "user",
  "content": user_greeting
}])

# print("response 1=", response)
print("\n\n")

print("\nresponse 1=", response['content'])

response = rails.generate(messages=[{
  "role": "user",
  "content": user_greeting
},
{
  "role": "assistant",
  "content": response['content']
},
{
  "role": "user",
  "content": "What is the capital of France?"
}])

print("\nresponse 2=", response['content'])