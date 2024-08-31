from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")

# print("type of config: ", type(config))
# print("config=", config)

rails = LLMRails(config)

response = rails.generate(messages=[{
  "role": "user",
  "content": "Hello! How are you??"
}])

print("response=", response)
print("\n\n")

print("response=", response['content'])