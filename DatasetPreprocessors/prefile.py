'''
1. approved_by
    2. author
3. author_flair_css_class
4. author_flair_text
5. banned_by
6. created
    7. created_utc
8. distinguished
9. downs
10. edited
11. gilded
    12. id
13. is_self
14. link_flair_css_class
15. link_flair_text
    16. num_comments
17. num_reports
    18. over_18
19. score
    20. selftext
    21. subreddit
    22. title
23. ups
    24. url
'''
import time
start_time = time.time()
#with open("posts_with_comments", "a") as fw:
with open("Flatfile_submissions") as f:
    line = f.readline()
    while line:
        items = line.split(",")
        if len(items) == 24 and items[15].isdigit():
            if items[19] != '""' :
                #fw.write("%s,%s,%s,%s,%s,%s,%s,%s,%s" % (items[1], items[6], items[11], items[15], items[17], items[19], items[20], items[21], items[23]))
                print "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (items[1], items[6], items[11], items[15], items[17], items[19], items[20], items[21], items[23])
        line = f.readline()
print("--- %s seconds ---" % (time.time() - start_time))