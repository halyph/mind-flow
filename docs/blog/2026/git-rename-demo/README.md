# Git Rename Detection Demo

This demo shows how Git detects file renames based on content similarity.

## Setup

```bash
# Navigate to demo folder
cd git-rename-demo

# Run the demo script
bash demo.sh
```

## What the demo shows:

### Scenario 1: Move without changes
- Git detects as **renamed** (100% similarity)

### Scenario 2: Move with minor changes
- Git detects as **renamed** (~90% similarity)

### Scenario 3: Move with major changes
- Git treats as **deleted + created** (low similarity)

## Manual Demo Commands

You can also run these commands manually to see the behavior:

### Scenario 1: Pure rename (no content change)

```bash
# Create a file
cat > article.txt << 'EOF'
# Introduction to Programming

Programming is the art of telling computers what to do.
It involves writing instructions in a language that computers can understand.

## Why Learn Programming?

1. Problem-solving skills
2. Career opportunities
3. Creative expression
4. Automation of tasks

## Getting Started

The best way to learn programming is by doing.
Start with simple projects and gradually increase complexity.
EOF

git add article.txt
git commit -m "Add article.txt"

# Move the file (no changes)
mkdir docs
git mv article.txt docs/article.txt
git commit -m "Move article to docs folder"

# Check how Git detected it
git show --stat -M
git log --oneline --stat -M -2
```

### Scenario 2: Move with minor changes (still detected)

```bash
# Create another file
cat > tutorial.txt << 'EOF'
# Python Basics

Python is a high-level programming language.
It is known for its simplicity and readability.

## Variables
Variables store data values.
x = 5
name = "Alice"

## Functions
Functions are reusable blocks of code.
def greet(name):
    print(f"Hello, {name}")

## Loops
Loops repeat code multiple times.
for i in range(5):
    print(i)
EOF

git add tutorial.txt
git commit -m "Add tutorial.txt"

# Move and make small changes
mkdir guides
cat > guides/python-tutorial.txt << 'EOF'
# Python Basics - Beginner's Guide

Python is a high-level programming language.
It is known for its simplicity, readability, and ease of learning.

## Variables
Variables store data values.
x = 5
name = "Alice"
age = 25

## Functions
Functions are reusable blocks of code.
def greet(name):
    print(f"Hello, {name}!")

## Loops
Loops repeat code multiple times.
for i in range(5):
    print(i)

Happy coding!
EOF

git rm tutorial.txt
git add guides/python-tutorial.txt
git commit -m "Move tutorial and add minor improvements"

# Check detection (should still show as renamed with ~85% similarity)
git show --stat -M
git show --stat -M50%  # Require 50% similarity
```

### Scenario 3: Move with major changes (not detected)

```bash
# Create a file with substantial content
cat > draft.txt << 'EOF'
# Machine Learning Introduction

Machine learning is a subset of artificial intelligence.
It focuses on building systems that learn from data.

## Types of Machine Learning

1. Supervised Learning
   - Classification
   - Regression

2. Unsupervised Learning
   - Clustering
   - Dimensionality Reduction

3. Reinforcement Learning
   - Agent-based learning
   - Reward optimization

## Applications

- Image recognition
- Natural language processing
- Recommendation systems
- Autonomous vehicles
EOF

git add draft.txt
git commit -m "Add ML draft"

# Move and completely rewrite
mkdir articles
cat > articles/ai-guide.txt << 'EOF'
# Artificial Intelligence: A Comprehensive Guide

Artificial Intelligence (AI) represents the frontier of computer science.

## What is AI?

AI enables machines to simulate human intelligence through:
- Learning and adaptation
- Problem-solving capabilities
- Decision-making processes

## Modern AI Approaches

### Deep Learning
Neural networks with multiple layers that can learn complex patterns.

### Natural Language Processing
Teaching computers to understand and generate human language.

### Computer Vision
Enabling machines to interpret and understand visual information.

## The Future of AI

AI continues to evolve rapidly, with applications in:
- Healthcare diagnostics
- Financial forecasting
- Smart assistants
- Robotics and automation

## Ethical Considerations

As AI grows more powerful, we must consider:
- Privacy concerns
- Algorithmic bias
- Job displacement
- AI safety and control
EOF

git rm draft.txt
git add articles/ai-guide.txt
git commit -m "Rewrite draft as comprehensive AI guide"

# Check detection (should show as delete + create, not rename)
git show --stat -M
git show --stat -M30%  # Even with lower threshold
```

## Understanding the Results

### Commands to analyze rename detection:

```bash
# Show changes with rename detection (default 50% threshold)
git log --stat -M

# Show with custom threshold (e.g., 30%)
git log --stat -M30%

# Show detailed diff with rename detection
git log -p -M

# See what Git thinks about your working directory
git diff --stat -M
git diff --name-status -M
```

### Key flags:

- `-M` or `-M50%`: Detect renames (50% similarity threshold)
- `-M30%`: Lower threshold (30% similarity)
- `-M90%`: Higher threshold (90% similarity)
- `--find-renames`: Same as `-M`
- `-C`: Also detect copies (more expensive)

## Best Practices

1. **Separate commits**: Move/rename files separately from content changes
2. **Use git mv**: While not technically different, it's clearer in intent
3. **Review with -M**: Always use `-M` when reviewing refactoring commits
4. **Configure Git**: Set `diff.renames = true` in your config

```bash
git config diff.renames true
git config diff.renameLimit 999
```
