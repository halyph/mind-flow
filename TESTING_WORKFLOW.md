# Safe Workflow Testing Guide

## Option 1: Test Branch Method (Recommended)

### Steps:
1. Create a test branch:
   ```bash
   git checkout -b test-deploy
   ```

2. Push to trigger the test workflow:
   ```bash
   git push origin test-deploy
   ```

3. Check the workflow run:
   - Go to: https://github.com/halyph/mind-flow/actions
   - Look for "Test CI" workflow
   - Monitor the build

4. Verify the test deployment:
   - Go to: https://github.com/halyph/halyph.github.io/tree/test-deploy
   - Check the files are correct
   - You can download the branch to view locally

5. If everything works, merge changes to master:
   ```bash
   git checkout master
   git merge test-deploy
   git push origin master
   ```

## Option 2: Manual Trigger Method

### Steps:
1. Go to Actions tab: https://github.com/halyph/mind-flow/actions
2. Select "Test CI" workflow
3. Click "Run workflow" button
4. Choose the branch to test
5. Click "Run workflow"

This won't deploy to production - it deploys to `test-deploy` branch.

## Option 3: Local Testing with Act

Install act (GitHub Actions runner):
```bash
brew install act
```

Test the workflow locally:
```bash
# Dry run - see what would happen
act -n

# Run the workflow (won't actually deploy)
act push --secret-file .secrets
```

Create `.secrets` file:
```
GOOGLE_ANALYTICS_KEY=your_key_here
SSH_DEPLOY_KEY=your_key_here
```

**Note:** Local testing won't do actual deployment, but validates the build.

## Option 4: Build-Only Test

Add a build-only workflow that doesn't deploy:

```yaml
name: Build Test
on:
  pull_request:
  push:
    branches-ignore: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
          cache: 'pip'
      - run: pip install -r requirements.txt
      - run: mkdocs build -f mkdocs.ci.yml
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: site
          path: site/
```

Download the artifact to verify the build locally.

## Safety Checklist

Before updating production workflow:

- [ ] Test workflow runs successfully
- [ ] Build completes without errors
- [ ] All pages are generated correctly
- [ ] Assets (CSS, JS, images) are present
- [ ] No broken links
- [ ] Build time is acceptable
- [ ] Test deployment to `test-deploy` branch works

## Rollback Plan

If production deployment fails:

1. Revert the workflow file:
   ```bash
   git checkout HEAD~1 .github/workflows/ci.yaml
   git commit -m "Revert workflow changes"
   git push
   ```

2. Or manually trigger old workflow from GitHub UI

3. Check halyph.github.io repository history and force push previous commit if needed:
   ```bash
   cd /path/to/halyph.github.io
   git log  # Find the last good commit
   git reset --hard <commit-hash>
   git push --force
   ```

## Monitoring

After deploying to production:
1. Check workflow run completes: https://github.com/halyph/mind-flow/actions
2. Verify site is live: https://halyph.github.io
3. Check build time improved
4. Monitor for any errors in Actions tab

## Progressive Rollout

Test changes incrementally:

### Phase 1: Non-Breaking Changes
- Update action versions (@v3 → @v4)
- Add caching
- Change fetch-depth

### Phase 2: Deployment Method
- Switch from Docker action to peaceiris/actions-gh-pages
- Test on `test-deploy` branch first

### Phase 3: Optimization
- Adjust MkDocs settings
- Fine-tune caching strategies
