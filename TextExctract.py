import os
import re

dir_list = os.listdir('data/')

for file_name in dir_list:
    file_name = file_name.split('.')[0]
    with open(f'data/{file_name}.xml', 'r') as file:
        content = file.read()
    print(file_name, " \n")

    
    try: #extract body if body exists, if not -> go to next file_name
        body = re.search(r'<body>(.*?)</body>', content, re.DOTALL).group(1)
    except:
        continue
    
    #Remove all XML tags
    text = re.sub(r'<[^>]+>', '', body)

    #filter out lines starting with a backslash
    filtered_lines = [line for line in text.splitlines() if not line.strip().startswith('\\')]

    cleaned_text = '\n'.join(filtered_lines)

    with open(f'text/{file_name}.txt', 'w') as f:
        f.write(cleaned_text)
