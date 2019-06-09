import re
import glob

# Path of the folder containing .txt files (expected to contain <email>:<xxx> data)
# Default: './IN/*.txt'
# The default value will select every .txt file in the IN/ directory
path = './IN/*.txt'

# Language of emails you want to extract (e.g. 'fr' | 'com' | 'co.uk' | 'ru')
# Default: 'fr'
# The default value will extract french emails
language = 'fr'

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

files = glob.glob(path)
for name in files:
    try:
        # Open each .txt file
        with open(name, encoding="ISO-8859-1") as s:
            for line in s:
                # Remove blank spaces and put each line in lowercase letters
                line = line.strip().lower()

                # Find lines containing '.fr:' or '.fr;'
                regex = re.compile(r"(\.%s(:|;))" %language)
                match = regex.search(line)
                if match is not None:
                    if has_cyrillic(line) is False:
                        # Define if the line is using ':' or ';'
                        ext = line.split('.%s' %language)[1][0]

                        # Reformat <email>:<xxx> data (some files may use the ';' delimiter which is not cool)
                        email = line.split(ext)[0]
                        xxx = line.split(ext)[1]

                        # Print in console and extract in 'OUT.txt' file
                        print('{}:{}'.format(email, xxx))
                        f = open('OUT.txt', 'a')
                        f.write(email+':'+xxx+'\n')
                        f.close()

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
