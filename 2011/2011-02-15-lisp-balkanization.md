# Lisp Balkanization?
> | review | lisp |

I've heard this words' pair too often and I never knew what does it mean?

 Until I read these two posts: [Ultra-Balkanization Makes Lisp Autistic](http://gilesbowkett.blogspot.com/2008/02/ultra-balkanization-makes-lisp-autistic.html) and [Reddit and Lisp psychosis](http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html).

 In general every Lisp developer tends to write "new" super-puper Lisp, invent the wheel, write own "cool" emacs extension and tell to the world that he is a HACKER. I love this.

 Nowadays, Clojure is the real answer for Lisp guys. It can consolidate the Lisp language flexibility and JVM power. I think it's a good choice.

**Update** 2019-03-29: I have added original posts because it's more convenient to have them inline. All references have been preserved.

---

## [WebArchive Copy] Giles Bowkett: Ultra-Balkanization Makes Lisp Autistic

[Source](https://web.archive.org/web/20101201110952/http://gilesbowkett.blogspot.com/2008/02/ultra-balkanization-makes-lisp-autistic.html "Permalink to Giles Bowkett: Ultra-Balkanization Makes Lisp Autistic")

[An interesting perspective](https://web.archive.org/web/20101201110952/http://lua-users.org/lists/lua-l/2008-02/msg00247.html). It's too long, so I extracted key sentences expressing the idea I find interesting: [Lisp's hyper-specific DSL features](https://web.archive.org/web/20101201110952/http://www.paulgraham.com/onlisp.html) make Lisp programs autistic.

*A language is an interface between programmers and hardware, so it has social/psychological/pedagogical features which are just as important as its formal properties. Many Lisp zealots dismiss the language's failures as "merely social", but that's missing the purpose of a language entirely. Normal syntax gives you a feeling of what's idiomatic vs. what's weird. With sexps, it's much harder to create, maintain and convey such opinions in the code's appearance. Without this consensus you'll have a hard time building a functional social group. Since with Lisp you essentially design your own single-use language for your application, you're the only one in the world using that language variant.*

---

## [Copy] Finding Lisp: Reddit and Lisp psychosis

[Source](http://www.findinglisp.com/blog/2005/12/reddit-and-lisp-psychosis.html "Permalink to Finding Lisp")

I went away on a family vacation at the first part of this week and just got back last night. During that time, I completely missed the whole [Reddit](http://lemonodor.com/archives/001301.html) [scandal](http://pobox.com/~dnm/tdw/2005/12/contextinople.html). It seems like the guys at Reddit ended up choosing to [rewrite Reddit in Python](http://reddit.com/blog/2005/12/on-lisp.html) because Lisp just wasn't working for them. To some, this seems to be a slap in the face of Lisp. However, if you look at [spez's blog entry](http://reddit.com/blog/2005/12/on-lisp.html), you can see that the rationale for choosing Python was pretty sane.

In particular, this paragraph was interesting (also [quoted by John at Lemonodor](http://lemonodor.com/archives/001301.html)):

> Emacs and SLIME are a killer combination, but I develop on a Mac, and reddit.com is a FreeBSD box. On my Mac, my choices of threaded Lisp implementations was limited to OpenMCL, and in FreeBSD it's CMUCL. Because of the low-level socket and threading code we had to write, reddit would not run on my Mac, and I was always tethered to our FreeBSD development server. Not being able to program offline is a pain.

In a comment on [Lemonodor](http://lemonodor.com/archives/001301.html), Steve Huffman said:

> The biggest trouble that plagued us was that we could never quite get Lisp reddit stable enough to sleep at night. There were weird threading issues that would bring the site to its knees a couple times a day and required constant monitoring.

Now, here's where the Lisp psychosis comes in. Rather than suggesting that the guys at Reddit were dopes, or that they didn't try hard enough, or that they should have done such and such a workaround, blah, blah, I wish Lispers would step up and internalize that the Reddit experience was a great case study and that the community should work to solve the issues it raised. These guys did not have a bad Lisp experience. In fact, they are quite complimentary of Lisp. For [example](http://reddit.com/blog/2005/12/on-lisp.html):

> Lisp is an amazing language. After spending the entire summer working entirely in Lisp, it's nearly impossible to work in another language and not say to myself, "If only this were Lisp..." Lisp has many goodies that make programming in it a joy: the REPL, macros and the lack of syntax are some. I won't go into the details, but rest assured, it's cool. People become Lisp zealots for a reason.

So here's what I took away from the Reddit feedback:

1. Lisp is a great language. Keep this point in mind. The Reddit developers gave Lisp compliments; they didn't 'diss it.
2. Lisp has a balkanized feature set. Some (necessary!) things to build modern applications are not cross-platform. When you have to work on multiple machines and environments, which is more and more the norm these days, there are no open source implementations of Lisp that run across the dominant environments without differences. (CLISP comes the closest, but you may or may not be able to tolerate its GPL license terms.) Because these features are not standardized, you're left writing compatibility layers if you want things to work across platforms.
3. In particular, networking and threading are problem areas.
4. Lisp libraries are scant. This is a well known problem in the Lisp community. The standard, basically valid, response is "Jump in and help us write some more libraries." (Kudos to Kenny Tilton for driving this line hard. He's right, but there's also a bit more to it than that.)
5. The library problems are compounded by the balkanization of feature set. In some cases you can find something that sort of works, but it may work on another implementation, not yours. If it has any dependencies on the problem areas of threads and networking, you've got a long road of tweaking ahead to get it to work. This time is better spent getting on with your real task.
6. [Edi Weitz](http://weitz.de/) (yet again) wins the Lisp Superhero award for creating the best libraries out there, bar none. Seriously, if anybody aspires to create libraries that are well-used, go take some cues from Edi. His code is always high quality, his APIs and implementations are always complete, he's absolutely responsive to problem reports, he provides great documentation, and he often tests his code across multiple implementations, trying to make them as cross-platform as possible. In short, you couldn't expect better service and support from a commercial vendor, and Edi releases his code as open source.

Okay, all that said, what's the constructive response here? My suggestions are:

1. First, stop grumbling and suggesting workarounds to the Reddit folks. They did the Lisp community a great service by documenting their experiences. Rather than harrassing them, sit down and talk with them to get more info.
2. Next, focus on the foundational balkanization problems. In my opinion, the biggest issues with Lisp are the lack of standard (defacto or otherwise) networking and threading APIs. If those were in place, it would be a lot easier to get libraries that worked all over the place. Would this solve everything? No, but it would go a long way and would enable lots of other innovation on top of that foundation instead of having everybody spending time creating compatibility libraries and generally re-inventing the wheel.
3. Work on getting a good cross-platform, open source Lisp implementation with a liberal license. Like I said previously, I really like [CLISP](http://clisp.cons.org/), and I use it for developing on Windows, but the license is not suitable for all code since it all-but-forces your code to be released as GPL. I'd really love to see [SBCL](http://www.sbcl.org/) or [CMUCL](http://www.cons.org/cmucl/) ported to Windows, with the full set of functionality. I'd also love to see SBCL's baseline functionality present on all platforms (currently threading only works on Linux, for instance, not BSD). By the way, this is no knock on any other Lisp implementation. I just happen to use SBCL on Linux and think it rocks. If [OpenMCL](http://openmcl.clozure.com/) can make the jump off of Mac onto other platforms, that would be great. Or maybe [GCL](http://www.gnu.org/software/gcl/gcl.html) can do the job. I don't know the exact route, but the fact is the lack of a baseline functionality across all platforms is hurting us.

Can I do all the above? Nope. I've tried grokking the internals of SBCL and I'm only qualified to kibitz around the margins. I stand in awe of guys like William, Christophe, Dan, Nikodemus, Gabor, Juho, Alexey, and many others (Update: I added to this list twice already because I felt so bad for leaving out somebody's name--sorry William and Nikodemus. If you're a significant SBCL contributor--or even and insignificant one--believe me when I say I stand in awe of you too ;-). I do try to help out SBCL by reducing the friction for newbies to get started with Lisp, compiling the RPM binaries that are available on [SourceForge](http://sourceforge.net/projects/sbcl/) and maintaining the [FedoraLisp.org](http://www.fedoralisp.org/) Yum repository.

That said, I'm going to start working on the networking API issues. You'll see a document from me posted over the next couple of weeks. It's been in process for a few months, but I finally got a hankering to finish it with this Reddit bru-ha-ha. If you're interested in networking APIs and have a desire to help in such an endeavor, please drop me a line (dave at findinglisp). I'd love to spread the work around. If somebody else wants to grab the threading stuff by the throat that would be great.

Above all, stay productive. Use the Reddit feedback to motivate you to make Lisp better. Whatever you do, stop suggesting workarounds to the Reddit guys or making them feel bad for the choices they made. They seem like smart guys, so let's assume that they did what they did knowing all the options (they do have [Paul Graham](http://www.paulgraham.com/) on the board, so I'm guessing that they talked about this before they did the rewrite). They have moved on and our job is to make any such workaround unnecessary for the next crew that tries to use Lisp.

And before anybody says it, yes I know that the commercial Lisp vendors have solved some of these problems. I have discussed before [some of my thoughts about the various license terms the vendors use](http://www.findinglisp.com/blog/2004/11/more-rad-thoughts.html). It isn't that those terms are bad in the abstract, they just don't allow those implementations to solve the problem I'm interested in. In short, I think it would help drive Lisp adoption if a common, cross-platform, free, open source version existed, in the same way that GCC has helped democratize programming in C. The next-best alternative would be a $99 "Turbo Lisp" environment ala Borland's language products in the 1980s/1990s. Perhaps the [Lispworks](http://www.lispworks.com/) guys will offer such a thing (hint, hint ;-).
