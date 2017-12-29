def longest_palindromic(t,l=len,d=divmod):
  return max([t[x:y] for x,y in(d(i,l(t)+1) for i in
    range((l(t)+1)**2))if t[x:y]==t[x:y][::-1]],key=len)


def longest_palindromic(text):
    return sorted([text[i:j] for i in range(len(text)+1) for j in range(len(text)+1) if text[i:j] == text[i:j][::-1] and len(text[i:j])>0 ],key=len,reverse=True)[0]
