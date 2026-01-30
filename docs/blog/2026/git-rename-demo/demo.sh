#!/bin/bash

# Git Rename Detection Demo Script
# This script demonstrates how Git detects file renames based on content similarity

set -e  # Exit on error

DEMO_REPO="git-rename-test-repo"

echo "=========================================="
echo "Git Rename Detection Demo"
echo "=========================================="
echo ""

# Cleanup previous demo if exists
if [ -d "$DEMO_REPO" ]; then
    echo "Cleaning up previous demo..."
    rm -rf "$DEMO_REPO"
fi

# Create a fresh demo repository
echo "Creating demo repository..."
mkdir "$DEMO_REPO"
cd "$DEMO_REPO"
git init
git config user.name "Demo User"
git config user.email "demo@example.com"
echo ""

#########################################
# SCENARIO 1: Move without changes
#########################################

echo "=========================================="
echo "SCENARIO 1: Move file without changes"
echo "=========================================="
echo ""

echo "Creating article.txt..."
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
git commit -m "Add article.txt" -q
echo "✓ Created and committed article.txt"
echo ""

echo "Moving article.txt to docs/article.txt (no content change)..."
mkdir docs
git mv article.txt docs/article.txt
git commit -m "Move article to docs folder" -q
echo "✓ Moved file"
echo ""

echo "Git detection result:"
git show --stat -M HEAD
echo ""
echo "Notice: Git shows 'article.txt => docs/article.txt' (100% similarity)"
echo ""
read -p "Press Enter to continue to Scenario 2..."
echo ""

#########################################
# SCENARIO 2: Move with minor changes
#########################################

echo "=========================================="
echo "SCENARIO 2: Move with minor changes"
echo "=========================================="
echo ""

echo "Creating tutorial.txt..."
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
git commit -m "Add tutorial.txt" -q
echo "✓ Created and committed tutorial.txt"
echo ""

echo "Moving to guides/python-tutorial.txt and adding minor changes..."
mkdir -p guides
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

git rm tutorial.txt -q
git add guides/python-tutorial.txt
git commit -m "Move tutorial and add minor improvements" -q
echo "✓ Moved and modified file"
echo ""

echo "Git detection result:"
git show --stat -M HEAD
echo ""
echo "Notice: Git still detects this as a rename with ~85% similarity"
echo ""
read -p "Press Enter to continue to Scenario 3..."
echo ""

#########################################
# SCENARIO 3: Move with major changes
#########################################

echo "=========================================="
echo "SCENARIO 3: Move with major changes"
echo "=========================================="
echo ""

echo "Creating draft.txt..."
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
git commit -m "Add ML draft" -q
echo "✓ Created and committed draft.txt"
echo ""

echo "Moving to articles/ai-guide.txt and completely rewriting..."
mkdir -p articles
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

git rm draft.txt -q
git add articles/ai-guide.txt
git commit -m "Rewrite draft as comprehensive AI guide" -q
echo "✓ Moved and completely rewrote file"
echo ""

echo "Git detection result:"
git show --stat -M HEAD
echo ""
echo "Notice: Git shows 'draft.txt' deleted and 'articles/ai-guide.txt' created"
echo "The content changed too much for Git to detect it as a rename"
echo ""

#########################################
# SUMMARY
#########################################

echo "=========================================="
echo "SUMMARY - Full commit history"
echo "=========================================="
echo ""

echo "With rename detection (default 50% threshold):"
git log --oneline --stat -M --reverse
echo ""

echo "=========================================="
echo "Experiment with different thresholds:"
echo "=========================================="
echo ""

echo "With 30% threshold (-M30%):"
git log --oneline --name-status -M30% --reverse
echo ""

echo "With 90% threshold (-M90%):"
git log --oneline --name-status -M90% --reverse
echo ""

echo "=========================================="
echo "Demo complete!"
echo "=========================================="
echo ""
echo "The demo repository is in: $DEMO_REPO"
echo "You can explore it with commands like:"
echo "  cd $DEMO_REPO"
echo "  git log --stat -M"
echo "  git log -p -M"
echo "  git log --name-status -M30%"
echo ""
