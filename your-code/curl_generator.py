

# Generate curl command

inputs = {
    'username':'JMark1991',
    'token':'c4ba010c2492abf5ee237fede565f8f8e3860e65',
    'request_type':'repos',
    'args':'JMark1991/lab-dataframe-calculations/commits'
}

curl_command = f"\n\ncurl -u {inputs['username']}:{inputs['token']} https://api.github.com/{inputs['request_type']}/{inputs['args']} > {inputs['request_type']}_output2.json\n\n"
print(curl_command)