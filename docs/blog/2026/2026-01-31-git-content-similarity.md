# Git Doesn't Track File Renames (And How It Fakes It)
<!-- tags: git -->

![pic0](2026-01-31-git-content-similarity/pic0.jpeg)

Ever used `git mv` to rename a file? Many people assume it creates special rename metadata in Git's object database.
Here's the surprise: **it doesn't**. Git has no concept of a "rename" operation at all.

Instead, Git uses *content similarity detection* algorithm. When you run `git log` or `git diff`, Git analyzes the content of deleted and added files on-the-fly. If two files are similar enough (≥50% by default), Git displays them as a *rename*. If not, you see them as separate *delete* and *create* operations.

In this post, we'll see three scenarios with different similarity percentages, learn how to adjust Git's detection threshold using the `-M` flag, and understand why `git mv` is just a convenience wrapper with no special powers.

## 1. How Git Stores Renames

**Git doesn't track renames explicitly.** According to [official documentation](https://git-scm.com/docs/gitdiffcore), Git detects renames post-hoc by analyzing content similarity:

- **≥50% similar** (default): Git shows as renamed
- **<50% similar**: Git shows as deleted + created

### 1.1. What about `git mv`?

`git mv` is just a **convenience command** that does this:

```sh
# These are equivalent:
git mv old.txt new.txt

# Same as:
mv old.txt new.txt
git rm old.txt
git add new.txt
```

Both produce **identical Git objects** - no rename metadata is stored.

---

Let's demonstrate this with a practical example. We'll create an empty test repository:

```sh
DEMO_REPO="git-rename-test-repo"

mkdir "$DEMO_REPO"
cd "$DEMO_REPO"
git init
git config user.name "Demo User"
git config user.email "demo@example.com"
```

## 2. SCENARIO 1: Move file without changes

```sh
# Creating file1.txt with 10 lines...

cat > file1.txt << 'EOF'
Line 01: This is the first line of the file
Line 02: This is the second line of the file
Line 03: This is the third line of the file
Line 04: This is the fourth line of the file
Line 05: This is the fifth line of the file
Line 06: This is the sixth line of the file
Line 07: This is the seventh line of the file
Line 08: This is the eighth line of the file
Line 09: This is the ninth line of the file
Line 10: This is the tenth line of the file
EOF

git add file1.txt
git commit -m "Add file1.txt"
[main (root-commit) 776edcb] Add file1.txt
 1 file changed, 10 insertions(+)
 create mode 100644 file1.txt

# Moving file1.txt to docs/file1.txt (no content change)...

mkdir docs
git mv file1.txt docs/file1.txt
git commit -m "Move file to docs folder"
[main d37b953] Move file to docs folder
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename file1.txt => docs/file1.txt (100%)
```

### 2.1. Git detection result

```sh
git show --stat -M HEAD

commit d37b9531cbf0e5bbe499fd2cbd49e365685d053e (HEAD -> main)
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:49:56 2026 +0100

    Move file to docs folder

 file1.txt => docs/file1.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
```

**Result:** Git detects this as a rename (R100 = 100% similarity). All 10/10 lines unchanged = 100% > 50% threshold.

## 3. SCENARIO 2: Move with minor changes

```sh
# Creating file2.txt with 10 lines...

cat > file2.txt << 'EOF'
Line 01: This is the first line of the file
Line 02: This is the second line of the file
Line 03: This is the third line of the file
Line 04: This is the fourth line of the file
Line 05: This is the fifth line of the file
Line 06: This is the sixth line of the file
Line 07: This is the seventh line of the file
Line 08: This is the eighth line of the file
Line 09: This is the ninth line of the file
Line 10: This is the tenth line of the file
EOF

git add file2.txt
git commit -m "Add file2.txt"
[main cb90460] Add file2.txt
 1 file changed, 10 insertions(+)
 create mode 100644 file2.txt

# Moving to subdir/file2.txt and changing 2 lines (80% similarity)...

mkdir -p subdir
cat > subdir/file2.txt << 'EOF'
Line 01: This is the first line of the file
Line 02: This line has been MODIFIED
Line 03: This is the third line of the file
Line 04: This is the fourth line of the file
Line 05: This is the fifth line of the file
Line 06: This is the sixth line of the file
Line 07: This is the seventh line of the file
Line 08: This is the eighth line of the file
Line 09: This is the ninth line of the file
Line 10: This line has also been MODIFIED
EOF

git rm file2.txt
rm 'file2.txt'

git add subdir/file2.txt

git commit -m "Move and modify 2 lines"
[main 7f9839c] Move and modify 2 lines
 1 file changed, 2 insertions(+), 2 deletions(-)
 rename file2.txt => subdir/file2.txt (80%)
```

### 3.1. Git detection result

```sh
git show --stat -M HEAD

commit 7f9839c33fb19397f9354ea4f8c17ba4e48141ee (HEAD -> main)
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:57:53 2026 +0100

    Move and modify 2 lines

 file2.txt => subdir/file2.txt | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

**Result:** Git detects this as a rename (R80 = 80% similarity). Changed 2/10 lines, so 8/10 lines unchanged = 80% > 50% threshold.

## 4. SCENARIO 3: Move with major changes

```sh
# Creating file3.txt with 10 lines...

cat > file3.txt << 'EOF'
Line 01: This is the first line of the file
Line 02: This is the second line of the file
Line 03: This is the third line of the file
Line 04: This is the fourth line of the file
Line 05: This is the fifth line of the file
Line 06: This is the sixth line of the file
Line 07: This is the seventh line of the file
Line 08: This is the eighth line of the file
Line 09: This is the ninth line of the file
Line 10: This is the tenth line of the file
EOF

git add file3.txt

git commit -m "Add file3.txt"
[main f43b480] Add file3.txt
 1 file changed, 10 insertions(+)
 create mode 100644 file3.txt

# Moving to newdir/file3.txt and changing 8 lines (20% similarity)...

mkdir -p newdir
cat > newdir/file3.txt << 'EOF'
Line 01: COMPLETELY DIFFERENT CONTENT HERE
Line 02: COMPLETELY DIFFERENT CONTENT HERE
Line 03: This is the third line of the file
Line 04: COMPLETELY DIFFERENT CONTENT HERE
Line 05: COMPLETELY DIFFERENT CONTENT HERE
Line 06: COMPLETELY DIFFERENT CONTENT HERE
Line 07: COMPLETELY DIFFERENT CONTENT HERE
Line 08: COMPLETELY DIFFERENT CONTENT HERE
Line 09: COMPLETELY DIFFERENT CONTENT HERE
Line 10: This is the tenth line of the file
EOF

git rm file3.txt -q
git add newdir/file3.txt

git commit -m "Move and rewrite most content" 
[main 963ddde] Move and rewrite most content
 2 files changed, 10 insertions(+), 10 deletions(-)
 delete mode 100644 file3.txt
 create mode 100644 newdir/file3.txt
```

### 4.1. Git detection result

```sh
git show --stat -M HEAD

commit 963dddea7bfe74d02b9873c59faae60a9c7132fe (HEAD -> main)
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 08:40:39 2026 +0100

    Move and rewrite most content

 file3.txt        | 10 ----------
 newdir/file3.txt | 10 ++++++++++
 2 files changed, 10 insertions(+), 10 deletions(-)
```

**Result:** Git does NOT detect this as a rename. Changed 8/10 lines, so only 2/10 lines unchanged = 20% < 50% threshold. Git shows 'file3.txt' deleted and 'newdir/file3.txt' created.

## 5. Key Takeaways

Git's rename detection is a powerful feature that works entirely through content similarity analysis:

- **No metadata stored**: Git treats `git mv` and `mv + git rm + git add` identically
- **Default 50% threshold**: Works well for most use cases
- **Adjustable sensitivity**: Use `-M<percentage>` to tune detection (e.g., `-M30%` for aggressive, `-M90%` for strict)
- **Post-hoc analysis**: Rename detection happens when you run `git log`, `git show`, or `git diff`, not during commit

---

## Appendix: Full commit history

### A.1. With rename detection (default 50% threshold)

<details>
<summary>View full commit history</summary>

```sh
git log --oneline --stat -M --reverse

776edcb Add file1.txt
 file1.txt | 10 ++++++++++
 1 file changed, 10 insertions(+)
d37b953 Move file to docs folder
 file1.txt => docs/file1.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
cb90460 Add file2.txt
 file2.txt | 10 ++++++++++
 1 file changed, 10 insertions(+)
7f9839c Move and modify 2 lines
 file2.txt => subdir/file2.txt | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
f43b480 Add file3.txt
 file3.txt | 10 ++++++++++
 1 file changed, 10 insertions(+)
963ddde (HEAD -> main) Move and rewrite most content
 file3.txt        | 10 ----------
 newdir/file3.txt | 10 ++++++++++
 2 files changed, 10 insertions(+), 10 deletions(-)
```

</details>

### A.2. Experiment with different thresholds

You can adjust Git's rename detection sensitivity using the `-M` flag. Let's see how different thresholds affect the detection of our three scenarios:

#### A.2.1. With 30% threshold (-M30%)

Lower threshold = more aggressive rename detection, but File3 (20% similarity) is still below the 30% threshold:

<details>
<summary>View output with -M30%</summary>

```sh
git log --oneline --name-status -M30% --reverse

776edcb Add file1.txt
A       file1.txt
d37b953 Move file to docs folder
R100    file1.txt       docs/file1.txt
cb90460 Add file2.txt
A       file2.txt
7f9839c Move and modify 2 lines
R080    file2.txt       subdir/file2.txt
f43b480 Add file3.txt
A       file3.txt
963ddde (HEAD -> main) Move and rewrite most content
D       file3.txt
A       newdir/file3.txt
```

Note: File3 is still shown as delete + add because 20% < 30% threshold.

</details>

#### A.2.2. With 90% threshold (-M90%)

Higher threshold = stricter rename detection. File2 (80% similarity) no longer detected as a **rename**:

<details>
<summary>View output with -M90%</summary>

```sh
git log --oneline --name-status -M90% --reverse

776edcb Add file1.txt
A       file1.txt
d37b953 Move file to docs folder
R100    file1.txt       docs/file1.txt
cb90460 Add file2.txt
A       file2.txt
7f9839c Move and modify 2 lines
D       file2.txt
A       subdir/file2.txt
f43b480 Add file3.txt
A       file3.txt
963ddde (HEAD -> main) Move and rewrite most content
D       file3.txt
A       newdir/file3.txt
```

Note: File2 is now shown as delete + add because 80% < 90% threshold. Only file1 with 100% similarity is still detected as a **rename**.

</details>

### A.3. Show detailed diff with rename detection

<details>
<summary>View detailed diff output</summary>

```sh
git log -p -M --reverse

commit 776edcb0641eb4fdde03c54c051695b79dfdf4a8
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:49:43 2026 +0100

    Add file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..941da65
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1,10 @@
+Line 01: This is the first line of the file
+Line 02: This is the second line of the file
+Line 03: This is the third line of the file
+Line 04: This is the fourth line of the file
+Line 05: This is the fifth line of the file
+Line 06: This is the sixth line of the file
+Line 07: This is the seventh line of the file
+Line 08: This is the eighth line of the file
+Line 09: This is the ninth line of the file
+Line 10: This is the tenth line of the file

commit d37b9531cbf0e5bbe499fd2cbd49e365685d053e
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:49:56 2026 +0100

    Move file to docs folder

diff --git a/file1.txt b/docs/file1.txt
similarity index 100%
rename from file1.txt
rename to docs/file1.txt

commit cb904608397555d6dd1810e6d1985c86d8d7092c
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:54:10 2026 +0100

    Add file2.txt

diff --git a/file2.txt b/file2.txt
new file mode 100644
index 0000000..941da65
--- /dev/null
+++ b/file2.txt
@@ -0,0 +1,10 @@
+Line 01: This is the first line of the file
+Line 02: This is the second line of the file
+Line 03: This is the third line of the file
+Line 04: This is the fourth line of the file
+Line 05: This is the fifth line of the file
+Line 06: This is the sixth line of the file
+Line 07: This is the seventh line of the file
+Line 08: This is the eighth line of the file
+Line 09: This is the ninth line of the file
+Line 10: This is the tenth line of the file

commit 7f9839c33fb19397f9354ea4f8c17ba4e48141ee
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 07:57:53 2026 +0100

    Move and modify 2 lines

diff --git a/file2.txt b/subdir/file2.txt
similarity index 80%
rename from file2.txt
rename to subdir/file2.txt
index 941da65..a651b2e 100644
--- a/file2.txt
+++ b/subdir/file2.txt
@@ -1,5 +1,5 @@
 Line 01: This is the first line of the file
-Line 02: This is the second line of the file
+Line 02: This line has been MODIFIED
 Line 03: This is the third line of the file
 Line 04: This is the fourth line of the file
 Line 05: This is the fifth line of the file
@@ -7,4 +7,4 @@ Line 06: This is the sixth line of the file
 Line 07: This is the seventh line of the file
 Line 08: This is the eighth line of the file
 Line 09: This is the ninth line of the file
-Line 10: This is the tenth line of the file
+Line 10: This line has also been MODIFIED

commit f43b4801b0a1073245cf18b6461d10fc82024f99
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 08:39:44 2026 +0100

    Add file3.txt

diff --git a/file3.txt b/file3.txt
new file mode 100644
index 0000000..941da65
--- /dev/null
+++ b/file3.txt
@@ -0,0 +1,10 @@
+Line 01: This is the first line of the file
+Line 02: This is the second line of the file
+Line 03: This is the third line of the file
+Line 04: This is the fourth line of the file
+Line 05: This is the fifth line of the file
+Line 06: This is the sixth line of the file
+Line 07: This is the seventh line of the file
+Line 08: This is the eighth line of the file
+Line 09: This is the ninth line of the file
+Line 10: This is the tenth line of the file

commit 963dddea7bfe74d02b9873c59faae60a9c7132fe
Author: Demo User <demo@example.com>
Date:   Sat Jan 31 08:40:39 2026 +0100

    Move and rewrite most content

diff --git a/file3.txt b/file3.txt
deleted file mode 100644
index 941da65..0000000
--- a/file3.txt
+++ /dev/null
@@ -1,10 +0,0 @@
-Line 01: This is the first line of the file
-Line 02: This is the second line of the file
-Line 03: This is the third line of the file
-Line 04: This is the fourth line of the file
-Line 05: This is the fifth line of the file
-Line 06: This is the sixth line of the file
-Line 07: This is the seventh line of the file
-Line 08: This is the eighth line of the file
-Line 09: This is the ninth line of the file
-Line 10: This is the tenth line of the file
diff --git a/newdir/file3.txt b/newdir/file3.txt
new file mode 100644
index 0000000..bd0c679
--- /dev/null
+++ b/newdir/file3.txt
@@ -0,0 +1,10 @@
+Line 01: COMPLETELY DIFFERENT CONTENT HERE
+Line 02: COMPLETELY DIFFERENT CONTENT HERE
+Line 03: This is the third line of the file
+Line 04: COMPLETELY DIFFERENT CONTENT HERE
+Line 05: COMPLETELY DIFFERENT CONTENT HERE
+Line 06: COMPLETELY DIFFERENT CONTENT HERE
+Line 07: COMPLETELY DIFFERENT CONTENT HERE
+Line 08: COMPLETELY DIFFERENT CONTENT HERE
+Line 09: COMPLETELY DIFFERENT CONTENT HERE
+Line 10: This is the tenth line of the file
```

</details>
