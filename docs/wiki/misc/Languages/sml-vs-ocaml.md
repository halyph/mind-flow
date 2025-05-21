---
tags:
  - ocaml
---

# SML and OCaml, Side by Side

!!! warning "Disclaimer"

    This is dump/copy of [Standard ML and Objective Caml, Side by Side](https://people.mpi-sws.org/~rossberg/sml-vs-ocaml.html)  
    Original version by Jens Olsson, jenso@csd.uu.se.  
    Last modified: 2011/01/18

    You may ask "*Why making copy instead of simple references to the source?*" -  
    Because, I'd like to have it as is without looking around internet when ppl decide to delete it.

This page gives a quick side by side comparison of program fragments in the two ML dialects Standard ML ('97 revision) and Objective Caml (version 3.12). It is primarily targetted at people who need to convert code between the two dialects. Where suitable we also mention common extensions to SML, or recent extensions of Ocaml. The comparison does not cover features that do not have an appropriate counter part in the sibling dialect (e.g. Ocaml's object sublanguage, SML's user-defined operator fixity, or advanced library issues).

## Literals

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
- 3; <br/>
> val it = 3 : int <br/>
</code> </td>
<td> <code>
# 3;; <br/>
- : int = 3 <br/>
</code> </td> </tr>

<tr> <td> <code>
- 3.141; <br/>
> val it = 3.141 : real <br/>
</code> </td>
<td> <code>
# 3.141;; <br/>
- : float = 3.141 <br/>
</code> </td> </tr>

<tr> <td> <code>
- "Hello world"; <br/>
> val it = "Hello world" : string <br/>
</code> </td>
<td> <code>
# "Hello world";; <br/>
- : string = "Hello world" <br/>
</code> </td> </tr>

<tr> <td> <code>
- #"J"; <br/>
> val it = #"J" : char <br/>
</code> </td>
<td> <code>
# 'J';; <br/>
- : char = 'J' <br/>
</code> </td> </tr>

<tr> <td> <code>
- true; <br/>
> val it = true : bool <br/>
</code> </td>
<td> <code>
# true;; <br/>
- : bool = true <br/>
</code> </td> </tr>

<tr> <td> <code>
- (); <br/>
> val it = () : unit <br/>
</code> </td>
<td> <code>
# ();; <br/>
- : unit = () <br/>
</code> </td> </tr>

<tr> <td> <code>
- (3, true, "hi"); <br/>
> val it = (3, true, "hi") : int * bool * string <br/>
</code> </td>
<td> <code>
# (3, true, "hi");; <br/>
- : int * bool * string = 3, true, "hi" <br/>
</code> </td> </tr>

<tr> <td> <code>
- [1, 2, 3]; <br/>
> val it = [1, 2, 3] : int list <br/>
</code> </td>
<td> <code>
# [1; 2; 3];; <br/>
- : int list = [1; 2; 3] <br/>
</code> </td> </tr>

<tr> <td> <code>
- #[1, 2, 3]; <br/>
> val it = #[1, 2, 3] : int vector <br/>
</code> <i>
Standard does not have vector literals but most implementations
support them &ndash; use library functions otherwise
</i> </td>
<td> <i>
Does not have vectors &ndash; use arrays
</i> </td> </tr>

<tr> <td> <i>
Does not have array literals &ndash; use library functions
</i> </td>
<td> <code>
# [|1; 2; 3|];; <br/>
- : int array = [|1; 2; 3|] <br/>
</code> </td> </tr>

</table>

## Expressions

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
~3*(1+7) div 2 mod 3 <br/>
</code> </td>
<td> <code>
-3*(1+7)/2 <font color="#0000ff">mod</font> 3 <br/>
</code> </td> </tr>

<tr> <td> <code>
~1.0/2.0 + 1.9*x <br/>
</code> </td>
<td> <code>
-1.0 /. 2.0 +. 1.9 *. x <br/>
</code> </td> </tr>

<tr> <td> <code>
a <font color="#0000ff">orelse</font> b
  <font color="#0000ff">andalso</font> c <br/>
<br/>
<br/>
</code> </td>
<td> <code>
a <font color="#0000ff">||</font> b <font color="#0000ff">&amp;&amp;</font> c <br/>
</code><i>or (deprecated)</i><code> <br/>
a <font color="#0000ff">or</font> b <font color="#0000ff">&amp;</font> c <br/>
</code> </td> </tr>

</table>

## Functions

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>
<tr> <td> <code>
<font color="#0000ff">fn</font> f <font color="#0000ff">=></font>
  <font color="#0000ff">fn</font> x <font color="#0000ff">=></font>
  <font color="#0000ff">fn</font> y <font color="#0000ff">=></font> f(x,y) <br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">fun</font> f <font color="#0000ff">-></font>
  <font color="#0000ff">fun</font> x <font color="#0000ff">-></font>
  <font color="#0000ff">fun</font> y <font color="#0000ff">-></font> f (x,y) <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">fun</font> f x y <font color="#0000ff">-></font>
  f (x,y) <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fn</font> 0 <font color="#0000ff">=></font> 0 <br/>
&nbsp;<font color="#0000ff">|</font> n <font color="#0000ff">=></font> 1 <br/>
</code> </td>
<td> <code>
<font color="#0000ff">function</font> 0 <font color="#0000ff">-></font> 0 <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#0000ff">|</font> n
  <font color="#0000ff">-></font> 1 <br/>
</code> </td> </tr>

<tr> <td> <code>
f o g <br/>
</code> </td>
<td> <code>
<font color="#0000ff">fun</font> x <font color="#0000ff">-></font> f (g x) <br/>
</code> </td> </tr>

<tr> <td> <code>

map SOME xs <br/>
</code> </td>
<td> <i>
Does not have first-class constructors &ndash; use function instead, e.g.
</i> <code> <br/>
map (<font color="#0000ff">fun</font> x
  <font color="#0000ff">-></font> Some x) xs <br/>
</code> </td> </tr>

<tr> <td> <code>
<br/>
map <font color="#0000ff">#</font>2 triples <br/>
map <font color="#0000ff">#</font>lab records <br/>
</code> </td>
<td> <i>
Does not have first-class selectors &ndash; use function instead, e.g.
</i> <code> <br/>
map (<font color="#0000ff">fun</font>
  (<font color="#0000ff">_</font>,x,<font color="#0000ff">_</font>)
  <font color="#0000ff">-></font> x) triples <br/>
map (<font color="#0000ff">fun</font> x
  <font color="#0000ff">-></font> x.lab) records <br/>
</code> </td> </tr>

<!--
<tr> <td> <code>
<br/>
map <font color="#0000ff">#</font>2 [("a",3,4), ("b",0,0), ("c",5,1)] <br/>
map <font color="#0000ff">#</font>age [{name="Alice", age=22}, {name="Bob", age=33}] <br/>
</code> </td>
<td> <i>
Does not have first-class selectors &ndash; use function instead, e.g.
</i> <code> <br/>
map (<font color="#0000ff">fun</font>
  (<font color="#0000ff">_</font>,x,<font color="#0000ff">_</font>)
  <font color="#0000ff">-></font> x) [("a",3,4); ("b",0,0); ("c",5,1)] <br/>
map (<font color="#0000ff">fun</font> x
  <font color="#0000ff">-></font> x.age) [{name="Alice"; age=22}; {name="Bob"; age=33}] <br/>
</code> </td> </tr>
-->

<tr> <td> <code>
f (inputLine stdIn) (inputLine stdIn) <br/>

</code> </td>
<td> <i>
Evaluation order is undefined for application &ndash; use <code><font color="#0000ff">let</font></code>, e.g. <br/>
</i><code>
<font color="#0000ff">let</font> line1 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
<font color="#0000ff">let</font> line2 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
f line1 line2
</code> </td> </tr>

</table>


## Control Flow

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">if</font> 3 > 2 <font color="#0000ff">then</font> "X"
  <font color="#0000ff">else</font> "Y" <br/>
</code> </td>
<td> <code>
<font color="#0000ff">if</font> 3 > 2 <font color="#0000ff">then</font> "X"
  <font color="#0000ff">else</font> "Y" <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">if</font> 3 > 2
  <font color="#0000ff">then</font> print "hello"
  <font color="#0000ff">else</font> () <br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">if</font> 3 > 2
  <font color="#0000ff">then</font> print_string "hello" <br/>
</code> <i>
Note: expression has to have type <code>unit</code>
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">while</font> true <font color="#0000ff">do</font> <br/>
&nbsp;&nbsp; print "X" <br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">while</font> true <font color="#0000ff">do</font> <br/>
&nbsp;&nbsp; print_string "X" <br/>
<font color="#0000ff">done</font> <br/>
</code> </td> </tr>

<tr> <td> <i>
Does not have <code><font color="#0000ff">for</font></code> loops &ndash;
use recursion or <code><font color="#0000ff">while</font></code>
</i> </td>
<td> <code>
<font color="#0000ff">for</font> i <font color="#0000ff">=</font> 1
  <font color="#0000ff">to</font> 10
  <font color="#0000ff">do</font> <br/>
&nbsp;&nbsp; print_endline "Hello" <br/>
<font color="#0000ff">done</font> <br/>
</code> </td> </tr>

<tr> <td> <code>
(print "Hello "; <br/>
&nbsp;print "world") <br/>

</code> </td>
<td> <code>
print_string "Hello "; <br/>
print_string "world" <br/>
</code><i>or</i><code> <br/>
(print_string "Hello "; <br/>
&nbsp;print_string "world") <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">begin</font> <br/>
&nbsp;&nbsp; print_string "Hello "; <br/>
&nbsp;&nbsp; print_string "world" <br/>
<font color="#0000ff">end</font> <br/>
</code> </td> </tr>

</table>

## Value Declarations

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> name <font color="#0000ff">=</font> expr <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> name <font color="#0000ff">=</font> expr <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> f x y <font color="#0000ff">=</font> expr <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> f x y <font color="#0000ff">=</font> expr <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> <font color="#0000ff">rec</font> fib
  <font color="#0000ff">=</font>
  <font color="#0000ff">fn</font> n <font color="#0000ff">=></font> <br/>
&nbsp;&nbsp; <font color="#0000ff">if</font> n &lt; 2 <br/>
&nbsp;&nbsp; <font color="#0000ff">then</font> n <br/>
&nbsp;&nbsp; <font color="#0000ff">else</font> fib(n-1) + fib(n-2) <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">fun</font> fib n <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">if</font> n &lt; 2 <br/>
&nbsp;&nbsp; <font color="#0000ff">then</font> n <br/>
&nbsp;&nbsp; <font color="#0000ff">else</font> fib(n-1) + fib(n-2) <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">rec</font> fib
  <font color="#0000ff">=</font>
  <font color="#0000ff">fun</font> n <font color="#0000ff">-></font> <br/>
&nbsp;&nbsp; <font color="#0000ff">if</font> n &lt; 2 <br/>
&nbsp;&nbsp; <font color="#0000ff">then</font> n <br/>
&nbsp;&nbsp; <font color="#0000ff">else</font> fib (n-1) + fib (n-2) <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">let</font> <font color="#0000ff">rec</font> fib n
  <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">if</font> n &lt; 2 <br/>
&nbsp;&nbsp; <font color="#0000ff">then</font> n <br/>
&nbsp;&nbsp; <font color="#0000ff">else</font> fib (n-1) + fib (n-2) <br/>
</code> </td> </tr>

</table>

## Type Declarations

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">type</font> t <font color="#0000ff">=</font>
  int <font color="#0000ff">-></font> bool <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> t <font color="#0000ff">=</font>
  int <font color="#0000ff">-></font> bool <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">type</font> ('a,'b) assoc_list
  <font color="#0000ff">=</font>
  ('a <font color="#0000ff">*</font> 'b) list <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> ('a,'b) assoc_list
  <font color="#0000ff">=</font>
  ('a <font color="#0000ff">*</font> 'b) list <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">datatype</font> 'a option <font color="#0000ff">=</font>
  NONE <font color="#0000ff">|</font>
  SOME <font color="#0000ff">of</font> 'a <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> 'a option <font color="#0000ff">=</font>
  None <font color="#0000ff">|</font>
  Some <font color="#0000ff">of</font> 'a <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">datatype</font> t <font color="#0000ff">=</font>
  A <font color="#0000ff">of</font> int
  <font color="#0000ff">|</font> B <font color="#0000ff">of</font> u <br/>
<font color="#0000ff">withtype</font> u <font color="#0000ff">=</font>
  t <font color="#0000ff">*</font> t <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> t <font color="#0000ff">=</font>
  A <font color="#0000ff">of</font> int
  <font color="#0000ff">|</font> B <font color="#0000ff">of</font> u <br/>
<font color="#0000ff">and</font> &nbsp;u <font color="#0000ff">=</font>
  t <font color="#0000ff">*</font> t <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">datatype</font> v <font color="#0000ff">=</font>
  <font color="#0000ff">datatype</font> t <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> v <font color="#0000ff">=</font>
  t <font color="#0000ff">=</font>
  A <font color="#0000ff">of</font> int
  <font color="#0000ff">|</font> B <font color="#0000ff">of</font> u <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">datatype</font> complex <font color="#0000ff">=</font> C <font color="#0000ff">of</font> real <font color="#0000ff">*</font> real <br/>
<font color="#0000ff">fun</font> complex xy <font color="#0000ff">=</font> C xy <br/>
<font color="#0000ff">fun</font> coord (C xy) <font color="#0000ff">=</font> xy <br/>
<br/>
<br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> complex <font color="#0000ff">=</font> C <font color="#0000ff">of</font> float <font color="#0000ff">*</font> float <br/>
<font color="#0000ff">let</font> complex (x,y) <font color="#0000ff">=</font> C (x,y) <br/>
<font color="#0000ff">let</font> coord (C (x,y)) <font color="#0000ff">=</font> (x,y) <br/>
</code> <i>
or (note parentheses in type declaration)<br/>
</i> <code>
<font color="#0000ff">type</font> complex <font color="#0000ff">=</font> C <font color="#0000ff">of</font> (float <font color="#0000ff">*</font> float) <br/>
<font color="#0000ff">let</font> complex xy <font color="#0000ff">=</font> C xy <br/>
<font color="#0000ff">let</font> coord (C xy) <font color="#0000ff">=</font> xy <br/>
</code> </td> </tr>

</table>

## Matching

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> getOpt(NONE, d) <font color="#0000ff">=</font>
  d <br/>
&nbsp; <font color="#0000ff">|</font> getOpt(SOME x,
  <font color="#0000ff">_</font>) <font color="#0000ff">=</font> x <br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> get_opt <font color="#0000ff">=</font>
  <font color="#0000ff">function</font> <br/>
&nbsp;&nbsp; &nbsp; (None, d) <font color="#0000ff">-></font> d <br/>
&nbsp;&nbsp; <font color="#0000ff">|</font> (Some x,
  <font color="#0000ff">_</font>) <font color="#0000ff">-></font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> getOpt (opt, d) = <br/>
&nbsp;&nbsp; <font color="#0000ff">case</font> opt
  <font color="#0000ff">of</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; &nbsp; NONE <font color="#0000ff">=></font>
  d <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">|</font> SOME x
  <font color="#0000ff">=></font> x <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> get_opt (opt, d) <font color="#0000ff">=</font>
  <br/>
&nbsp;&nbsp; <font color="#0000ff">match</font> opt
  <font color="#0000ff">with</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; &nbsp; None <font color="#0000ff">-></font> d <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">|</font> Some x
  <font color="#0000ff">-></font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> take 0 xs  <font color="#0000ff">=</font>
  [] <br/>
&nbsp; <font color="#0000ff">|</font> take n nil <font color="#0000ff">=</font>
  <font color="#0000ff">raise</font> Empty <br/>
&nbsp; <font color="#0000ff">|</font> take n (x::xs)
  <font color="#0000ff">=</font> x :: take (n-1) xs <br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">rec</font> take n xs
  <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">match</font> n, xs
  <font color="#0000ff">with</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 0, xs  <font color="#0000ff">-></font> [] <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">|</font> n, []
  <font color="#0000ff">-></font> failwith "take" <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">|</font> n, x::xs
  <font color="#0000ff">-></font> x :: take (n-1) xs <br/>
</code> </td> </tr>

<tr> <td> <i>
Does not have guards &ndash; use <code><font color="#0000ff">if</font></code>
</i> </td>
<td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">rec</font> fac
  <font color="#0000ff">=</font> <font color="#0000ff">function</font> <br/>
&nbsp;&nbsp; &nbsp; 0 <font color="#0000ff">-></font> 1 <br/>
&nbsp;&nbsp; <font color="#0000ff">|</font> n <font color="#0000ff">when</font>
  n>0 <font color="#0000ff">-></font> n * fac (n-1) <br/>
&nbsp;&nbsp; <font color="#0000ff">|</font> <font color="#0000ff">_</font>
  <font color="#0000ff">-></font> raise Hell <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> foo(p <font color="#0000ff">as</font> (x,y))  <font color="#0000ff">=</font>
  (x,p,y)
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> foo ((x,y) <font color="#0000ff">as</font> p)
  <font color="#0000ff">=</font> (x,p,y) <br/>
</code> </td> </tr>

</table>

## Tuples

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">type</font> foo <font color="#0000ff">=</font>
  int <font color="#0000ff">*</font> float <font color="#0000ff">*</font>
  string <br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> foo <font color="#0000ff">=</font>
  int <font color="#0000ff">*</font> float <font color="#0000ff">*</font>
  string <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> bar <font color="#0000ff">=</font>
  (0, 3.14, "hi") <br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> bar <font color="#0000ff">=</font>
  0, 3.14, "hi" <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">let</font> bar <font color="#0000ff">=</font>
  (0, 3.14, "hi") <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">#</font>2 bar <br/>
<br/>
<br/>
<br/>
</code> </td>
<td> <i>
Does not have tuple selection &ndash; use pattern matching instead, e.g.
</i> <code> <br/>
<font color="#0000ff">let</font>
  <font color="#0000ff">_</font>,x,<font color="#0000ff">_</font>
  <font color="#0000ff">=</font> bar
  <font color="#0000ff">in</font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">#</font>2 <br/>
<br/>
<br/>
<br/>
</code> </td>
<td> <i>
Does not have first-class selectors &ndash; use function instead, e.g.
</i> <code> <br/>
<font color="#0000ff">function</font>
  <font color="#0000ff">_</font>,x,<font color="#0000ff">_</font>
  <font color="#0000ff">-></font> x <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">fun</font>
  (<font color="#0000ff">_</font>,x,<font color="#0000ff">_</font>)
  <font color="#0000ff">-></font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
(inputLine stdIn, inputLine stdIn) <br/>
<br/>
<br/>
</code> </td>
<td> <i>
Evaluation order is undefined for tuples &ndash; use <code><font color="#0000ff">let</font></code>, e.g. <br/>
</i><code>
<font color="#0000ff">let</font> line1 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
<font color="#0000ff">let</font> line2 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
(line1, line2)
</code> </td> </tr>

</table>

## Records

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">type</font> foo <font color="#0000ff">=</font>
  {x<font color="#0000ff">:</font>int, y<font color="#0000ff">:</font>float,
  s<font color="#0000ff">:</font>string ref} <br/>
</code> <i>
Note: record types need not be declared
</i> </td>
<td> <code>
<font color="#0000ff">type</font> foo <font color="#0000ff">=</font>
  {x<font color="#0000ff">:</font>int; y<font color="#0000ff">:</font>float;
  <font color="#0000ff">mutable</font> s<font color="#0000ff">:</font>string}
  <br/>
</code> <i>
Note: mutable field does not have the same type as a reference
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> bar <font color="#0000ff">=</font>
  {x<font color="#0000ff">=</font>0, y<font color="#0000ff">=</font>3.14,
  s<font color="#0000ff">=</font>ref ""} <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> bar <font color="#0000ff">=</font>
  {x<font color="#0000ff">=</font>0; y<font color="#0000ff">=</font>3.14;
  s<font color="#0000ff">=</font>""} <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">#</font>x bar <br/>
<font color="#0000ff">#</font>y bar <br/>
!(<font color="#0000ff">#</font>s bar) <br/>
</code> </td>
<td> <code>
bar<font color="#0000ff">.</font>x <br/>
bar<font color="#0000ff">.</font>y <br/>
bar<font color="#0000ff">.</font>s <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">#</font>x <br/>
<br/>
</code> </td>
<td> <i>
Does not have first-class selectors &ndash; use function instead, e.g.
</i> <code> <br/>
<font color="#0000ff">fun</font> r <font color="#0000ff">-></font>
  r<font color="#0000ff">.</font>x <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> {x<font color="#0000ff">=</font>x,
  y<font color="#0000ff">=</font>y, s<font color="#0000ff">=</font>s}
  <font color="#0000ff">=</font> bar <br/>
<font color="#0000ff">val</font> {y<font color="#0000ff">=</font>y, ...}
  <font color="#0000ff">=</font> bar <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">val</font> {x, y, s}
  <font color="#0000ff">=</font> bar <br/>
<font color="#0000ff">val</font> {y, ...}
  <font color="#0000ff">=</font> bar <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> {x<font color="#0000ff">=</font>x;
  y<font color="#0000ff">=</font>y; s<font color="#0000ff">=</font>s}
  <font color="#0000ff">=</font> bar <br/>
<font color="#0000ff">let</font> {y<font color="#0000ff">=</font>y}
  <font color="#0000ff">=</font> bar <br/>
</code><i>or (since Ocaml 3.12)</i><code> <br/>
<font color="#0000ff">let</font> {x; y; s}
  <font color="#0000ff">=</font> bar <br/>
<font color="#0000ff">let</font> {y; _}
  <font color="#0000ff">=</font> bar <br/>
</code> </td> </tr>

<tr> <td> <code>
{x <font color="#0000ff">=</font> 1,
  y <font color="#0000ff">=</font> <font color="#0000ff">#</font>y bar,
  s <font color="#0000ff">=</font> <font color="#0000ff">#</font>s bar} <br/>
<br/>
<br/>
</code> </td>
<td> <code>
{x <font color="#0000ff">=</font> 1;
  y <font color="#0000ff">=</font> bar<font color="#0000ff">.</font>y;
  s <font color="#0000ff">=</font> bar<font color="#0000ff">.</font>s} <br/>
</code><i>or</i><code> <br/>
{bar <font color="#0000ff">with</font> x <font color="#0000ff">=</font> 1} <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">#</font>s bar := "something" <br/>
</code> </td>
<td> <code>
bar<font color="#0000ff">.</font>s
  <font color="#0000ff">&lt;-</font> "something" <br/>
</code> </td> </tr>

<tr> <td> <i>
Does not have polymorphic fields
</i> </td>
<td> <code>
<font color="#0000ff">type</font> bar <font color="#0000ff">=</font>
  {f<font color="#0000ff">:</font>'a.'a <font color="#0000ff">-></font> int}
  <br/>
</code>
</td> </tr>

<tr> <td> <code>
{a <font color="#0000ff">=</font> inputLine stdIn, b <font color="#0000ff">=</font> inputLine stdIn} <br/>
<br/>
<br/>
</code> </td>
<td> <i>
Evaluation order is undefined for records &ndash; use <code><font color="#0000ff">let</font></code>, e.g. <br/>
</i><code>
<font color="#0000ff">let</font> line1 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
<font color="#0000ff">let</font> line2 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
{a <font color="#0000ff">=</font> line1; b <font color="#0000ff">=</font> line2}
</code> </td> </tr>

</table>

## References

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> r <font color="#0000ff">=</font> ref 0 <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> r <font color="#0000ff">=</font> ref 0 <br/>
</code> </td> </tr>

<tr> <td> <code>
!r <br/>
<br/>
<br/>
</code> </td>
<td> <code>
!r <br/>
</code><i>or</i><code> <br/>
r<font color="#0000ff">.</font>contents <br/>
</code> </td> </tr>

<tr> <td> <code>
r := 1 <br/>
<br/>
<br/>
</code> </td>
<td> <code>
r := 1 <br/>
</code><i>or</i><code> <br/>
r<font color="#0000ff">.</font>contents <font color="#0000ff">&lt;-</font> 1 <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> f(ref x) <font color="#0000ff">=</font> x <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> f {contents<font color="#0000ff">=</font>x}
  <font color="#0000ff">=</font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
r1 = r2 <br/>
r1 &lt;&gt; r2 <br/>
</code> </td>
<td> <code>
r1 == r2 <br/>
r1 != r2 <br/>
</code> </td> </tr>

</table>

## Comparisons

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
2 = 2 <br/>
2 &lt;&gt; 3 <br/>
</code> </td>
<td> <code>
2 = 2 <br/>
2 &lt;&gt; 3 <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> r <font color="#0000ff">=</font> ref 2 <br/>
r = r <br/>
r &lt;&gt; ref 2 <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> r <font color="#0000ff">=</font> ref 2 <br/>
r == r <br/>
r != ref 2 <br/>
</code> </td> </tr>

<tr> <td> <code>
(2, r) = (2, r) <br/>
(2, r) &lt;&gt; (2, ref 2) <br/>
</code> </td>
<td> <i>
Does not have a proper generic equality <br/>
(on one hand 
<tt>(2, r) != (2, r)</tt>, on the other
<tt>(2, r) <font color="#0000ff">=</font> (2, ref 2)</tt>)
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">case</font> String.compare(x,y)
  <font color="#0000ff">of</font> <br/>
&nbsp;&nbsp;&nbsp;&nbsp; LESS <font color="#0000ff">=></font> a <br/>
&nbsp;&nbsp;&nbsp;| EQUAL <font color="#0000ff">=></font> b <br/>
&nbsp;&nbsp;&nbsp;| GREATER <font color="#0000ff">=></font> c <br/>
</code> </td>
<td> <code>
<font color="#0000ff">match</font> compare x y
  <font color="#0000ff">with</font> <br/>
&nbsp;&nbsp;&nbsp;&nbsp; n <font color="#0000ff">when</font> n &lt; 0
  <font color="#0000ff">-></font> a <br/>
&nbsp;&nbsp;&nbsp;| 0 <font color="#0000ff">-></font> b <br/>
&nbsp;&nbsp;&nbsp;| <font color="#0000ff">_</font>
  <font color="#0000ff">-></font> c <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> f x y <font color="#0000ff">=</font>
  (x = y) <br/>
<font color="#0000ff">val</font> f <font color="#0000ff">:</font>
  ''a <font color="#0000ff">-></font> ''a <font color="#0000ff">-></font>
  bool <br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> f x y <font color="#0000ff">=</font>
  (x = y) <br/>
<font color="#0000ff">val</font> f <font color="#0000ff">:</font>
  'a <font color="#0000ff">-></font> 'a <font color="#0000ff">-></font>
  bool <br/>
</code><i> Does not have equality type variables &ndash; comparison allowed on all types
but may raise <code>Invalid_argument</code> exception
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">eqtype</font> t <br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">type</font> t <br/>
</code><i> Does not have equality types &ndash; comparison allowed on all types
but may raise <code>Invalid_argument</code> exception
</i> </td> </tr>

</table>

## Lists

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
[1, 2, 3] <br/>
</code> </td>
<td> <code>
[1; 2; 3] <br/>
</code> </td> </tr>

<tr> <td> <code>
[(1, 2), (3, 4)] <br/>
</code> </td>
<td> <code>
[1, 2; 3, 4] <br/>
</code> </td> </tr>

<tr> <td> <code>
List.length xs <br/>
</code> </td>
<td> <code>
List.length xs <br/>
</code> </td> </tr>

<tr> <td> <code>
List.map f xs <br/>
</code> </td>
<td> <code>
List.map f xs <br/>
</code> </td> </tr>

<tr> <td> <code>
List.app f xs <br/>
</code> </td>
<td> <code>
List.iter f xs <br/>
</code> </td> </tr>

<tr> <td> <code>
List.foldl <font color="#0000ff">op</font>+ 0 xs <br/>
List.foldr <font color="#0000ff">op</font>- 100 xs <br/>
</code> </td>
<td> <code>
List.fold_left (+) 0 xs <br/>
List.fold_right (-) xs 100 <br/>
</code> </td> </tr>

<tr> <td> <code>
List.all (<font color="#0000ff">fn</font> x <font color="#0000ff">=></font>
  x=0) xs <br/>
List.exists (<font color="#0000ff">fn</font> x <font color="#0000ff">=></font>
  x>0) xs <br/>
</code> </td>
<td> <code>
List.for_all (<font color="#0000ff">fun</font> x <font color="#0000ff">-></font>
  x=0) xs <br/>
List.exists (<font color="#0000ff">fun</font> x <font color="#0000ff">-></font>
  x>0) xs <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> xys <font color="#0000ff">=</font> ListPair.zip (xs, ys) <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> xys <font color="#0000ff">=</font> List.combine xs ys <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">val</font> (xs, ys) <font color="#0000ff">=</font> ListPair.unzip xys <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> (xs, ys) <font color="#0000ff">=</font> List.split xys <br/>
</code> </td> </tr>

<tr> <td> <code>
ListPair.app f (xs, ys) <br/>
</code> </td>
<td> <code>
List.iter2 f xs ys <br/>
</code> </td> </tr>

<tr> <td> <code>
[inputLine stdIn, inputLine stdIn] <br/>
<br/>
<br/>
</code> </td>
<td> <i>
Evaluation order is undefined for lists &ndash; use <code><font color="#0000ff">let</font></code>, e.g. <br/>
</i><code>
<font color="#0000ff">let</font> line1 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
<font color="#0000ff">let</font> line2 <font color="#0000ff">=</font> read_line ()
  <font color="#0000ff">in</font> <br/>
[line1; line2]
</code> </td> </tr>

</table>

## Strings

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
"Hello " ^ "world\n" <br/>
</code> </td>
<td> <code>
"Hello " ^ "world\n" <br/>
</code> </td> </tr>

<tr> <td> <code>
Int.toString 13 <br/>
Real.toString 3.141 <br/>
</code> </td>
<td> <code>
string_of_int 13 <br/>
string_of_float 3.141 <br/>
</code> </td> </tr>

<tr> <td> <code>
String.size s <br/>
</code> </td>
<td> <code>
String.length s <br/>
</code> </td> </tr>

<tr> <td> <code>
String.substring(s, 1, 2) <br/>
</code> </td>
<td> <code>
String.sub s 1 2 <br/>
</code> </td> </tr>

<tr> <td> <code>
String.sub(s, 0) <br/>
<br/>
<br/>
</code> </td>
<td> <code>
String.get s 0 <br/>
</code><i>or</i><code> <br/>
s<font color="#0000ff">.</font>[0] <br/>
</code> </td> </tr>

<tr> <td> <i>
Strings are immutable, use <tt>CharArray</tt> for mutability
</i> </td>
<td> <code>
String.set s 0 'F' <br/>
</code><i>or</i><code> <br/>
s<font color="#0000ff">.</font>[0] <font color="#0000ff">&lt;-</font> 'F' <br/>
</code> </td> </tr>

</table>

## Array Functions

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
Array.array(20, 1.0) <br/>
</code> </td>
<td> <code>
Array.make 20 1.0 <br/>
</code> </td> </tr>

<tr> <td> <code>
Array.fromList xs <br/>
</code> </td>
<td> <code>
Array.from_list xs <br/>
</code> </td> </tr>

<tr> <td> <code>
Array.tabulate(30, <font color="#0000ff">fn</font> x
  <font color="#0000ff">=></font> x*x) <br/>
</code> </td>
<td> <code>
Array.init 30 (<font color="#0000ff">fun</font> x
  <font color="#0000ff">-></font> x*x) <br/>
</code> </td> </tr>

<tr> <td> <code>
Array.sub(a, 2) <br/>
<br/>
<br/>
</code> </td>
<td> <code>
Array.get a 2 <br/>
</code><i>or</i><code> <br/>
a.(2) <br/>
</code> </td> </tr>

<tr> <td> <code>
Array.update(a, 2, x) <br/>
<br/>
<br/>
</code> </td>
<td> <code>
Array.set a 2 x <br/>
</code><i>or</i><code> <br/>
a<font color="#0000ff">.</font>(2) <font color="#0000ff">&lt;-</font> x <br/>
</code> </td> </tr>

<tr> <td> <code>
Array.copy{src<font color="#0000ff">=</font>a,
  si<font color="#0000ff">=</font>10, dst<font color="#0000ff">=</font>b,
  di<font color="#0000ff">=</font>0, len<font color="#0000ff">=</font>20} <br/>
</code> </td>
<td> <code>
Array.blit <font color="#0000ff">~</font>src<font color="#0000ff">:</font>a
  <font color="#0000ff">~</font>src_pos<font color="#0000ff">:</font>10
  <font color="#0000ff">~</font>dst<font color="#0000ff">:</font>b
  <font color="#0000ff">~</font>dst_pos<font color="#0000ff">:</font>0
  <font color="#0000ff">~</font>len<font color="#0000ff">:</font>20 <br/>
</code> </td> </tr>

</table>

## Input/Output

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> copyFile(name1, name2)
  <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font> file1
  <font color="#0000ff">=</font> TextIO.openIn name1 <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font>
  s&nbsp;&nbsp;&nbsp;&nbsp;
  <font color="#0000ff">=</font> TextIO.inputAll file1 <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font>
  <font color="#0000ff">_</font>&nbsp;&nbsp;&nbsp;&nbsp;
  <font color="#0000ff">=</font> TextIO.closeIn file1 <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font> file2
  <font color="#0000ff">=</font> TextIO.openOut name2 <br/>
&nbsp;&nbsp; <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; TextIO.output(file2, s); <br/>
&nbsp;&nbsp; &nbsp;&nbsp; TextIO.closeOut file2 <br/>
&nbsp;&nbsp; <font color="#0000ff">end</font> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> copy_file name1 name2
  <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> file1
  <font color="#0000ff">=</font> open_in name1
  <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> size
  <font color="#0000ff">=</font> in_channel_length file1
  <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> buf
  <font color="#0000ff">=</font> String.create size
  <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; really_input file1 buf 0 size; <br/>
&nbsp;&nbsp; close_in file1; <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> file2
  <font color="#0000ff">=</font> open_out name2
  <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; output_string file2 buf; <br/>
&nbsp;&nbsp; close_out file2 <br/>
</code> <i>
Caveat: above code actually contains a race condition.
</i> </td> </tr>

</table>

## Exceptions

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">exception</font> Hell <br/>
</code> </td>
<td> <code>
<font color="#0000ff">exception</font> Hell <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">exception</font> TotalFailure
  <font color="#0000ff">of</font> string <br/>
</code> </td>
<td> <code>
<font color="#0000ff">exception</font> Total_failure
  <font color="#0000ff">of</font> string <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">raise</font> TotalFailure "Unknown code" <br/>
</code> </td>
<td> <code>
raise (Total_failure "Unknown code") <br/>
</code> </td> </tr>

<tr> <td> <code>
expr <font color="#0000ff">handle</font> TotalFailure s
  <font color="#0000ff">=></font> <br/>
&nbsp;&nbsp; ouch() <br/>
</code> </td>
<td> <code>
<font color="#0000ff">try</font> expr <font color="#0000ff">with</font> <br/>
&nbsp;&nbsp; Total_failure s
  <font color="#0000ff">-></font> ouch () <br/>
</code> </td> </tr>

</table>

## Local Declarations

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">fun</font> pyt(x,y) <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font> xx
  <font color="#0000ff">=</font> x * x <br/>
&nbsp;&nbsp; &nbsp;&nbsp; <font color="#0000ff">val</font> yy
  <font color="#0000ff">=</font> y * y <br/>
&nbsp;&nbsp; <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; &nbsp;&nbsp; Math.sqrt(xx + yy) <br/>
&nbsp;&nbsp; <font color="#0000ff">end</font> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> pyt x y <font color="#0000ff">=</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> xx
  <font color="#0000ff">=</font> x *. x <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> yy
  <font color="#0000ff">=</font> y *. y <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; sqrt (xx +. yy) <br/>
<br/>
<br/>
<br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">local</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">fun</font> sqr x
  <font color="#0000ff">=</font> x * x <br/>
<font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">fun</font> pyt(x,y)
  <font color="#0000ff">=</font> Math.sqrt(sqr x + sqr y) <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <i>
Does not have <code><font color="#0000ff">local</font></code> &ndash;
use global declarations, an auxiliary module, or
<code><font color="#0000ff">let</font></code>
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">let</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">structure</font> X
  <font color="#0000ff">=</font> F(A) <br/>
<font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; X.value + 10<br/>
<font color="#0000ff">end</font> <br/>
</code> <i>
Standard does not have structure declarations in
<code><font color="#0000ff">let</font></code> but some implementations
support them
</i> </td>
<td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">module</font> X
  <font color="#0000ff">=</font> F (A) <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; X.value + 10<br/>
<br/>
<br/>
<br/>
</code> <i>
Experimental language extension <br/>
<br/>
</i></td> </tr>

<tr> <td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">open</font> M <font color="#0000ff">in</font> expr <font color="#0000ff">end</font> <br/> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">let</font> <font color="#0000ff">open</font> M <font color="#0000ff">in</font> expr <br/>
</code> <i>
Note: since Ocaml 3.12
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">let</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">datatype</font> t
  <font color="#0000ff">=</font> A <font color="#0000ff">|</font> B <br/>
&nbsp;&nbsp; <font color="#0000ff">exception</font> E <br/>
<font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; expr <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <i>
Does not have local type or exception declarations &ndash;
use global declarations or <code><font color="#0000ff">let</font></code>
<code><font color="#0000ff">module</font></code>
</i> </td> </tr>

</table>

## Structures

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">structure</font> X <font color="#0000ff">:></font> S
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">struct</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">type</font> t
  <font color="#0000ff">=</font> int <br/>
&nbsp;&nbsp; <font color="#0000ff">val</font> x
  <font color="#0000ff">=</font> 0 <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">module</font> X <font color="#0000ff">:</font> S
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">struct</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">type</font> t
  <font color="#0000ff">=</font> int <br/>
&nbsp;&nbsp; <font color="#0000ff">let</font> x
  <font color="#0000ff">=</font> 0 <br/>
<font color="#0000ff">end</font> <br/>
</code> </td> </tr>

<tr> <td> <code>
X <font color="#0000ff">:></font> S <br/>
</code> </td>
<td> <code>
(X <font color="#0000ff">:</font> S) <br/>
</code> </td> </tr>

<tr> <td> <code>
X <font color="#0000ff">:</font> S <br/>
</code> </td>
<td> <i>
Does not have transparent signature ascription &ndash; use opaque ascription
and <code><font color="#0000ff">with</font></code> constraints
</i> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">open</font> X <br/>
</code> </td>
<td> <code>
<font color="#0000ff">include</font> X <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">local</font> <font color="#0000ff">open</font> X
  <font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; (* ... *) <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">open</font> X <br/>
(* ... *)<br/>
<br/>
</code> </td> </tr>

</table>

## Functors

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">functor</font> F(X <font color="#0000ff">:</font> S)
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">struct</font> <br/>
&nbsp;&nbsp; (* ... *) <br/>
<font color="#0000ff">end</font> <br/>
<br/>
<br/>
<br/>
<br/>
<br/>
</code> </td>
<td> <code>
<font color="#0000ff">module</font> F (X <font color="#0000ff">:</font> S)
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">struct</font> <br/>
&nbsp;&nbsp; (* ... *) <br/>
<font color="#0000ff">end</font> <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">module</font> F <font color="#0000ff">=</font>
  <font color="#0000ff">functor</font> (X <font color="#0000ff">:</font> S)
  <font color="#0000ff">-></font> <br/>
<font color="#0000ff">struct</font> <br/>
&nbsp;&nbsp; (* ... *) <br/>
<font color="#0000ff">end</font> <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">functor</font> F(X <font color="#0000ff">:</font>
  <font color="#0000ff">sig</font>
  <font color="#0000ff">type</font> t
  <font color="#0000ff">end</font>)
  <font color="#0000ff">=</font> body <br/>
<!--
  <font color="#0000ff">struct</font>
  <font color="#0000ff">type</font> u <font color="#0000ff">=</font> X.t
  <font color="#0000ff">end</font> <br/>
-->
<font color="#0000ff">structure</font> X <font color="#0000ff">=</font>
  F (<font color="#0000ff">struct</font>
  <font color="#0000ff">type</font> t <font color="#0000ff">=</font> int
  <font color="#0000ff">end</font>) <br/> </code> <i>
or </i> <br/> <code>
<font color="#0000ff">functor</font> F(<font color="#0000ff">type</font> t)
  <font color="#0000ff">=</font> body <br/>
<!--
  <font color="#0000ff">struct</font>
  <font color="#0000ff">type</font> u <font color="#0000ff">=</font> t
  <font color="#0000ff">end</font>
-->
<font color="#0000ff">structure</font> X <font color="#0000ff">=</font>
  F(<font color="#0000ff">type</font> t <font color="#0000ff">=</font> int) <br/>
</code> </td>
<td> <code>
<font color="#0000ff">module</font> F (X <font color="#0000ff">:</font>
  <font color="#0000ff">sig</font>
  <font color="#0000ff">type</font> t
  <font color="#0000ff">end</font>)
  <font color="#0000ff">=</font> body <br/>
<!--
  <font color="#0000ff">struct</font>
  <font color="#0000ff">type</font> u <font color="#0000ff">=</font> X.t
  <font color="#0000ff">end</font> <br/>
-->
<font color="#0000ff">module</font> X <font color="#0000ff">=</font>
  F(<font color="#0000ff">struct</font>
  <font color="#0000ff">type</font> t <font color="#0000ff">=</font> int
  <font color="#0000ff">end</font>) <br/>
  <br/>
  <br/>
  <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">functor</font> F (X <font color="#0000ff">:</font> S)
  (Y <font color="#0000ff">:</font> T) <font color="#0000ff">=</font> body <br/>
</code> <i>
Standard does not have higher-order functors but several implementations
support them
</i> </td>
<td> <code>
<font color="#0000ff">module</font> F (X <font color="#0000ff">:</font> S)
  (Y <font color="#0000ff">:</font> T) <font color="#0000ff">=</font> body <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">module</font> F <font color="#0000ff">=</font>
  <font color="#0000ff">functor</font> (X <font color="#0000ff">:</font> S)
  <font color="#0000ff">-></font>
  <font color="#0000ff">functor</font> (Y <font color="#0000ff">:</font> T)
  <font color="#0000ff">-></font> body <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">functor</font> F(X <font color="#0000ff">:</font> S)
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">let</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">structure</font> Y
  <font color="#0000ff">=</font> G(X) <br/>
<font color="#0000ff">in</font> <br/>
&nbsp;&nbsp; Y.A <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <i>
Does not have <code><font color="#0000ff">let</font></code> for modules
</i> </td> </tr>

</table>

## Signatures

<table width="100%" border="border" cellpadding="2">
<tr> <th width="50%" align="left">SML</th>
     <th width="50%" align="left">Ocaml</th> </tr>

<tr> <td> <code>
<font color="#0000ff">signature</font> S <font color="#0000ff">=</font> <br/>
<font color="#0000ff">sig</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">type</font> t <br/>
&nbsp;&nbsp; <font color="#0000ff">eqtype</font> u <br/>
&nbsp;&nbsp; <font color="#0000ff">val</font> x
  <font color="#0000ff">:</font> t <br/>
&nbsp;&nbsp; <font color="#0000ff">structure</font> M
  <font color="#0000ff">:</font> T <br/>
<font color="#0000ff">end</font> <br/>
</code> </td>
<td> <code>
<font color="#0000ff">module</font> <font color="#0000ff">type</font> S
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">sig</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">type</font> t <br/>
&nbsp;&nbsp; <font color="#0000ff">type</font> u <br/>
&nbsp;&nbsp; <font color="#0000ff">val</font> x
  <font color="#0000ff">:</font> t <br/>
&nbsp;&nbsp; <font color="#0000ff">module</font> M
  <font color="#0000ff">:</font> T <br/>
<font color="#0000ff">end</font> <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">functor</font> F(X <font color="#0000ff">:</font> S)
  <font color="#0000ff">:</font> S <br/>
</code> <i>
Standard does not have higher-order functors but several implementations
support them
</i> </td>
<td> <code>
<font color="#0000ff">module</font> F (X <font color="#0000ff">:</font> S)
  <font color="#0000ff">:</font> S <br/>
</code><i>or</i><code> <br/>
<font color="#0000ff">module</font> F <font color="#0000ff">:</font>
  <font color="#0000ff">functor</font> (X <font color="#0000ff">:</font> S)
  <font color="#0000ff">-></font> S <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">include</font> S <br/>
</code> </td>
<td> <code>
<font color="#0000ff">include</font> S <br/>
</code> </td> </tr>

<tr> <td> <i>
Does not have <code><font color="#0000ff">open</font></code> in signatures
</i> </td>
<td> <code>
<font color="#0000ff">open</font> X <br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">structure</font> X <font color="#0000ff">:</font> A <br/>
<font color="#0000ff">structure</font> Y <font color="#0000ff">:</font> B <br/>
<font color="#0000ff">sharing</font> <font color="#0000ff">type</font> X.t
  <font color="#0000ff">=</font> Y.u <br/>
</code> </td>
<td> <i>
Does not have <code><font color="#0000ff">sharing</font></code> constraints &ndash;
use <code><font color="#0000ff">with</font></code>
</i> </td> </tr>

<tr> <td> <code>
S <font color="#0000ff">where</font> <font color="#0000ff">type</font> t
  <font color="#0000ff">=</font> int <br/>
</code> </td>
<td> <code>
S <font color="#0000ff">with</font> <font color="#0000ff">type</font> t
  <font color="#0000ff">=</font> int <br/>
</code> </td> </tr>

<tr> <td> <code>
S <font color="#0000ff">where</font> X <font color="#0000ff">=</font> A.B <br/>
</code> <i>
Standard does not have <code><font color="#0000ff">where</font></code>
for structures but several implementations support it &ndash;
use <code><font color="#0000ff">where</font></code>
<code><font color="#0000ff">type</font></code> otherwise
</i> </td>
<td> <code>
S <font color="#0000ff">with</font> X <font color="#0000ff">=</font> A.B <br/>
<br/>
<br/>
</code> </td> </tr>

<tr> <td> <code>
<font color="#0000ff">signature</font> S
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">sig</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">signature</font> A <br/>
&nbsp;&nbsp; <font color="#0000ff">signature</font> B <font color="#0000ff">=</font> A <br/>
<font color="#0000ff">end</font> <br/>
</code> <i>
Standard does not have nested signatures but some implementations support them
</i> </td>
<td> <code>
<font color="#0000ff">module</font> <font color="#0000ff">type</font> S
  <font color="#0000ff">=</font> <br/>
<font color="#0000ff">sig</font> <br/>
&nbsp;&nbsp; <font color="#0000ff">module</font>
  <font color="#0000ff">type</font> A <br/>
&nbsp;&nbsp; <font color="#0000ff">module</font>
  <font color="#0000ff">type</font> B <font color="#0000ff">=</font> A <br/>
<font color="#0000ff">end</font> <br/>
<br/>
<br/>
</code> </td> </tr>

</table>
