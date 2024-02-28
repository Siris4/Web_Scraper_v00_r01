from bs4 import BeautifulSoup
import requests
# import chardet

response = requests.get("https://news.ycombinator.com/news")    # removed: , verify=False)
webpage_html_document = response.text
print(webpage_html_document)

soup = BeautifulSoup(webpage_html_document, "html.parser")  # we want to pass the html document that we want to parse (yc_webpage), then we provide the Method of which we are going to parse it with.
# NOW: dig in, and find the parts that we want out of the html doc.

# print(soup.title)  # For example, if we want the tab Title name, use print(soup.title)

  # what if we wanted to get a hold of the text that is the title of the first story link?

article_tag_first_yc_story_link = soup.find(name="a", href="https://overkill.wtf/nintendo-sue-yuzu-emulator/")

print(f"The <a> tag line is: {article_tag_first_yc_story_link}")    # the <a> tag line:  <a href="https://overkill.wtf/nintendo-sue-yuzu-emulator/">Nintendo is suing the creators of Switch emulator Yuzu</a>
print(f"The .getText Method of article_tag_first_yc_story_link is: {article_tag_first_yc_story_link.getText()}\n")  # to GET the Text INSIDE/WITHIN the anchor tag:

print(f"The Title of the article is: {article_tag_first_yc_story_link.text}")   # text of the article title itself: Nintendo is suing the creators of Switch emulator Yuzu


article_text = article_tag_first_yc_story_link.getText()
article_link = article_tag_first_yc_story_link.get("href")  #looking for the Value: href
article_upvote = soup.find(name="span", class_="score")  # <span class="score" id="score_39530203">480 points</span>

# print(article_text)
print(f"The article link itself is: {article_link}")
print(f"The Upvote point score.text is currently: {article_upvote.text}")
print(f"The Upvote point score.getText() is currently: {article_upvote.getText()}")

# OR:

article_upvote = soup.find(name="span", class_="score").getText()  # <span class="score" id="score_39530203">480 points</span>
print(f"Using a different Method of .getText(), the article_upvote is: {article_upvote}")






# <a href="https://overkill.wtf/nintendo-sue-yuzu-emulator/">




# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()    #you must indent!!
#     # print(contents)
#
# #BeautifulSoup is the class
#
# #then, we create an object from that Class, pass in the contents, and then the parser)
# soup = BeautifulSoup(contents, "html.parser")   # or use lxml for XML content, if HTML is not working
#
# print(soup)
#
# print(f"The title tag (soup.title) is: {soup.title}")
# print(f"The name of that particular title tag (title.name) is: {soup.title.name}")
# print(f"The string that is contained inside the title tag (title.string) is: {soup.title.string}\n")
#
# print(f"The soup.heading (Heading) is: {soup.heading}")
# print(f"The soup.h3 (Heading - level 3) is: {soup.h3}")
# print(f"The soup.class (Class) is {soup.__class__}")
#
# print(soup.prettify())
#
# # to find the first anchor tag in the website, use:
# print(soup.a)
#
# # the first list item (li):
# print(soup.li)
#
# #the first paragraph only:
# print(soup.p)
#
# # ALL of the items of a particular group:
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)
#
# all_list_item_tags = soup.find_all(name="li")
# print(all_list_item_tags)
#
#
# # What if I wanted to get a hold of all of the text from just the anchor tags? Yup, we use a For Loop:
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# # OK, what about getting a hold of all of the links/URLs themselves? (href):
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# # To Search / get a hold of an item by it's attribute / attribute name:
# # you can isolate an h1, h2, h3 etc by it's id=:
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# # Finding and selecting the Class element of a soup:
# section_heading = soup.find(name="h3", class_="heading")   #we cannot use the 'class' keyword, because it is reserved for class CREATION (code is already taken by another method)
#                                                             # so, we use 'class_' UNDERscore immediately after the class keyword
#
# print(section_heading)          #the whole heading tag
# print(section_heading.getText())    #get the text within that heading
# print(section_heading.name)   #name of that particular tag
# print(section_heading.get("class"))   # if we want to get a hold of a value of an attribute (this example gets the Class value)
#
# company_url = soup.select_one(selector="p a")  # select the first one that is an <a> tag, that sits inside a <p> tag, the "p a" string is the CSS Selector:
# print(company_url)
#
# #selector ID:
# name = soup.select_one(selector="#name")  # we want to get a hold of 'name' within the HTML file.
# print(name)
#
#
# # Select an Element by Class: (Ex: to select ALL of the elements that have a Class of ‘heading’):
# headings = soup.select(".heading")    # or selector=".heading"   (CSS Classes start with . )
# print(headings)





