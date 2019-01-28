# :email: Emails country extractor

This Python script will allow you to extract, from an `<email>:<xxx>` list, emails from a given country. Extracting from multiple text files is completely possible and the script also handle the `;` delimiter.

## Example

Let's say that you own a text file (or more) containing a bunch of emails and you only want the ones from France.

    test1@test.com:test
    test2@test.fr:test
    test3@test.FR:test
    test4@test.ru:test
    test5@test.com:test
    test6@test.be:test
    ...

The script will create a new `OUT.txt` file containing those emails :

    test2@test.fr:test
    test3@test.fr:test
Cool, huh?

## How to use

 1. First of all, you need to have [Python](https://www.python.org/)  installed on your machine.

 2. By default, the script will extract **emails from France**. If you want to handle another country, open the `script.py` file and edit the `language` variable *(line 12)*. *Examples:* `'fr'`, `'com'`, `'co.uk'`, `'ru'`, `'be'`, ...

 3. When the specific country has been set as you wanted to, simply put the **.txt** files you want in the **`IN/`** directory and run the script by typing :
``` bash
$ python script.py
```
 4. It's done! The extracted emails will be automatically put in a new `OUT.txt` file within a few seconds.
