# Git Rename Detection - Quick Reference

## How It Works

Git doesn't track renames directly. Instead, it uses **content similarity detection**:

- **≥50% similar** (default): Git shows as renamed
- **<50% similar**: Git shows as deleted + created

## Essential Commands

### View rename detection in logs

```bash
# Show renames with default 50% threshold
git log --stat -M

# Show renames with custom threshold
git log --stat -M30%     # 30% similarity
git log --stat -M90%     # 90% similarity

# Show full diff with renames
git log -p -M

# Show just file status (R = renamed, A = added, D = deleted)
git log --name-status -M
```

### View rename detection in diffs

```bash
# Check current changes
git diff --stat -M
git diff --name-status -M

# Check specific commit
git show --stat -M HEAD
git show --stat -M abc123
```

### View rename detection in specific commit

```bash
# Last commit
git show --stat -M

# Specific commit
git show --stat -M <commit-hash>
```

## Configuration

```bash
# Enable rename detection by default
git config diff.renames true

# Set the search limit for renames
git config diff.renameLimit 999
git config merge.renameLimit 999
```

## Common Patterns

### Pattern 1: Pure rename (✓ Detected)

```bash
git mv oldname.txt newname.txt
git commit -m "Rename file"
# Result: oldname.txt => newname.txt (100%)
```

### Pattern 2: Rename + minor edits (✓ Detected)

```bash
git mv oldname.txt newname.txt
# Edit newname.txt slightly (add a few lines)
git add newname.txt
git commit -m "Rename and update file"
# Result: oldname.txt => newname.txt (85%)
```

### Pattern 3: Rename + major rewrite (✗ Not detected)

```bash
git mv oldname.txt newname.txt
# Completely rewrite newname.txt
git add newname.txt
git commit -m "Rewrite file"
# Result: oldname.txt deleted, newname.txt created
```

## Similarity Threshold Examples

```bash
# Default (50%)
git log --stat -M

# Strict (90% - only detect obvious renames)
git log --stat -M90%

# Lenient (30% - detect more aggressive renames)
git log --stat -M30%

# Very lenient (10% - detect even major rewrites)
git log --stat -M10%
```

## Best Practices

### ✓ DO

- Commit renames separately from content changes
- Use `-M` flag when reviewing history
- Use `git mv` for clarity (though `mv` + `git add` works too)
- Configure `diff.renames = true` globally

### ✗ DON'T

- Mix major refactoring with renames in one commit
- Forget `-M` when reviewing refactoring PRs
- Assume Git will always detect your renames

## Real-World Examples

### Good: Separate commits

```bash
# Commit 1: Rename only
git mv src/utils.js src/helpers.js
git commit -m "Rename utils to helpers"

# Commit 2: Modify content
# Edit src/helpers.js
git commit -am "Refactor helper functions"
```

### Bad: Mixed commit

```bash
# One commit: Rename + major changes
git mv src/utils.js src/helpers.js
# Completely rewrite src/helpers.js
git add src/helpers.js
git commit -m "Rename and refactor"
# Result: Git may not detect the rename!
```

## Troubleshooting

### Why isn't Git detecting my rename?

1. **Too many changes**: Content similarity < 50%
   - Solution: Use lower threshold `-M30%` to view
   - Better: Commit rename separately

2. **Not using -M flag**: Rename detection not enabled
   - Solution: Add `-M` to your commands
   - Better: Configure globally with `git config diff.renames true`

3. **Multiple renames**: Hit the rename limit
   - Solution: Increase with `git config diff.renameLimit 999`

### Check what Git sees

```bash
# See raw diff without rename detection
git log --stat --no-renames

# See with rename detection
git log --stat -M

# Compare the output
```

## Advanced: Copy Detection

Git can also detect copies (not just moves):

```bash
# Detect copies (more expensive)
git log --stat -C

# Detect copies even from unmodified files
git log --stat -C -C

# Detect copies with custom threshold
git log --stat -C50%
```

## Summary Table

| Threshold | When to Use |
|-----------|-------------|
| `-M` or `-M50%` | Default, balanced |
| `-M90%` | Strict, only obvious renames |
| `-M30%` | Lenient, refactoring work |
| `-M10%` | Very lenient, major rewrites |
| `--no-renames` | Disable detection, see raw changes |
