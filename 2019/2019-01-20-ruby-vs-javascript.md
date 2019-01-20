# Ruby vs Javascript comparison
> **tags**: | Ruby | javascript | vs | comparison |

First of all it's not my writings and it's just a copy of *Artem's Tyurin* [agentcooper/js-ruby-comparison](https://github.com/agentcooper/js-ruby-comparison) repo 

- [Arrays](#arrays)
  - [Manipulation](#manipulation)
  - [Predicates](#predicates)
  - [Array map methong](#array-map-methong)
  - [Slices](#slices)
  - [Iterating elements](#iterating-elements)
- [Strings](#strings)
- [TT](#tt)

---

## Arrays 

### Manipulation

**Ruby**

```ruby
a = ["1", "2"]
a.push("3")

a.map!(&:to_i) # [1, 2, 3]

a.delete_at(1)
a # [1, 3]

a.reverse! # [3, 1]

a.unshift(777) # [777, 3, 1]

a.last # [1]
```

**JavaScript**

```javascript
var a = ["1", "2"];
a.push("3");

a = a.map(function(n) { return parseInt(n, 10); });

a.splice(1, 1 /* how much */);
a; // [1, 3]

a.reverse() // [3, 1]

a.unshift(777); // 3
a; // [777, 3, 1]

/* or in place: */ var b = [3, 1];
                   [777].concat(b); // [777, 3, 1]
a.slice(-1)[0]; // 1
/* or */ a[a.length - 1]; // 1
```

### Predicates

**Ruby**

```ruby
a = [1, 2, 3]

a.index(2) # 1

a.all?{|n| n > 4} # false
a.any?{|n| n > 2} # true

a.keep_if{|n| n > 1} # [2, 3]
```

**JavaScript**

```javascript
var a = [1, 2, 3];

a.indexOf(2); // 1

a.every(function(n) { return n > 4; }); // false
a.some(function(n) { return n > 2; });  // true

a.filter(function(n) { return n > 1;}); // [2, 3]
```

### Array map methong

**Ruby**

```ruby
a = ["aaa  ", "  bbb", "  ccc  "]

a.map(&:strip) # ["aaa", "bbb", "ccc"]
```

**JavaScript**

```javascript
var a = ["aaa  ", "  bbb", "  ccc  "]

a.map(function(x) { return x.trim(); });               // ['aaa', 'bbb', 'ccc']
a.map(Function.prototype.call, String.prototype.trim); // ['aaa', 'bbb', 'ccc']
a.map(x => x.trim());                                  // ['aaa', 'bbb', 'ccc']
```

### Slices

**Ruby**

```ruby
a = [1, 2, 3, 4, 5]

a.slice(1..-2)  # [2, 3, 4]
a[1..-2]        # [2, 3, 4]
```

**JavaScript**

```javascript
var a = [1, 2, 3, 4, 5];

a.slice(1, -1); // [2, 3, 4]
```

### Iterating elements

```ruby
a = [1, 2, 3]

a.each {|n| puts n}

a.each do |n|
    puts n
end


for i in 0..(a.length - 1) do
  puts a[i]
end
```

**JavaScript**

```javascript
var a = [1, 2, 3];

a.forEach(function(n) { console.log(n); })

for (var i = 0; i < a.length; i++) {
  console.log(a[i]);
}

for (elem of a) {
  console.log(elem);
}
```

## Strings

## TT 

**Ruby**

```ruby

```

**JavaScript**

```javascript

```
