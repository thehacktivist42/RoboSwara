import random
a = open('Atlas_A.txt','r')
b = open('Atlas_B.txt','r')
c = open('Atlas_C.txt','r')
d = open('Atlas_D.txt','r')
e = open('Atlas_E.txt','r')
f = open('Atlas_F.txt','r')
g = open('Atlas_G.txt','r')
h = open('Atlas_H.txt','r')
i = open('Atlas_I.txt','r')
j = open('Atlas_J.txt','r')
k = open('Atlas_K.txt','r')
l = open('Atlas_L.txt','r')
m = open('Atlas_M.txt','r')
n = open('Atlas_N.txt','r')
o = open('Atlas_O.txt','r')
p = open('Atlas_P.txt','r')
q = open('Atlas_Q.txt','r')
r = open('Atlas_R.txt','r')
s = open('Atlas_S.txt','r')
t = open('Atlas_T.txt','r')
u = open('Atlas_U.txt','r')
v = open('Atlas_V.txt','r')
w = open('Atlas_W.txt','r')
x = open('Atlas_X.txt','r')
y = open('Atlas_Y.txt','r')
z = open('Atlas_Z.txt','r')
a = list(a.read().split())
b = list(b.read().split())
c = list(c.read().split())
d = list(d.read().split())
e = list(e.read().split())
f = list(f.read().split())
g = list(g.read().split())
h = list(h.read().split())
i = list(i.read().split())
j = list(j.read().split())
k = list(k.read().split())
l = list(l.read().split())
m = list(m.read().split())
n = list(n.read().split())
o = list(o.read().split())
p = list(p.read().split())
q = list(q.read().split())
r = list(r.read().split())
s = list(s.read().split())
t = list(t.read().split())
u = list(u.read().split())
v = list(v.read().split())
w = list(w.read().split())
x = list(x.read().split())
y = list(y.read().split())
z = list(z.read().split())
print("Welcome to the Atlas Game!\n The rules are simple: you have to type a word, and then I will type a word that will start with the same letter, as your word ends. This cycle continues. Type 'exit()' to exit Let's begin!")
inp = ""
while inp != "exit()":
    inp = input('>')
    inp = inp.lower()
    end = inp[-1]
    if end == 'a':
        print(random.choice(a))
    if end == 'b':
        print(random.choice(b))
    if end == 'c':
        print(random.choice(c))
    if end == 'd':
        print(random.choice(d))
    if end == 'e':
        print(random.choice(e))
    if end == 'f':
        print(random.choice(f))
    if end == 'g':
        print(random.choice(g))
    if end == 'h':
        print(random.choice(h))
    if end == 'i':
        print(random.choice(i))
    if end == 'j':
        print(random.choice(j))
    if end == 'k':
        print(random.choice(k))
    if end == 'l':
        print(random.choice(l))
    if end == 'm':
        print(random.choice(m))
    if end == 'n':
        print(random.choice(n))
    if end == 'o':
        print(random.choice(o))
    if end == 'p':
        print(random.choice(p))
    if end == 'q':
        print(random.choice(q))
    if end == 'r':
        print(random.choice(r))
    if end == 's':
        print(random.choice(s))
    if end == 't':
        print(random.choice(t))
    if end == 'u':
        print(random.choice(u))
    if end == 'v':
        print(random.choice(v))
    if end == 'w':
        print(random.choice(w))
    if end == 'x':
        print(random.choice(x))
    if end == 'y':
        print(random.choice(y))
    if end == 'z':
        print(random.choice(z))
