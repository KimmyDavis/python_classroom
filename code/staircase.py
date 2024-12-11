'''
this is meant create a staircase from a string of text
'''


init_text = "hello world"
step = 0
words = init_text.strip().split()
longest = max([len(word) for word in words])
joined = "".join(init_text.strip().split())
big_step = 5
for i in range(20):
    current_word = words[i % len(words)]
    print(joined * ((step // len(joined)) + (i // big_step))
          + joined[:((step % len(joined)) + longest - len(current_word))]
          + "😁" 
          + current_word)
    step += 5
