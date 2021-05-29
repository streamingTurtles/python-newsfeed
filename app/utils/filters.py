




def format_date(date):
  return date.strftime('%m/%d/%y')


from datetime import datetime
print(format_date(datetime.now()))


# This code removes all extraneous information from a URL string, leaving only the domain name. Note that the methods we use, like replace() and split(), behave exactly the same as they do in JavaScript.
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]



# Run the script again, and confirm that both print() statements output "google.com"
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))


#  to address the issue of correctly pluralizing words.
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# Run the script again to confirm that it pluralizes "cats" while keeping "dog" singular.
print(format_plural(1, 'cat'))
print(format_plural(3, 'dog'))  